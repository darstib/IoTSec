# Claude Code Skills

本项目已安装以下技能：

## PDF 技能

**位置**: `pdf/`  
**环境**: `pdf/.venv/`  
**激活**: `source pdf/.venv/bin/activate`

### 功能
- 读取和提取 PDF 文本/表格
- 合并/拆分 PDF 文件
- 旋转页面、添加水印
- 创建新 PDF
- 填写 PDF 表单
- 加密/解密 PDF
- 提取图像
- OCR 扫描 PDF

### 依赖包
- pypdf >= 4.0.0
- pdfplumber >= 0.11.0
- reportlab >= 4.0.0
- pytesseract >= 0.3.10
- pdf2image >= 1.17.0
- pillow >= 10.0.0

### 文档
详见 `pdf/SKILL.md` 和 `pdf/reference.md`

---

## DOCX 技能

**位置**: `docx/`  
**环境**: `docx/.venv/`  
**激活**: `source docx/.venv/bin/activate`

### 功能
- 创建、读取、编辑 Word 文档
- 处理追踪修订和注释
- 插入/替换图像
- 查找和替换内容
- 转换 .doc 到 .docx
- 处理专业文档格式（目录、页眉页脚等）

### 依赖包
- defusedxml >= 0.7.0
- docx (Node.js): `npm install -g docx`
- pandoc: 文本提取
- LibreOffice: PDF 转换

### 文档
详见 `docx/SKILL.md`

---

## PPTX 技能

**位置**: `pptx/`  
**环境**: `pptx/.venv/`  
**激活**: `source pptx/.venv/bin/activate`

### 功能
- 创建幻灯片、演示文稿
- 读取、解析、提取 PPTX 文本
- 编辑、修改、更新现有演示文稿
- 合并或拆分幻灯片文件
- 处理模板、布局、备注、注释
- 生成缩略图预览

### 依赖包
- defusedxml >= 0.7.0
- pillow >= 10.0.0
- markitdown >= 0.0.1a2 (文本提取)
- pptxgenjs (Node.js): `npm install -g pptxgenjs` (从头创建)
- LibreOffice: 转换和渲染

### 文档
详见 `pptx/SKILL.md`、`pptx/editing.md`、`pptx/pptxgenjs.md`

---

## 使用方法

在项目根目录下，Claude Code 会自动检测并加载这些技能。当你需要处理 PDF、DOCX 或 PPTX 文件时，直接告诉 Claude 即可。

### 示例

```
# PDF 操作
"帮我合并这三个 PDF 文件"
"提取 report.pdf 的所有表格"
"将这个扫描的 PDF 转换为可搜索文本"

# DOCX 操作
"创建一个带目录的 Word 报告"
"读取 contract.docx 并接受所有修订"
"在文档中插入图片"

# PPTX 操作
"创建一个演示文稿，包含公司介绍"
"提取 slides.pptx 的所有文本内容"
"生成演示文稿的缩略图预览"
```

---

## 维护

### 更新依赖

PDF:
```bash
cd pdf
source .venv/bin/activate
uv pip install --upgrade pypdf pdfplumber reportlab
```

DOCX:
```bash
cd docx
source .venv/bin/activate
uv pip install --upgrade defusedxml
```

PPTX:
```bash
cd pptx
source .venv/bin/activate
uv pip install --upgrade defusedxml pillow markitdown
```

### 重建环境

如果环境损坏，可以删除 `.venv/` 目录并重新安装：

```bash
# PDF
cd pdf
rm -rf .venv
uv venv
uv pip install -e .

# DOCX
cd docx
rm -rf .venv
uv venv
uv pip install -e .

# PPTX
cd pptx
rm -rf .venv
uv venv
uv pip install -e .
```
