#Server Part


########### Import Part ###########

from Tkinter import *
from threading import Thread
import time
from socket import *

###################################

########### GUI PART ##############

def windows():

    bgcolor = "#4d2177"

    #Window Part
    global window
    window = Tk()
    window.title("Server")
    window.minsize(width=500, height=600)
    window.maxsize(width=500, height=600)

    # Frame Part
    global frame
    frame = Frame(window, width=500, height=600, bg=bgcolor)
    frame.pack()

    #Text Area Part
    global textarea
    textarea_label = Label(frame, bg=bgcolor, fg="white", text="[ Server ]", font=("Helvetica 15 bold"))
    textarea_label.place(x=200, y=20)

    textarea = Text(frame, font=("Helvetica", 13))
    textarea.place(x=20, y=60, height=410, width=455)
    scrollbar = Scrollbar(window, command=textarea.yview)  
    textarea['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=462, y=60, height=410)
    textarea.insert(END, "\n" + "Server started..." + "\n")

###################################


######## Programming Part #########

sock1 = socket(AF_INET, SOCK_STREAM)
sock2 = socket(AF_INET, SOCK_STREAM)
sock3 = socket(AF_INET, SOCK_STREAM)

host = gethostname()
port1 = 5001
port2 = 5002
port3 = 5003
connection1 = ''
connection2 = ''
connection3 = ''
sock1.bind((host, port1))
sock2.bind((host, port2))
sock3.bind((host, port3))


client1_ConnectionStatus=0
client2_ConnectionStatus=0
client3_ConnectionStatus=0

client1_arrived=0
client2_arrived=0
client3_arrived=0


print "Server started..."

def Client1():
    sock1.listen(1)
    global client1_ConnectionStatus
    global client2_ConnectionStatus
    global client3_ConnectionStatus
    global client1_arrived

    global connection1
    connection1, address1 = sock1.accept()
    print "Connected With " + str(address1)
    client1_ConnectionStatus = 1
    client1_arrived=1
    textarea.insert(END, "\n" + "-> Connected With " + str(address1) + "\n")

    while True:

        data1 = connection1.recv(4096)

        if data1 == "Zahid Disconnected":
            client1_ConnectionStatus = 0
            if client2_ConnectionStatus == 1:
                connection2.sendall("Zahid Disconnected")
            if client3_ConnectionStatus == 1:
                connection3.sendall("Zahid Disconnected")
            connection1.close()
            t1.stop()
            break
        else:
            data1 = "Zahid: " + data1

            if client2_ConnectionStatus == 1:
                connection2.sendall(data1)
            if client3_ConnectionStatus == 1:
                connection3.sendall(data1)
            # print data1
            textarea.configure(state='normal')
            textarea.insert(END, "\n" + data1)
            textarea.configure(state='disabled')
            sock1.close()
            time.sleep(.5)

        

def Client2():
    sock2.listen(1)
    global connection2
    global client1_ConnectionStatus
    global client2_ConnectionStatus
    global client3_ConnectionStatus
    global client2_arrived

    connection2, address2 = sock2.accept()
    print "Connected With " + str(address2)
    client2_ConnectionStatus = 1
    textarea.insert(END, "\n" + "-> Connected With " + str(address2) + "\n")

    client2_arrived = 1

    while True:
        data2 = connection2.recv(4096)

        if data2 == "Saif Disconnected":
            client2_ConnectionStatus = 0
            if client1_ConnectionStatus == 1:
                connection1.sendall("Saif Disconnected")
            if client3_ConnectionStatus == 1:
                connection3.sendall("Saif Disconnected")
            connection2.close()
            t2.stop()
            break
        else:
            data2 = "Saif: " + data2

            if client1_ConnectionStatus == 1:
                connection1.sendall(data2)
            if client3_ConnectionStatus == 1:
                connection3.sendall(data2)
            print data2
            textarea.configure(state='normal')
            textarea.insert(END, "\n" + data2)
            textarea.configure(state='disabled')
            sock2.close()
            time.sleep(.5)


        

def Client3():
    sock3.listen(1)
    global connection3

    global client1_ConnectionStatus
    global client2_ConnectionStatus
    global client3_ConnectionStatus
    global client3_arrived

    connection3, address3 = sock3.accept()
    print "Connected With " + str(address3)
    client3_ConnectionStatus = 1
    textarea.insert(END, "\n" + "-> Connected With " + str(address3) + "\n")

    client3_arrived = 1

    while True:
        data3 = connection3.recv(4096)

        if data3 == "Saimoon Disconnected":
            client3_ConnectionStatus = 0
            if client1_ConnectionStatus == 1:
                connection1.sendall("Saimoon Disconnected")
            if client2_ConnectionStatus == 1:
                connection2.sendall("Saimoon Disconnected")
            connection3.close()
            t3.stop()
            break
        else:
            data3 = "Saimoon: " + data3

            if client1_ConnectionStatus == 1:
                connection1.sendall(data3)
            if client2_ConnectionStatus == 1:
                connection2.sendall(data3)
            print data3
            textarea.configure(state='normal')
            textarea.insert(END, "\n" + data3)
            textarea.configure(state='disabled')
            sock3.close()
            time.sleep(.5)



def check():
    global client1_ConnectionStatus
    global client2_ConnectionStatus
    global client3_ConnectionStatus

    global connection1
    global connection2
    global connection3
    
    global client1_arrived
    global client2_arrived
    global client3_arrived

    while True:
        #Zahid is Online
        if client1_ConnectionStatus == 1:
            if client2_arrived == 1:
                connection1.sendall("Saif is Online")
            if client3_arrived == 1:
                connection1.sendall("Saimoon is Online")

        #Saif is Online
        if client2_ConnectionStatus == 1:
            if client1_arrived == 1:
                connection2.sendall("Zahid is Online")
            if client3_arrived == 1:
                connection2.sendall("Saimoon is Online")
        
        #Saimoon is Online
        if client3_ConnectionStatus == 1:
            if client1_arrived == 1:
                connection3.sendall("Zahid is Online")
            if client2_arrived == 1:
                connection3.sendall("Saif is Online")



        #Zahid
        if client1_arrived == 1:
            client1_arrived = 0
            if client2_ConnectionStatus == 1:
                connection1.sendall("Saif is Online")

            if client3_ConnectionStatus == 1:
                connection1.sendall("Saimoon is Online")
        #Saif
        if client2_arrived == 1:
            client2_arrived = 0
            if client1_ConnectionStatus == 1:
                connection2.sendall("Zahid is Online")
            if client3_ConnectionStatus == 1:
                connection2.sendall("Saimoon is Online")
        #Saimoon
        if client3_arrived == 1:
            client3_arrived = 0
            if client1_ConnectionStatus == 1:
                connection3.sendall("Zahid is Online")
            if client2_ConnectionStatus == 1:
                connection3.sendall("Saif is Online")

        time.sleep(.5)

###################################

####### Functions & Threads ########

windows()
t1 = Thread(target=Client1)
t2 = Thread(target=Client2)
t3 = Thread(target=Client3)
t4 = Thread(target=check)

t1.start()
t2.start()
t3.start()
t4.start()


window.mainloop()

###################################
