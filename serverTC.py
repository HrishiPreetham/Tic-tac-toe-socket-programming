import socket
import threading
from tkinter import *
from tkinter import messagebox #message box displays pop-up message boxes to the users
window=Tk()
cell=' '
turn=True #server has to make the first move in the game

host='192.168.56.1' #IP address of the server 
port=65535 #port number of the server

conn,addr=None,None #used to store the client object and the address of the client respectively

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a socket(IPV4 and TCP socket)
sock.bind((host,port)) #binds the socket on the specified address and port number
sock.listen(1) #waits for a single connection and if it recieves additional connection requests,they have to wait

def create_thread(targett):
    thread=threading.Thread(target=targett)
    thread.daemon=True #the thread will run in the background and will not prevent the program from exiting even when the main thread has completed executing.
    thread.start() #start running the thread
    
def recieveData():
    global cell
    global turn
    while True:
        data,addr=conn.recvfrom(1024) #it makes use of the conn socket object to accept the data from the client side
        #1024 bytes of data is arriving at the client side
        data2=data.decode() #converts the recieved data from bytes to string
        dataa=data2.split('-')#converts the string into the list of strings(which are seperated by -)
        cell=dataa[0] #this is the cell that was clicked by the client
        update()
        if(dataa[1]=='YourTurn'):
            turn=True
            print("Server turn= ",str(turn))
    
def update():
            if cell=='A':
                clicked1()
            elif cell=='B':
                clicked2()
            elif cell=='C':
                clicked3()
            elif cell=='D':
                clicked4()
            elif cell=='E':
                clicked5()
            elif cell=='F':
                clicked6()
            elif cell=='G':
                clicked7()
            elif cell=='H':
                clicked8()
            elif cell=='I':
                clicked9()
            else:
                print("No matching character")
    

            
    
def waiting4connection():
        print("Thread created")
        global conn,addr #changes made to these variables must be reflected globally
        conn,addr=sock.accept() #accepts the client connection and assigns the socket abject and address to conn,addr respectively.
        print("Client is created")
        recieveData()
        
create_thread(waiting4connection)

window.title("Welcome Player1 to Tic-Tac-Toe game")
window.geometry("400x300")

lbl=Label(window,text='Tic-Tac-Toe',font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text='Player 1:X',font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text='Player 2:O',font=('Helvetica','10'))
lbl.grid(row=2,column=0)

def clicked1():
    global turn
    global cell
    if turn==True and btn1["text"]==" ":#server makes the move
        btn1["text"]="X"
        send_data='{}-{}'.format('A','YourTurn').encode() #assigns tthe name to the cell and indicates it's the client's turn
        conn.send(send_data) #the string encoded into bytes is sent to the client side
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn1["text"]==" " and cell=="A"): #client makes the move and this is displayed on the server side
        btn1["text"]="O"
        turn =True
        check()

def clicked2():
    global turn
    global cell
    if turn==True and btn2["text"]==" ":
        btn2["text"]="X"
        send_data='{}-{}'.format('B','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn2["text"]==" " and cell=="B"):
        btn2["text"]="O"
        turn =True
        check()

        
def clicked3():
    global turn
    global cell
    if turn==True and btn3["text"]==" ":
        btn3["text"]="X"
        send_data='{}-{}'.format('C','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn3["text"]==" " and cell=="C"):
        btn3["text"]="O"
        turn =True
        check()
        
def clicked4():
    global turn
    global cell
    if turn==True and btn4["text"]==" ":
        btn4["text"]="X"
        send_data='{}-{}'.format('D','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn4["text"]==" " and cell=="D"):
        btn4["text"]="O"
        turn =True
        check()
        
def clicked5():
    global turn
    global cell
    if turn==True and btn5["text"]==" ":
        btn5["text"]="X"
        send_data='{}-{}'.format('E','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn5["text"]==" " and cell=="E"):
        btn5["text"]="O"
        turn =True
        check()
        
def clicked6():
    global turn
    global cell
    if turn==True and btn6["text"]==" ":
        btn6["text"]="X"
        send_data='{}-{}'.format('F','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn6["text"]==" " and cell=="F"):
        btn6["text"]="O"
        turn =True
        check()
        
def clicked7():
    global turn
    global cell
    if turn==True and btn7["text"]==" ":
        btn7["text"]="X"
        send_data='{}-{}'.format('G','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn7["text"]==" " and cell=="G"):
        btn7["text"]="O"
        turn =True
        check()     
        
def clicked8():
    global turn
    global cell
    if turn==True and btn8["text"]==" ":
        btn8["text"]="X"
        send_data='{}-{}'.format('H','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn8["text"]==" " and cell=="H"):
        btn8["text"]="O"
        turn =True
        check()

def clicked9():
    global turn
    global cell
    if turn==True and btn9["text"]==" ":
        btn9["text"]="X"
        send_data='{}-{}'.format('I','YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn=False
        check()
    elif(turn==False and btn9["text"]==" " and cell=="I"):
        btn9["text"]="O"
        turn =True
        check()

flag=1
def check():
    global flag
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    flag=flag+1
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"])
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"])
    if flag==10:
        messagebox.showinfo("Tie","Match tied!!! Try again!!")
        window.destroy()

def win(player):
    ans="Game done "+player+" wins ";
    messagebox.showinfo("Congratulations",ans)
    window.destroy()

btn1=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked1)
btn1.grid(column=1,row=1)
btn2=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked2)
btn2.grid(column=2,row=1)
btn3=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked3)
btn3.grid(column=3,row=1)
btn4=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked4)
btn4.grid(column=1,row=2)
btn5=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked5)
btn5.grid(column=2,row=2)
btn6=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked6)
btn6.grid(column=3,row=2)
btn7=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked7)
btn7.grid(column=1,row=3)
btn8=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked8)
btn8.grid(column=2,row=3)
btn9=Button(window,text=" ",bg="white",fg="black",width=2,height=2,font=("Helvetica",'20'),command=clicked9)
btn9.grid(column=3,row=3)

window.mainloop()