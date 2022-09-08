import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))



class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")
        
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=400)

        self.text=Label(self.login,text="Please Login To Continue",justify=CENTER,font="Helvetica 14 bold")
        self.text.place(relheight=0.15,relx=0.2,rely=0.07)

        self.labelName=Label(self.login,text="Name",font="Helvetica 14 bold")
        self.labelName.place(relheight=0.1,relx=0.1,rely=0.2)

        self.entrybox=Entry(self.login,font="Helvetica 14 bold")
        self.entrybox.place(relwidth=0.5,relheight=0.10,relx=0.35,rely=0.2)

        self.entrybox.focus()
        self.gobutton = Button(self.login,text="CONTINUE",font="Helvetica 14 bold",command=lambda:self.goAhead(self.entrybox.get()))
        self.gobutton.place(relx=0.4,rely=0.5)

        self.window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rev=Thread(target=self.receive)
        rev.start() 

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break

g=GUI()

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()
