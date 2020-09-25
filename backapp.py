#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import filedialog


# Backup files
def backupFuncPatient(self):
    self.label=Tk()
    self.label.title("Search File")
    filepath = filedialog.askopenfilename(initialdir = "./Backup/Files1",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    try:
        with open(filepath, 'r') as fichier:
            fichier.read()
    except FileNotFoundError as error_path:
        print("+ The file does not exist !", error_path)
    except UnboundLocalError as error_unbound:
        print("+ Local variable !", error_unbound)

    self.label=Label(self.label, justify=LEFT, font=('Times 14'),
        bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

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
