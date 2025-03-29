import os
import subprocess
import sys
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

# Try importing Pillow
try:
    from PIL import Image
    pillow_installed = True
except ImportError:
    pillow_installed = False

# Function to install Pillow if missing
def install_pillow():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        messagebox.showinfo("Success", "Pillow installed. Please restart the app.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to install Pillow:\n{e}")

# Folder picker
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, "end")
        path_entry.insert(0, folder)

# File picker
def browse_file():
    file = filedialog.askopenfilename(filetypes=[("WebP files", "*.webp")])
    if file:
        path_entry.delete(0, "end")
        path_entry.insert(0, file)

# Conversion logic
def convert_images():
    input_path = path_entry.get().strip()
    if not os.path.exists(input_path):
        messagebox.showerror("Error", "Invalid path.")
        return

    converted = 0

    # Folder mode
    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.lower().endswith(".webp"):
                full_path = os.path.join(input_path, filename)
                output_path = os.path.splitext(full_path)[0] + ".jpg"
                try:
                    im = Image.open(full_path)
                    im.save(output_path, "JPEG")
                    converted += 1
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")
    # Single file mode
    elif input_path.lower().endswith(".webp"):
        output_path = os.path.splitext(input_path)[0] + ".jpg"
        try:
            im = Image.open(input_path)
            im.save(output_path, "JPEG")
            converted += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert:\n{e}")
            return
    else:
        messagebox.showwarning("Warning", "Selected file is not a .webp image.")
        return

    messagebox.showinfo("Done", f"Converted {converted} .webp file(s) to .jpg")

# ---------------------- GUI ----------------------

root = Tk()
root.title("WebP to JPG Converter")

# Set fixed small window size
window_width = 300
window_height = 200
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)

# Center the layout using grid
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Install Pillow if needed
if not pillow_installed:
    install_btn = Button(root, text="Install Pillow", command=install_pillow)
    install_btn.grid(row=1, column=1, columnspan=1, pady=(10, 5))

# Label on top
Label(root, text="Paste or browse a .webp file or folder").grid(row=0, column=0, columnspan=3, pady=(10, 5))

# Entry field for path
path_entry = Entry(root, width=40)
path_entry.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 10))

# Browse buttons (side-by-side)
Button(root, text="Browse File", width=12, command=browse_file).grid(row=3, column=0, columnspan=1, padx=20, pady=5)
Button(root, text="Browse Folder", width=12, command=browse_folder).grid(row=3, column=1, columnspan=1, padx=0, pady=5)

# Apply button (larger)
apply_btn = Button(root, text="Apply", width=15, height=3, command=convert_images, state="normal" if pillow_installed else "disabled")
apply_btn.grid(row=4, column=0, columnspan=3, pady=(10, 5))

root.mainloop()
