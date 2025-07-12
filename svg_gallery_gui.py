import os
import webbrowser
from tkinter import Tk, Label, Button, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

def generate_html(folder_path):
    svg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.svg')]
    if not svg_files:
        messagebox.showinfo("No SVG Found", "No SVG files found in the selected folder.")
        return

    html_path = os.path.join(folder_path, 'gallery.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SVG Gallery</title>
  <style>
    body { display: flex; flex-wrap: wrap; gap: 10px; padding: 20px; background: #f8f8f8; }
    img { width: 100px; height: 100px; object-fit: contain; border: 1px solid #ccc; padding: 5px; background: #fff; }
  </style>
</head>
<body>
''')
        for svg in svg_files:
            f.write(f'  <img src="{svg}" alt="{svg}">\n')
        f.write('</body>\n</html>')

    webbrowser.open(f'file://{html_path}')
    messagebox.showinfo("Done", "gallery.html has been created and opened in your browser.")

def on_drop(event):
    path = event.data.strip('{}')  # remove { } around path
    if os.path.isdir(path):
        generate_html(path)
    else:
        messagebox.showerror("Invalid Drop", "Please drop a valid folder containing SVG files.")

def browse_folder():
    folder = filedialog.askdirectory(title="Select Folder with SVG Files")
    if folder:
        generate_html(folder)

# GUI Setup
root = TkinterDnD.Tk()
root.title("SVG Gallery Generator")
root.geometry("420x200")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

label = Label(root, text="Drag and drop a folder here\nor click the button below", bg="#f0f0f0",
              font=("Segoe UI", 12), relief="solid", borderwidth=2, width=40, height=5)
label.pack(pady=20)

browse_btn = Button(root, text="Browse Folder", command=browse_folder, font=("Segoe UI", 10))
browse_btn.pack(pady=5)

label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
