""" NO MORE UNDERSCORE

Generate a copyable list of all filenames from a user-specified 
directory with the filetype extension removed and all underscores replaced
with a space.

e.g., 2025_bound.pdf will be printed as 2025 bound

e.g., 1987_dwyer_et_al_meaning_of_pluto.docx will be printed as 
   1987 dwyer et al meaning of pluto
   
"""


### Imports --------------------------------------------------------------

from tkinter import Tk
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import Text
from tkinter import Frame
from tkinter import E
from tkinter import W
from tkinter import scrolledtext


### Global variables --------------------------------------------------------

ROOT = None
OUT_FIELD = None
DIR_LABEL = None




### GUI Logic ---------------------------------------------------------------






### GUI Structure -----------------------------------------------------------

def create_menu_bar():
    global ROOT
    menu_bar = Menu(ROOT)
    menu_bar.add_cascade(label='About', command=None)
    menu_bar.add_cascade(label='License', command=None) # COMMAND TO DO   
    return menu_bar

def create_header():
    global ROOT
    header = Frame()
    Label(header, text='Select directory:').grid(row=0, column=0, sticky=W)
    Button(header, text='Select', command=None).grid(row=0, column=1, sticky=E, padx=20)
    return header

def create_main_window():
    # Create root window
    global ROOT
    ROOT = Tk()
    ROOT.title("no more underscore")
    ROOT.geometry('500x500') # width x height of root window
    
    # Create menu bar
    menu_bar = create_menu_bar()
    ROOT.config(menu=menu_bar)
    
    # Configure column and row widths
    ROOT.columnconfigure(0, weight=1)
    ROOT.rowconfigure(0, weight=1, pad=1)
    ROOT.rowconfigure(1, weight=1, pad=1)
    ROOT.rowconfigure(2, weight=1, pad=1)
    
    # Create header section
    header = create_header()
    header.grid(row=0, column=0)
    
    # Create output section
    OUT_FIELD = scrolledtext.ScrolledText(ROOT, width=50, height=25)
    DIR_LABEL = Label(ROOT, text='This is the directory label')
    OUT_FIELD.grid(row=1, column=0)
    DIR_LABEL.grid(row=2, column=0)
        
    ROOT.mainloop()


### Main loop ---------------------------------------------------------------

if __name__ == "__main__":
    create_main_window()