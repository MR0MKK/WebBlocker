#import library
#importing tkinter volume which will allow us to create a GUI


from tkinter import *

#initialize window
#creating the main window 


root = Tk()

root.geometry('500x300')

root.resizable(0,0)

root.title("Group 185 Project Exhibition - Website Blocker And Unblocker")

#heading
#creating the heading for the GUI

Label(root, text = 'Disable Website' , font = 'Algerian 22 bold').pack()

#creating the bottom text for the group name

Label(root,text = 'Group 185' , font = 'Algerian 20 bold').pack(side = BOTTOM)

#path of our host file and ip address 
#entering the links into the host will block the website from the system
#local ip address should be added before the link to make the change effective


host_path = 'C:\Windows\System32\drivers\etc\hosts'

ip_address = '127.0.0.1'

#ENTER WEBSITE
#Takes input from the user, i.e it takes the links which we have to block


Label(root, text= 'ENTER WEBSITE:', font = 'arial 14 bold').place(x=5,y=60)

Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 5, pady=5)

Websites.place(x = 180, y =60)



#block function
#the main function which will get the link entered in the GUI and put it in the host file which will block the link

def Blocker():

    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.read()

        for website in Website:

            if website in file_content:

                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass

            else:

                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)




#Unblock function
#the main function which will get the link entered in the GUI and remove it from the host file which will unblock the link

def Unblock():

    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.readlines()
        
        host_file.seek(0)
        
        
        for line in file_content:

            if not any(site in line for site in Website):
                
                host_file.write(line)
                
                Label(root, text = "UnBlocked", font = 'arial 12 bold').place(x=350,y =200)
        
        host_file.truncate()







#creating the block button in the GUI

block_btn = Button(root, text = 'BLOCK' , font = 'arial 13 bold', command = Blocker , height = 2, width = 8, bg = 'red', activebackground = 'black')

#positioning the button on the GUI 

block_btn.place(x = 200, y =140)


        
#creating the unblock button in the GUI

unblock_button = Button(root, text = 'UNBLOCK',font = 'arial 13 bold',command = Unblock , height = 2, width = 10, bg = 'GREEN', activebackground = 'black')


#positioning the button on the GUI

unblock_button.place(x = 350, y = 140)

root.mainloop
    
    
