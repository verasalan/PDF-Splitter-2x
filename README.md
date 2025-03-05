# PDF-Splitter-2x
O PDF Splitter 2x é uma automação eficiente para dividir arquivos PDF em partes menores, separando automaticamente as páginas em blocos de 2. Essa ferramenta é ideal para quem precisa processar documentos de forma rápida e prática, facilitando a organização, impressão e manipulação de arquivos grandes.

## Descrição
Este script em Python permite dividir um arquivo PDF de múltiplas páginas em arquivos menores, contendo 2 páginas cada. Utiliza a biblioteca `PyMuPDF` (`fitz`) para manipulação dos arquivos PDF.

## Pré-requisitos
Antes de executar o script, certifique-se de ter o Python instalado e a biblioteca necessária instalada. Você pode instalá-la com o seguinte comando:

```bash
pip install pymupdf
```

## Como Usar
1. Coloque o arquivo PDF que deseja dividir no mesmo diretório do script.
2. Edite a variável `input_pdf` no código para corresponder ao nome do seu arquivo.
3. Execute o script Python:

```bash
python split_pdf.py
```

4. Os arquivos gerados serão nomeados com o prefixo definido em `output_prefix`, por exemplo:
   - `output_part_1.pdf`
   - `output_part_2.pdf`
   - ...

## Personalização
- Altere o valor de `input_pdf` para especificar o arquivo de entrada.
- Modifique `output_prefix` para definir um prefixo diferente para os arquivos gerados.

## Exemplo de Uso
Se o arquivo de entrada for `documento.pdf` com 6 páginas, o script gerará:
- `output_part_1.pdf` (páginas 1 e 2)
- `output_part_2.pdf` (páginas 3 e 4)
- `output_part_3.pdf` (páginas 5 e 6)

## Resumo
Este script foi desenvolvido para facilitar a separação de páginas em arquivos PDF, permitindo um processamento mais eficiente de documentos grandes.


