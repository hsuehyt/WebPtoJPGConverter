# WebP to JPG Converter 🖼️

![Screenshot](https://github.com/hsuehyt/WebPtoJPGConverter/blob/main/images/Screenshot%202025-03-29%20161948.png)

A lightweight and beginner-friendly desktop tool to convert `.webp` images to `.jpg` using a simple graphical interface. Supports both individual files and batch conversion for folders.

## Features

- ✅ Convert single `.webp` files or entire folders
- 🖱️ Drag-and-click file/folder selection
- 💾 Saves output as `.jpg` in the same directory
- 🧱 Minimal, fixed-size UI (300×200 px)
- ⚙️ Automatically prompts to install Pillow (Python Imaging Library) if not found

---

## Installation

### Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (installed automatically if missing)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/hsuehyt/WebPtoJPGConverter.git
cd WebPtoJPGConverter
```

2. Run the script:

```bash
python convert_webp.py
```

> 💡 If Pillow is not installed, the app will prompt you to install it automatically.

---

## How to Use

1. Run the app (`convert_webp.py`)
2. Paste or browse to a `.webp` file or folder
3. Click **"Apply"** to convert
4. The converted `.jpg` files will appear alongside the original `.webp` files

---

## License

MIT License © [hsuehyt](https://github.com/hsuehyt)
