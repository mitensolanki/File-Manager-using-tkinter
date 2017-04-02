from tkinter import *
import shutil         
import os

#   FUNCTIONS

def open_file():
    global e1
    string = e1.get()
    try:
        os.startfile(string)
    except:
        print('File not found')   
    
def open_window():
    global e1
    read = Tk()
    Label(read, text="Enter File Location").grid(row = 1, column = 1)
    e1 = Entry(read)
    e1.grid(row  = 5, column = 1)  
    Button(read, text='Go', command=open_file).grid(row=7, column=1)
    read.mainloop()

def copy_file():
    global source
    global destination
    source1 = source.get()
    destination1 = destination.get()
    shutil.copy(source1,destination1)
    
def copy_window():   
    global source
    global destination
    copy = Tk()
    Label(copy, text = "Enter the Source Location").grid(row = 1, column = 1)
    Label(copy, text = "Enter the destination Location").grid(row = 4, column = 1)
    source = Entry(copy)
    source.grid(row = 1, column = 14)
    destination = Entry(copy)
    destination.grid(row = 4, column = 14)
    Button(copy, text = 'Go', command = copy_file).grid(row = 7, column = 2)
    copy.mainloop()

def delete_file():
    global deletefile
    string = deletefile.get()
    if os.path.exists(string):
        os.remove(string)             
    else:
        print('File not found')

def delete_window():
    global deletefile
    delete = Tk()
    Label(delete, text = "Enter the file Location").grid(row = 1, column = 1)
    deletefile = Entry(delete)
    deletefile.grid(row = 5, column = 1)
    Button(delete, text = 'Go', command = delete_file).grid(row = 7, column = 1)
    delete.mainloop()

def list_file():
    global listfile
    string = listfile.get()
    sortlist=sorted(os.listdir(string))       
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1
    
def list_window():
    global listfile
    listwindow = Tk()
    Label(listwindow, text = "Enter the file Location").grid(row = 1, column = 1)
    listfile = Entry(listwindow)
    listfile.grid(row = 5, column = 1)
    Button(listwindow, text = 'Go', command = list_file).grid(row = 7, column = 1)
    listwindow.mainloop()

def check_file():
    global checkfile
    string = checkfile.get()
    if os.path.isfile(string)==True:
        print('File Found')
    else:
        print('File not Found')

def check_window():
    global checkfile
    checkwindow = Tk()
    Label(checkwindow, text = "Enter the file Location").grid(row = 1, column = 1)
    checkfile = Entry(checkwindow)
    checkfile.grid(row = 5, column = 1)
    Button(checkwindow, text = 'Go', command = check_file).grid(row = 7, column = 1)
    checkwindow.mainloop()

def rename_file():
    global path1
    global path2
    string1 = path1.get()
    string2 = path2.get()
    shutil.move(string1,string2)
    
def rename_window():
    global path1
    global path2
    rename = Tk()
    Label(rename, text = "Enter the Source Location").grid(row = 1, column = 1)
    Label(rename, text = "Enter the destination Location").grid(row = 4, column = 1)
    path1 = Entry(rename)
    path1.grid(row = 1, column = 14)
    path2 = Entry(rename)
    path2.grid(row = 4, column = 14)
    Button(rename, text = 'Go', command = rename_file).grid(row = 7, column = 2)
    rename.mainloop()

def check_folder():
    global checkfolder
    string = checkfolder.get()
    if os.path.isdir(string)==True:
        print('Folder Found')
    else:
        print('Folder Not Found')
        
def checkfolder_window():
    global checkfolder
    checkfolderwindow = Tk()
    Label(checkfolderwindow, text = "Enter the file Location").grid(row = 1, column = 1)
    checkfolder = Entry(checkfolderwindow)
    checkfolder.grid(row = 5, column = 1)
    Button(checkfolderwindow, text = 'Go', command = check_folder).grid(row = 7, column = 1)
    checkfolderwindow.mainloop()

def make_folder():
    global makefolder
    string = makefolder.get()
    os.makedirs(string)

def make_window():
    global makefolder
    makewindow = Tk()
    Label(makewindow, text = "Enter the file Location").grid(row = 1, column = 1)
    makefolder = Entry(makewindow)
    makefolder.grid(row = 5, column = 1)
    Button(makewindow, text = 'Go', command = make_folder).grid(row = 7, column = 1)
    makewindow.mainloop()

def remove_folder():
    global removefolder
    string = removefolder.get()
    os.rmdir(string)

def remove_window():
    global removefolder
    removewindow = Tk()
    Label(removewindow, text = "Enter the file Location").grid(row = 1, column = 1)
    removefolder = Entry(removewindow)
    removefolder.grid(row = 5, column = 1)
    Button(removewindow, text = 'Go', command = remove_folder).grid(row = 7, column = 1)
    removewindow.mainloop()

#Tkinter UI
    
root = Tk()

Label(root, text="File Manager").grid(row = 5, column = 2)

Button(root, text = "Open a File", command = open_window).grid(row=7, column =1)

Button(root, text = "Copy a File", command = copy_window).grid(row = 19, column = 13)

Button(root, text = "Delete a File", command = delete_window).grid(row = 25, column = 1)

Button(root, text = "List all Files in Directory", command = list_window).grid(row = 31,column = 1)

Button(root, text = "Check a File", command = check_window).grid(row = 13,column = 1)

Button(root, text = "Rename a File", command = rename_window).grid(row = 7, column = 13)

Button(root, text = "Check Folder", command = checkfolder_window).grid(row = 19,column = 1)

Button(root, text = "Move a File", command = rename_window).grid(row = 13, column =13)

Button(root, text = "Make a Folder", command = make_window).grid(row = 25, column = 13)

Button(root, text = "Remove a Folder", command = remove_window).grid(row = 31, column =13)

root.mainloop()
