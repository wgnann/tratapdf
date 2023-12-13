# tratapdf
Trata PDF para torná-lo compatível com PDF/X e com impressoras em escala de cinza.

## dependências
  - icc-profiles
  - ghostscript
  - poppler-utils
  - python3-tk
  - texlive-extra-utils
  - visualizador de PDF (nesta versão usamos o evince hardcoded)

## instalação no Debian 12
  - clonar o repositório;
  - configurar as variáveis no `trata.py` e no `setup.sh`:
    - `BASE_DIR`: diretório onde ficarão os recursos;
    - `GHOSTSCRIPT`: caminho para o gs;
    - `PDF_INFO`: caminho para o pdfinfo;
    - `PDF_JAM`: caminho para o pdfjam;
    - `PDF_VIEWER`: caminho para o visualizador;
  - rodar `setup.sh`.

## como rodar?
Executar `python3 <caminho-para-trata.py>`. Outra opção é criar um _launcher_ para o programa. Nesse caso é recomendável usar o path completo do Python bem como marcar o _launcher_ como executável. 

Será criado um arquivo com o mesmo nome do tratado, mas com o sufixo `-tratado`.
