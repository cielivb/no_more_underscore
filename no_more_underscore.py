""" NO MORE UNDERSCORE

Generate a copyable list of all filenames from a user-specified 
directory with the filetype extension removed and all underscores replaced
with a space.

e.g., 2025_bound.pdf will be printed as 2025 bound

e.g., 1987_dwyer_et_al_meaning_of_pluto.docx will be printed as 
   1987 dwyer et al meaning of pluto
   
"""


### Imports ------------------------------------------------------------

import os
import pyperclip

from tkinter import Tk

from tkinter import Button
from tkinter import E
from tkinter import END
from tkinter import filedialog
from tkinter import Frame
from tkinter import INSERT
from tkinter import Label
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import W
from tkinter import Text
from tkinter import Toplevel
from tkinter import ttk



### Global variables ---------------------------------------------------

ROOT = None # Will be of type Tk when set
OUT_FIELD = None # Will be of type ScrolledText when set
DIR_LABEL = None # Will be of type Label when set
SELECTED_DIR = None # Will be of type string when set
COPY_NOTICE = None # Will be of type Label when set





### Core Logic ---------------------------------------------------------

def get_filenames():
    """Retrieve filename list without extensions from selected directory"""
    global SELECTED_DIR
    out_list = []
    for file in os.listdir(SELECTED_DIR):
        # Each file is of type string
        # Folders are of format foldername (not followed by .extension)
        # Files are of format filename.extension
        # This program includes files only
        if "." in file:
            out_list.append(".".join(file.split(".")[:-1]))  
    return out_list


def select_dir():
    """Open file dialog for user to select desired directory"""
    global SELECTED_DIR
    global DIR_LABEL
    SELECTED_DIR = filedialog.askdirectory(title="Choose directory")
    DIR_LABEL.config(text=SELECTED_DIR)    


def run():
    """Prompt user for directory and execute underscore replacement"""
    global OUT_FILED
    
    select_dir()
    filenames = get_filenames()
    output = ""
    for file in filenames:
        file = file.replace("_", " ")
        output = output + file + "\n"
    
    OUT_FIELD.configure(state='normal')    
    OUT_FIELD.delete("1.0", END)
    OUT_FIELD.insert(INSERT, output)
    OUT_FIELD.configure(state='disabled')
    




### Copy output logic --------------------------------------------------

def hide_copy_notice():
    """Make copy notice label the same colour as window background"""
    global COPY_NOTICE
    COPY_NOTICE.config(bg=ROOT.cget("bg"), fg=ROOT.cget("bg"))
    
    
def notify_copy():
    """Notify user by flashing 'Copied' when they copy output"""
    global COPY_NOTICE
    COPY_NOTICE.config(bg="green", fg="white")
    ROOT.after(2000, hide_copy_notice) # after 2000 ms (2 seconds)


def copy_output(event):
    """Copies contents of OUT_FIELD widget to clipboard"""
    global OUT_FIELD
    pyperclip.copy(OUT_FIELD.get("1.0", END))
    notify_copy()
    




### Menubar logic ------------------------------------------------------

def open_about_window():
    about_window = Toplevel()
    about_window.title("no more underscore - About")
    about_window.geometry("420x200")
    about_info = Label(about_window, text=__doc__, pady=20, padx=20)
    about_info.pack()


def open_license_window():
    # Get license contents
    script_dir = os.path.dirname(os.path.abspath(__file__))
    license_path = os.path.join(script_dir, 'LICENSE')
    with open(license_path, 'r') as license_file:
        content = license_file.read()
        
    # Create license window base
    license_window = Toplevel()
    license_window.title("no more underscore - License")
    license_window.geometry("600x350")
    
    # Display license information
    license_label = Label(license_window, text=content, pady=20, padx=20)
    license_label.pack()
    




### GUI Structure ------------------------------------------------------

def create_menu_bar():
    global ROOT
    
    menu_bar = Menu(ROOT)
    menu_bar.add_cascade(label='About', command=open_about_window)
    menu_bar.add_cascade(label='License', command=open_license_window)
    
    return menu_bar


def create_header():
    global ROOT
    global COPY_NOTICE
    
    header = Frame(pady=5)
    header.columnconfigure(0, weight=1)
    header.columnconfigure(1, weight=1)
    header.columnconfigure(2, weight=1)
    header.columnconfigure(3, weight=1)
    
    Label(header, text='Select directory:').grid(row=0, column=0, sticky=W)
    
    select_button = Button(header, text='Select', command=run)
    select_button.grid(row=0, column=1, sticky=W, padx=20)
    
    COPY_NOTICE = Label(header, text='Copied', width=10, 
                        bg=ROOT.cget("bg"), fg=ROOT.cget("bg"))
    COPY_NOTICE.grid(row=0, column=2, sticky=E, padx=20, columnspan=2)
    
    return header


def create_output_field():
    output_field = scrolledtext.ScrolledText(ROOT, width=50, height=25, cursor="hand2")
    output_field.bind("<Button-1>", copy_output)
    output_field.bind("<Button-3>", copy_output)
    output_field.configure(state="disabled")
    return output_field


def create_main_window():
    global ROOT
    global OUT_FIELD
    global DIR_LABEL
    
    # Create root window
    ROOT = Tk()
    ROOT.title("no more underscore")
    ROOT.geometry('500x500') # width x height of root window
    ROOT.columnconfigure(0, weight=1)
    ROOT.rowconfigure(0, weight=1, pad=1)
    ROOT.rowconfigure(1, weight=1, pad=1)
    ROOT.rowconfigure(2, weight=1, pad=1)
    
    # Create menu bar
    menu_bar = create_menu_bar()
    ROOT.config(menu=menu_bar)    
    
    # Create header section
    header = create_header()
    header.grid(row=0, column=0)
    
    # Create output section
    OUT_FIELD = create_output_field()
    OUT_FIELD.grid(row=1, column=0)
    
    # Create directory label
    DIR_LABEL = Label(ROOT, text='Selected directory will appear here')    
    DIR_LABEL.grid(row=2, column=0)
        
    ROOT.mainloop()






### Main loop ----------------------------------------------------------

if __name__ == "__main__":
    create_main_window()