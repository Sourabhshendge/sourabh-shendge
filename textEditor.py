import tkinter as tk
from tkinter.constants import INSERT
from tkinter.filedialog import askopenfilename, asksaveasfilename

global selected


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

def cut_file():
    global selected
    if txt_edit.selection_get():
        selected = txt_edit.selection_get()
        txt_edit.delete("sel.first","sel.last")



def copy_file():
    if txt_edit.selection_get():
        selected = txt_edit.selection_get()

def paste_file():
    if selected:
        position=txt_edit.index(INSERT)
        txt_edit.insert(position,selected)


window = tk.Tk()
window.title("Text Editor Application")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_copy = tk.Button(fr_buttons, text="Copy", command=copy_file)
btn_cut = tk.Button(fr_buttons, text="Cut", command=cut_file)
btn_paste = tk.Button(fr_buttons, text="Paste", command=paste_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_copy.grid(row=2, column=0, sticky="ew", padx=5)
btn_cut.grid(row=3, column=0, sticky="ew", padx=5)
btn_paste.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()