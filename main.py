import fitz  # PyMuPDF

def split_pdf(input_pdf, output_prefix):
    doc = fitz.open(input_pdf)
    total_pages = len(doc)
    
    for i in range(0, total_pages, 2):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=i, to_page=min(i+1, total_pages-1))
        output_filename = f"{output_prefix}_part_{i//2 + 1}.pdf"
        new_doc.save(output_filename)
        new_doc.close()
        print(f"Created: {output_filename}")
    
    doc.close()

# Exemplo de uso
input_pdf = "documento.pdf"  # Substitua pelo seu arquivo
output_prefix = "output"  # Prefixo dos arquivos de saída
split_pdf(input_pdf, output_prefix)
