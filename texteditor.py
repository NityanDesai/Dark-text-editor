from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Menu Functions
def newFile():
    global file
    root.title('Untitled - Basic Text editor')
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', "*.*"), ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + " - Basic Text Editor")
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[('All Files', "*.*"), ('Text Documents', '*.txt')])
        if file == '':
            file = None
        else:
            f = open(file, 'w')  # Save as a new file
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Basic Text Editor")
            print('Saved')
    else:
        f = open(file, 'w')  # Save the file
        f.write(TextArea.get(1.0, END))
        f.close()
def copyFile():
    TextArea.event_generate('<<Copy>>')
def cutFile():
    TextArea.event_generate('<<Cut>>')
def pasteFile():
    TextArea.event_generate('<<Paste>>')
def about():
    tmsg.showinfo('About BTE!!', "Created By Nityan Desai.\nIf you're thinking what is BTE?: It's 'Basic Text Editor'. Now, what is text Editor??🙄 Come on man! This is 2020, you should know what a text editor is. It's notepad kinda thing man, can't you see?! Why are you still reading this, are you crazy, dude? Seriously, are you still reading?? Go home kiddo, there's nothing here, I am just playing with you, Now I don't even wanna write somthing, I'm out!! Bcoz you're not going anywhere, you're still reading!!🤦‍♂️🤢")

if __name__ == '__main__':
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.title('Untitled - Basic Text editor')
    root.wm_iconbitmap('2.ico')
    root.configure(background='grey30')

    # Add Text Area
    TextArea = Text(root, insertbackground='white', font='courier 13', bg='grey15', fg='white')
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    # File menu starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # New file
    FileMenu.add_command(label='New', command=newFile)
    # Open already existing file
    FileMenu.add_command(label='Open', command=openFile)
    # To save current file
    FileMenu.add_command(label='Save', command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quit)
    MenuBar.add_cascade(label='File', menu=FileMenu)
    # File menu ends

    # Edit menu starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # Copy, cut, paste
    EditMenu.add_command(label='Copy', command=copyFile)
    EditMenu.add_command(label='Cut', command=cutFile)
    EditMenu.add_command(label='Paste', command=pasteFile)
    MenuBar.add_cascade(label='Edit', menu=EditMenu)
    # Edit menu ends

    # Help menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    # About
    HelpMenu.add_command(label='About BTE', command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)
    # Help menu ends

    root.config(menu=MenuBar)

    # Scrollbar
    sb = Scrollbar(TextArea)
    sb.pack(side=RIGHT, fill=Y)
    sb.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=sb.set)

    root.mainloop()