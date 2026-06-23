"""
从 ch9 指令选择.pdf 中提取关键页面为图片。
根据课件内容，以下页面包含重要图示：
- Page 11: Jouette 指令集（树模式表）
- Page 14: Tree Patterns for Jouette
- Page 15: Multiple Patterns for ADDI
- Page 19-20: Tiling for Memory Load
- Page 21: Tiling for a[i] := x
- Page 22: Instruction Emission
- Page 25: Tiling with Another Strategy
- Page 29: Optimal vs Optimum example
- Page 35: Maximal Munch start
- Page 36-41: Maximal Munch step-by-step
- Page 55: Dynamic Programming example start
- Page 56-58: Dynamic Programming step-by-step
- Page 59: DP Instruction Emission
- Page 69: Tree Grammar parsing example
- Page 73: RISC vs CISC comparison
"""
import fitz  # PyMuPDF
import os

PDF_PATH = "slide/ch9 指令选择.pdf"
OUTPUT_DIR = "note/assets/chapter9-instruction-selection"

# 页面编号（1-indexed）和对应文件名
PAGES = [
    (11, "ch9-p11-jouette-instructions.png"),
    (14, "ch9-p14-tree-patterns.png"),
    (15, "ch9-p15-multiple-patterns.png"),
    (19, "ch9-p19-tiling-memory-load.png"),
    (21, "ch9-p21-tiling-array-assign.png"),
    (22, "ch9-p22-instruction-emission.png"),
    (25, "ch9-p25-small-tiles.png"),
    (29, "ch9-p29-optimal-vs-optimum.png"),
    (35, "ch9-p35-mm-start.png"),
    (36, "ch9-p36-mm-step1.png"),
    (37, "ch9-p37-mm-step2.png"),
    (38, "ch9-p38-mm-step3.png"),
    (39, "ch9-p39-mm-step4.png"),
    (40, "ch9-p40-mm-step5.png"),
    (41, "ch9-p41-mm-step6.png"),
    (55, "ch9-p55-dp-example.png"),
    (56, "ch9-p56-dp-const.png"),
    (57, "ch9-p57-dp-plus.png"),
    (58, "ch9-p58-dp-mem.png"),
    (59, "ch9-p59-dp-emission.png"),
    (69, "ch9-p69-tree-grammar.png"),
    (73, "ch9-p73-risc-vs-cisc.png"),
]

def extract_pages(pdf_path, output_dir, pages, dpi=200):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    for page_num, filename in pages:
        page = doc[page_num - 1]  # fitz 用 0-indexed
        # 渲染为图片
        mat = fitz.Matrix(dpi / 72, dpi / 72)  # 72 是默认 DPI
        pix = page.get_pixmap(matrix=mat)
        
        output_path = os.path.join(output_dir, filename)
        pix.save(output_path)
        print(f"Saved page {page_num} -> {filename} ({pix.width}x{pix.height})")
    
    doc.close()
    print(f"\nDone! Extracted {len(pages)} pages to {output_dir}")

if __name__ == "__main__":
    extract_pages(PDF_PATH, OUTPUT_DIR, PAGES)
