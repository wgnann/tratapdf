import os
import subprocess
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

BASE_DIR = os.getcwd()
GHOSTSCRIPT = '/usr/bin/gs'
PDF_VIEWER = '/usr/bin/evince'

def novo_nome(path):
    sufixo = '-tratado'
    base = os.path.dirname(path)
    original = os.path.basename(path)
    arquivo = os.path.splitext(original)[0]
    extensao = os.path.splitext(original)[1]

    return base+'/'+arquivo+sufixo+extensao

class Tratador:
    def __init__(self):
        self.window = tkinter.Tk()
        lbl_aviso = tkinter.Label(text="Tratador de PDF para impressão", height=2)
        lbl_aviso.pack()
        btn_abrir = tkinter.Button(text="Abrir PDF", height=2)
        btn_abrir.bind("<Button-1>", self.tratar_pdf)
        btn_abrir.pack()
        self.window.mainloop()

    def tratar_pdf(self, event):
        gs = GHOSTSCRIPT
        viewer = PDF_VIEWER
        base = BASE_DIR

        path = askopenfilename(
            filetypes=[("PDF", "*.pdf")],
            initialdir=os.path.expanduser('~')
        )

        if (path):
            output = novo_nome(path)

            process = subprocess.run([
                gs, '-dBATCH', '-dNOPAUSE',
                '-dPDFX',
                '-sDEVICE=pdfwrite',
                '-sColorConversionStrategy=Gray',
                '-sPDFSETTINGS=prepress',
                '-sOutputFile={output}'.format(output=output),
                '-I', base,
                '{base}/PDFX_def.ps'.format(base=base),
                path
            ])
            if (process.returncode != 0):
                showerror("Erro", "Erro ao processar arquivo. Tem certeza que é um PDF?")
            else:
                subprocess.run([
                    viewer, output
                ])

        self.window.destroy()

def main():
    Tratador()
main()
