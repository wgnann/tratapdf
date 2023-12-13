import os
import re
import subprocess
import sys
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

BASE_DIR = os.getcwd()
GHOSTSCRIPT = '/usr/bin/gs'
PDF_INFO = '/usr/bin/pdfinfo'
PDF_VIEWER = '/usr/bin/evince'

def novo_nome(path):
    sufixo = '-tratado'
    base = os.path.dirname(path)
    original = os.path.basename(path)
    arquivo = os.path.splitext(original)[0]
    extensao = os.path.splitext(original)[1]

    return base+'/'+arquivo+sufixo+extensao

class Tratador:
    def __init__(self, mode):
        if (mode == 'cli'):
            self.cli(sys.argv[1])
        else:
            self.gui()

    def gui(self):
        self.window = tkinter.Tk()
        lbl_aviso = tkinter.Label(text="Tratador de PDF para impressão", height=2)
        lbl_aviso.pack()
        btn_abrir = tkinter.Button(text="Abrir PDF", height=2)
        btn_abrir.bind("<Button-1>", self.tratar_pdf)
        btn_abrir.pack()
        self.window.mainloop()

    def tratar_pdf(self, event):
        viewer = PDF_VIEWER
        path = askopenfilename(
            filetypes=[("PDF", "*.pdf")],
            initialdir=os.path.expanduser('~')
        )
        output = novo_nome(path)
        returncode = self.pdfx(path)
        if (returncode != 0):
            showerror("Erro", "Erro ao processar arquivo. Tem certeza que é um PDF?")
        else:
            subprocess.run([
                viewer, output
            ])
        self.window.destroy()

    def cli(self, path):
        output = novo_nome(path)
        returncode = self.pdfx(path)
        if (returncode != 0):
            print("Erro ao processar arquivo.")
        else:
            print("Arquivo {output} criado.".format(output=output))

    def pdfinfo(self, path):
        pdfinfo = PDF_INFO

        process = subprocess.run([pdfinfo, path], capture_output=True)
        if (process.returncode != 0):
            print("Problema no PDF: tamanho indefinido")
            raise

        matches = re.search('Page size:\s+(\d+\.?\d+)\sx\s(\d+\.?\d+)', process.stdout.decode())
        info = {}
        info['width'] = matches[1]
        info['height'] = matches[2]

        return info

    # devolve process.returncode
    def pdfx(self, path):
        gs = GHOSTSCRIPT
        base = BASE_DIR
        output = novo_nome(path)

        process = subprocess.run([
            gs, '-dBATCH', '-dNOPAUSE',
            '-dPDFX',
            '-sDEVICE=pdfwrite',
            '-sColorConversionStrategy=Gray',
            '-sPDFSETTINGS=prepress',
            '-sOutputFile={output}'.format(output=output),
            '-I', base, '{base}/PDFX_def.ps'.format(base=base),
            path
        ])

        return process.returncode

def main():
    mode = 'gui'
    if (len(sys.argv) > 1):
        mode = 'cli'
    Tratador(mode)
main()
