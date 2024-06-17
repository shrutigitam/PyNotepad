from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile(event=""):
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile(event=""):
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            print("File Saved")
    else:
        #save the file
        f= open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Shruti")

if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - My Notepad")
    icon_path = "1.ico"
    root.bind("<Control-o>", openFile)
    root.bind("<Control-O>", openFile)
    root.bind("<Control-n>", newFile)
    root.bind("<Control-N>", newFile)

    root.geometry("400x500")

    #Add TextArea
    TextArea = Text(root, font="Lucida 13", padx=10, pady=10, wrap=WORD, selectbackground="orange", bd=2, insertwidth=3)
    file = None
    TextArea.pack(fill=BOTH, expand=TRUE)

    #Lets create a menubar
    MenuBar = Menu(root)

    #File menu Sart
    FileMenu = Menu(MenuBar, tearoff=0)

    #To open new file
    FileMenu.add_command(label="New", accelerator="Ctrl+n", command=newFile)

    #To open already existing file
    FileMenu.add_command(label="Open", accelerator="Ctrl+o",command = openFile)
    FileMenu.add_separator()
    #To save the current File
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    #File menu end

    #Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)

    #To give a feature of cut,copy,paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label = "Edit", menu = EditMenu)

    #Edit menu ends

    #help menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command= about)
    MenuBar.add_cascade(label = "Help", menu=HelpMenu)
    #help menu ends

    root.config(menu = MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()

