import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def list_files_dirs():
    output.delete("1.0", tk.END)
    files = os.listdir(".")
    for f in files:
        output.insert(tk.END, f + "\n")

def create_file():
    ext = simpledialog.askstring("File Type", "Enter file extension (e.g., .txt, .c, .sh):")
    name = simpledialog.askstring("Create File", "Enter file name without extension:")
    if name and ext:
        full_name = name + ext
        open(full_name, "w").close()
        list_files_dirs()

def delete_file():
    name = simpledialog.askstring("Delete File", "Enter file name to delete:")
    if name and os.path.exists(name):
        os.remove(name)
        list_files_dirs()
    else:
        messagebox.showerror("Error", "File not found")

def rename_file():
    old = simpledialog.askstring("Rename File", "Enter current file name:")
    new = simpledialog.askstring("Rename File", "Enter new file name:")
    if old and new and os.path.exists(old):
        os.rename(old, new)
        list_files_dirs()
    else:
        messagebox.showerror("Error", "File not found")

def edit_file():
    name = simpledialog.askstring("Edit File", "Enter file name to edit:")
    if name and os.path.exists(name):
        os.system(f"nano {name}")
        list_files_dirs()
    else:
        messagebox.showerror("Error", "File not found")

def search_file():
    name = simpledialog.askstring("Search File", "Enter file name to search:")
    result = os.popen(f"find . -name '{name}'").read()
    output.delete("1.0", tk.END)
    output.insert(tk.END, result if result else "File not found")

def file_details():
    name = simpledialog.askstring("File Details", "Enter file name:")
    if name and os.path.exists(name):
        result = os.popen(f"stat {name}").read()
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    else:
        messagebox.showerror("Error", "File not found")

def view_content():
    name = simpledialog.askstring("View File", "Enter file name:")
    if name and os.path.exists(name):
        with open(name, "r") as f:
            content = f.read()
        output.delete("1.0", tk.END)
        output.insert(tk.END, content)
    else:
        messagebox.showerror("Error", "File not found")

def sort_file_content():
    name = simpledialog.askstring("Sort Content", "Enter file name:")
    if name and os.path.exists(name):
        with open(name, "r") as f:
            lines = f.readlines()
        lines.sort()
        output.delete("1.0", tk.END)
        output.insert(tk.END, ''.join(lines))
    else:
        messagebox.showerror("Error", "File not found")

def list_directories():
    output.delete("1.0", tk.END)
    dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
    for d in dirs:
        output.insert(tk.END, d + "/\n")

def list_by_extension():
    ext = simpledialog.askstring("File Extension", "Enter extension (e.g., .txt):")
    output.delete("1.0", tk.END)
    for f in os.listdir("."):
        if f.endswith(ext):
            output.insert(tk.END, f + "\n")

def count_directories():
    count = len([d for d in os.listdir(".") if os.path.isdir(d)])
    messagebox.showinfo("Directory Count", f"Total directories: {count}")

def count_files():
    count = len([f for f in os.listdir(".") if os.path.isfile(f)])
    messagebox.showinfo("File Count", f"Total files: {count}")

def sort_files():
    files = sorted(os.listdir("."))
    output.delete("1.0", tk.END)
    for f in files:
        output.insert(tk.END, f + "\n")

def create_folder():
    folder = simpledialog.askstring("Create Folder", "Enter folder name:")
    if folder:
        os.mkdir(folder)
        list_files_dirs()

def move_file():
    src = simpledialog.askstring("Move File", "Enter source file name:")
    dst = simpledialog.askstring("Move File", "Enter destination folder:")
    if src and dst:
        shutil.move(src, dst)
        list_files_dirs()

def copy_file():
    src = simpledialog.askstring("Copy File", "Enter source file name:")
    dst = simpledialog.askstring("Copy File", "Enter destination file name:")
    if src and dst:
        shutil.copy(src, dst)
        list_files_dirs()

def open_file_default():
    name = simpledialog.askstring("Open File", "Enter file name:")
    if name and os.path.exists(name):
        os.system(f"xdg-open '{name}'")
    else:
        messagebox.showerror("Error", "File not found")

root = tk.Tk()
root.title("File Management System - GUI Version")

buttons = [
    ("1. List Files/Dirs", list_files_dirs),
    ("2. Create File", create_file),
    ("3. Delete File", delete_file),
    ("4. Rename File", rename_file),
    ("5. Edit File", edit_file),
    ("6. Search File", search_file),
    ("7. File Details", file_details),
    ("8. View File Content", view_content),
    ("9. Sort File Content", sort_file_content),
    ("10. List Directories", list_directories),
    ("11. List Files by Extension", list_by_extension),
    ("12. Count Directories", count_directories),
    ("13. Count Files", count_files),
    ("14. Sort Files in Directory", sort_files),
    ("15. Create Folder", create_folder),
    ("16. Move File", move_file),
    ("17. Copy File", copy_file),
    ("18. Open File with Default App", open_file_default)
]

for (text, cmd) in buttons:
    tk.Button(root, text=text, command=cmd).pack(fill=tk.X)

output = tk.Text(root, height=20, width=80)
output.pack()

root.mainloop()