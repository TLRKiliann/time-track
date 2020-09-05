#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import filedialog


# Backup
def backupFuncPatient(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files1",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    # I have to try with Text (else no scrollbar)
    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient2(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files2",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient3(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files3",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient4(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files4",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient5(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files5",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient6(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files6",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient7(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files7",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient8(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files8",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient9(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files9",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

# Backup
def backupFuncPatient10(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files10",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)