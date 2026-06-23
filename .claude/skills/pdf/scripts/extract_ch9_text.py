"""Extract text from ch9 指令选择.pdf"""
from pypdf import PdfReader
import sys

def extract_pdf_text(pdf_path, output_path=None):
    """Extract text from all pages of a PDF file."""
    reader = PdfReader(pdf_path)
    
    all_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        all_text.append(f"=== Page {i+1} ===\n{text}\n")
    
    result = "\n".join(all_text)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Text written to {output_path}")
    else:
        print(result)
    
    return result

if __name__ == "__main__":
    pdf_path = "slide/ch9 指令选择.pdf"
    output_path = "note/assets/_tmp_ch9_text.txt"
    extract_pdf_text(pdf_path, output_path)
