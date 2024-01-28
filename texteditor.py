from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox as mb 
from PIL import Image, ImageTk 
import os



def open_file():
   file=fd.askopenfilename(defaultextension='.text', filetypes=[('All Files','*.*'),
                                                                        ("Text File",".txt")])
   
   if file !='':
       root.title(f"{os.path.basename(file)}")
       text_area.delete(1.0, END)
       with open(file, "r") as file_:
           text_area.insert(1.0, file_.read())
           file_.close()

   else:
       file=None

def open_new_file():
    root.title("Untitled - Text Editor")
    text_area.delete(1.0, END)


def save_file():
   global text_area
   file = fd.asksaveasfile(initialfile='Untitled.txt', defaultextension='.txt',
                                   filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
   if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
   text2save = str(text_area.get(1.0, END)) 
   file.write(text2save)
   file.close()
   root.title(f"{file}")

def exit_application():
     root.destroy()

def copy_text():
    text_area.event_generate("<<Copy>>")

def cut_text():
    text_area.event_generate("<<Cut>>")

def paste_text():
     text_area.event_generate("<<Paste>>")


def about_editor():
     mb.showinfo("About Text Editor", "This is a simple text editor created using python.")


    
     
root=Tk()
root.title("Untitled - Text Editor")
root.geometry("800x500")
root.resizable(0,0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

icon=ImageTk.PhotoImage(Image.open('noteIcon.png'))
root.iconphoto(False,icon)


menu_bar =Menu(root)

file_menu=Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

file_menu.add_command(label="New", command=open_new_file)
file_menu.add_command(label="Open File",command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File",command=exit_application)

menu_bar.add_cascade(label="File",menu=file_menu)


edit_menu=Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
edit_menu.add_command(label="Copy",command=copy_text)
edit_menu.add_command(label="Cut",command=cut_text)
edit_menu.add_command(label="Paste",command=paste_text)
edit_menu.add_separator()
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu=Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
help_menu.add_command(label="About Text Editor", command=about_editor)


menu_bar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu_bar)


text_area=Text(root,font=("Times New Roman", 12))
text_area.grid(sticky=NSEW)

scroller=Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT,fill=Y)

scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)



root.update()
root.mainloop()