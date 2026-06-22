## Python 环境管理

本项目使用 [uv](https://docs.astral.sh/uv/) 进行 Python 环境管理。

### 基本使用

#### 创建虚拟环境

```bash
# 在当前目录创建虚拟环境
uv venv

# 指定 Python 版本
uv venv --python 3.11

# 指定环境名称
uv venv .venv-dev
```

#### 激活虚拟环境

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

#### 安装依赖

```bash
# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 安装单个包
uv pip install package-name

# 安装特定版本
uv pip install package-name==1.0.0

# 安装开发依赖
uv pip install -e ".[dev]"
```

#### 导出依赖

```bash
# 导出当前环境依赖
uv pip freeze > requirements.txt

# 导出精简依赖（不含子依赖）
uv pip compile requirements.in -o requirements.txt
```

#### 运行脚本

```bash
# 在虚拟环境中直接运行（无需激活）
uv run script.py

# 运行模块
uv run -m module_name
```

### 常用命令速查

| 命令 | 说明 |
|------|------|
| `uv venv` | 创建虚拟环境 |
| `uv pip install <package>` | 安装包 |
| `uv pip install -r requirements.txt` | 批量安装依赖 |
| `uv pip freeze` | 列出已安装的包 |
| `uv pip list` | 列出已安装的包（表格形式） |
| `uv pip uninstall <package>` | 卸载包 |
| `uv run <script>` | 在虚拟环境中运行脚本 |
| `uv pip compile requirements.in` | 锁定依赖版本 |

### Skills 环境配置

pdf 和 docx skills 已安装在 `~/.claude/skills/` 目录下。每个 skill 使用独立的虚拟环境：

```bash
# pdf skill 环境
cd ~/.claude/skills/pdf
uv venv
source .venv/bin/activate
uv pip install pypdf pdfplumber reportlab pytesseract pdf2image

# docx skill 环境
cd ~/.claude/skills/docx
uv venv
source .venv/bin/activate
uv pip install python-docx lxml
```

### 项目环境配置

```bash
# 初始化项目环境
cd /home/darstib/ZJUCourse/IoTSec
uv venv
source .venv/bin/activate

# 如果有 requirements.txt
uv pip install -r requirements.txt

# 如果有 pyproject.toml
uv pip install -e .
```

### 多环境管理

使用不同名称创建多个环境：

```bash
# 开发环境
uv venv .venv-dev --python 3.11

# 测试环境
uv venv .venv-test --python 3.10

# 生产环境
uv venv .venv-prod --python 3.11
```

### 故障排除

**问题：找不到 Python 版本**
```bash
# 查看可用的 Python 版本
uv python list

# 安装特定版本
uv python install 3.11
```

**问题：依赖冲突**
```bash
# 使用 pip compile 解决依赖冲突
uv pip compile requirements.in --resolver=backtracking
```

**问题：虚拟环境激活失败**
```bash
# 确保使用正确的 shell
echo $SHELL

# 或直接使用 uv run（无需激活）
uv run python script.py
```