from tkinter import *
import time

space=""
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("MinhKingKong")
Label(root, text = 'Chặn Website' , font = 'Algerian 22 bold').pack()
Label(root,text = 'Nhóm XXX' , font = 'Algerian 20 bold').pack(side = BOTTOM)

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'


Label(root, text= 'ENTER WEBSITE:', font = 'arial 14 bold').place(x=5,y=60)
Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 5, pady=5)
Websites.place(x = 180, y =60)

   
def Blocker():
    Label(root, text = "         ", font = 'arial 12 bold').place(x=350,y =200)
    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.read()

        for website in Website:

            if website in file_content:
                Label(root, width=20).place(x=200,y =200)   
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)      
                pass

            else:
                Label(root, width=35).place(x=200,y =200)    
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=200,y =200)
def Unblock():

    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.readlines()
        
        host_file.seek(0)
        
        
        for line in file_content:

            if not any(site in line for site in Website):
                Label(root, width=20).place(x=200,y =200)   
                host_file.write(line)
                Label(root, text = "UnBlocked", font = 'arial 12 bold').place(x=350,y =200)
        host_file.truncate()
    

block_button = Button(root, text = 'BLOCK' , font = 'arial 13 bold', command = Blocker , height = 2, width = 8, bg = 'red', activebackground = 'black')
block_button.place(x = 200, y =140)


unblock_button = Button(root, text = 'UNBLOCK',font = 'arial 13 bold',command = Unblock , height = 2, width = 10, bg = 'GREEN', activebackground = 'black')
unblock_button.place(x = 350, y = 140)


root.mainloop()