# tratapdf
Trata PDF para torná-lo compatível com PDF/X e com impressoras em escala de cinza.

## dependências
  - icc-profiles
  - ghostscript
  - visualizador de PDF (nesta versão usamos o evince hardcoded)

## instalação no Debian 11
  - clonar o repositório;
  - configurar as variáveis:
    - `BASE_DIR`: diretório onde ficarão os recursos;
    - `GHOSTSCRIPT`: caminho para o executável;
    - `PDF_VIEWER`: caminho para o executável;
  - copiar os arquivos abaixo para o `BASE_DIR`:
    - `/usr/share/ghostscript/9.53.3/lib/PDFX_def.ps`;
    - `/usr/share/color/icc/ISOuncoated.icc`.
  - editar o `PDFX_def.ps`, substituindo o que está entre `()` na linha começada por `/ICCProfile` para o caminho para o `ISOuncoated.icc` recém copiado.
Exemplo: `/ICCProfile (/tmp/tratapdf/ISOuncoated.icc) def`.

## como rodar?
Executar `python3 <caminho-para-trata.py>`. Outra opção é criar um _launcher_ para o programa. Nesse caso é recomendável usar o path completo do Python bem como marcar o _launcher_ como executável. 

Será criado um arquivo com o mesmo nome do tratado, mas com o sufixo `-tratado`.
