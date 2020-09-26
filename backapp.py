#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import filedialog


""" To access to backup files
from the main file time-track.py
with a GUI textbox
"""
def backupFuncPatient(self):
    self.fen=Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='cyan')
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files1",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox=Text(self.fen, height=30, width=60, font=18, relief=SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("+ Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(END, li)
    except FileNotFoundError as error_file:
        print("+ File not found !", error_file)
    except TypeError as type_err:
        print("+ Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
            print("+ Unbound Local Error", unb_err)

def backupFuncPatient2(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files2",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    #self.label.withdraw()
    try:
        if not filepath:
            self.label.destroy()
    except Exception as ex_file:
        print("+ Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.read()
    except FileNotFoundError as error_file:
        print("+ File not found !", error_file)
    except TypeError as type_err:
        print("+ Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
            print("+ Unbound Local Error", unb_err)

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

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

def backupFuncPatient11(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files11",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient12(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files12",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient13(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files13",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient14(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files14",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient15(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files15",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient16(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files16",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient17(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files17",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient18(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files18",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient19(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files19",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient20(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files20",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient21(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files21",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient22(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files22",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient23(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files23",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

def backupFuncPatient24(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files24",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)
    with open(filepath, 'r') as fichier:
        content = fichier.read()

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)
