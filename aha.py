import turtle
from turtle import Screen
from tkinter import *

import pyttsx3
engine = pyttsx3.init()
f=1


from tkinter.ttk import *
 
master = Tk()
master.geometry("200x200") 

def ach():
    li=[]
    oi=[]
    no=int(input("enter no. of elements"))
    for i in range (0,no):
        k=int(input("Enter next element :"))
        li.append(k)
        oi.append(k)

    ar = turtle.Turtle()
    screen = turtle.Screen()

    ar.hideturtle()
    def kuch():
        ar.clear()
        ar.penup()
        ar.goto(-400,-130)
        ar.pendown()
        ar.write("Sorting is the process of arranging data into ",font=('Times New Roman',12))
        ar.penup()
        ar.goto(-400,-150)
        ar.pendown()
        ar.write("meaningful order(ascending or descending order) so that you can analyze it more effectively.",font=('Times New Roman',12))
        
    def arr():
        ar.clear()
        ar.penup()
        ar.goto(-400,-130)
        ar.pendown()
        ar.write("An array is a group of related data items which share’s a common name.",font=('Times New Roman',12))
        ar.penup()
        ar.goto(-400,-150)
        ar.pendown()
        ar.write("A particular value in an array is identified with the help of its index number",font=('Times New Roman',12))
    def ye(): 
        ar.clear()
        ar.penup()
        ar.goto(-400,-130)
        ar.pendown()
        ar.write("There are numerous types of sorting in data structures some of which are -",font=('Times New Roman',12))
        ar.penup()
        ar.goto(-400,-150)
        ar.pendown()
        ar.write("bubble sort, insertion sort, selection sort, quick sort, merge sort, heap sort, radix sort, bucket sort etc.",font=('Times New Roman',12))

    def hgh(): 
        ar.clear()
        ar.penup()
        ar.goto(-400,-130)
        ar.pendown()
        ar.write("Bubble Sort is the simplest sorting algorithm that works by ",font=('Times New Roman',12))
        ar.penup()
        ar.goto(-400,-150)
        ar.pendown()
        ar.write("repeatedly swapping the adjacent elements if they are in the wrong order.",font=('Times New Roman',12))


        
    canvas = screen.getcanvas()
    button = Button(canvas.master, text="what is an array: ", command=arr)
    button.pack()
    button.place(x=100,y=130)

    canvas = screen.getcanvas()
    button = Button(canvas.master, text="what is sorting : ", command=kuch)
    button.pack()
    button.place(x=100,y=100)

    canvas = screen.getcanvas()
    button = Button(canvas.master, text="Types of sorting ", command=ye)
    button.pack()
    button.place(x=100,y=160)

    canvas = screen.getcanvas()
    button = Button(canvas.master, text="What is Bubble sorting ", command=hgh)
    button.pack()
    button.place(x=100,y=190)


                

    def doing(s,b,oi):
            for u in range(0,no):
                    li[u]=oi[u]
            t.clear()
            t.speed(0)
            t.penup()
            t.pencolor('black')
            
            t.goto(-50,100)
            t.write("Sort Array stimulator",align="Center",font=('Times New Roman',14,'bold'))  
            t.pendown()

            g=-100
            h=-40
                
            b=-150
            t.penup()
            t.goto(200,260)
            t.pendown()
            
            t.pencolor('blue')
            t.write("Start inserting elements into an array",font=('Times New Roman',12,'bold'))
            t.pencolor('black')
            for i in range(0,a):
                t.penup()
                t.goto(b,0)
                t.pendown()

                for j in range(4):
                    t.left(90)
                    t.forward(50)

                b=b+50
            
                t.write(li[i],align="right")
                m=str(li[i])
                c=str(i)
                t.penup()
                t.goto(g,h)
                t.pendown()
                t.write(m+" is inserted at index "+c,font=('Times New Roman',12,'bold'))
                h=h-20
            d=-150
        
            
            t.penup()
            t.goto(200,240)
            t.pendown()
            t.pencolor('blue')
            t.write("first loop :sort starts with very first two elements",font=('Times New Roman',12,'bold'))
            t.penup()
            t.goto(200,220)
            t.pendown()
            t.write(" comparing them to check which one is greater.",font=('Times New Roman',12,'bold'))
            t.pencolor('black')
            t.penup()
            t.goto(200,160)
            q=200
            t.pendown()
            
            for i in range(0,a-1):
                if(i<(s+1)):
                    t.speed(0)
                else:
                    t.speed(1)
                for j in range(i+1,a):
                        t.penup()
                        t.goto(200,q)
                        t.pendown()
                        t.write("compairing two values if "+ str(li[i])+ " is greater than "+ str(li[j]) +" then swap" ,font=('Times New Roman',10))
                        q=q-12
                        t.penup()
                        if(li[i]>li[j]):
                                
                                
                                t.penup()
                                t.goto(200,q)
                                t.pendown()
                                t.pencolor('green')
                                t.write("swapping two values "+ str(li[i])+" and "+ str(li[j]),font=('Times New Roman',10))
                                t.pencolor('black')
                                q=q-12
                                t.penup()
                                t.goto(d+(i*50),0)
                                t.pendown()
                                t.pencolor('white')
                                t.write(li[i],align="right")
                                t.penup()
                                t.goto(d+(j*50),0)
                                t.pendown()
                                t.write(li[j],align="right")
                                temp=li[i]
                                li[i]=li[j]
                                li[j]=temp
                                t.pencolor('black')
                                t.penup()
                                t.goto(d+(i*50),0)
                                t.pendown()
                                t.write(li[i],align="right")
                                t.penup()
                                t.goto(d+(j*50),0)
                                t.pendown()
                                t.write(li[j],align="right")
                        else:
                            t.penup()
                            t.goto(200,q)
                            t.pendown()
                            t.pencolor('red')
                            t.write("No need to swap "+ str(li[i])+" and "+ str(li[j]),font=('Times New Roman',10))
                            t.pencolor('black')
                            q=q-12
                            t.penup()
                q=q-20
                t.penup()
                t.goto(200,q)
                t.pendown()
                
                q=q-22
                t.penup()


            t.penup()
            t.goto(200,q)
            t.pendown()
            t.write("Array is sorted")
            q=q-10
            
            t.penup()
            screen.exitonclick() 

         
    def acha(b,i,oi):
        a=880
        canvas = screen.getcanvas()
        button = Button(canvas.master, text=" NEXT LOOP STARTS : ", command=lambda: doing(i,b,oi))
        button.pack()
        button.place(x=a,y=b)
        
        
        
        return b,i






    if(no>8):
            win_width, win_height = 2000, 2000
    else:
            win_width, win_height = 700, 650

    turtle.setup()
    turtle.screensize(win_width, win_height)

    t = turtle.Turtle()



    screen = turtle.Screen()

    t.penup()
    t.pencolor('black')
    t.speed(2)
    t.goto(-50,100)
    t.write("Sort Array stimulator",align="Center",font=('Times New Roman',14,'bold'))  
    t.pendown()

    def do_something():
            
            global f
            f=0
    canvas = screen.getcanvas()
    button = Button(canvas.master, text="MUTE", command=do_something)
    button.pack()
    button.place(x=500, y=150)  


    g=-100
    h=-40
                
    b=-150
    t.penup()
    t.goto(200,260)
    t.pendown()
            
    t.pencolor('blue')
    t.write("Start inserting elements into an array",font=('Times New Roman',12,'bold'))
    t.pencolor('black')

    t.penup()
    t.goto(200,240)
    t.pendown()
    t.pencolor('blue')
    t.write("first loop :sort starts with very first two elements",font=('Times New Roman',12,'bold'))
    t.pencolor('black')
    t.penup()

    for i in range(0,no):
                t.penup()
                t.goto(b,0)
                t.pendown()

                for j in range(4):
                    t.left(90)
                    t.forward(50)

                b=b+50
            
                t.write(li[i],align="right")
                m=str(li[i])
                c=str(i)
                if(f==1):
                    engine.say(m+" is inserted at index "+c)
                    engine.runAndWait()
                else:
                    
                    t.penup()
                    t.goto(g,h)
                    t.pendown()
                    t.write(m+" is inserted at index "+c,font=('Times New Roman',12,'bold'))
                    h=h-20
                d=-150

    q=200
    a=no
    b=125
    for i in range(0,a-1):
            
                for j in range(i+1,a):
                        t.penup()
                        t.goto(200,q)
                        t.pendown()
                        t.write("compairing two values if "+ str(li[i])+ " is greater than "+ str(li[j]) +" then swap" ,font=('Times New Roman',10))
                        q=q-12
                        b=b+12
                        t.penup()
                        if(li[i]>li[j]):
                                
                                
                                t.penup()
                                t.goto(200,q)
                                t.pendown()
                                t.pencolor('green')
                                t.write("swapping two values "+ str(li[i])+" and "+ str(li[j]),font=('Times New Roman',10))
                                t.pencolor('black')
                                q=q-12
                                b=b+13
                                t.penup()
                                t.goto(d+(i*50),0)
                                t.pendown()
                                t.pencolor('white')
                                t.write(li[i],align="right")
                                t.penup()
                                t.goto(d+(j*50),0)
                                t.pendown()
                                t.write(li[j],align="right")
                                temp=li[i]
                                li[i]=li[j]
                                li[j]=temp
                                t.pencolor('black')
                                t.penup()
                                t.goto(d+(i*50),0)
                                t.pendown()
                                t.write(li[i],align="right")
                                t.penup()
                                t.goto(d+(j*50),0)
                                t.pendown()
                                t.write(li[j],align="right")
                        else:
                            t.penup()
                            t.goto(200,q)
                            t.pendown()
                            t.pencolor('red')
                            t.write("No need to swap "+ str(li[i])+" and "+ str(li[j]),font=('Times New Roman',10))
                            t.pencolor('black')
                            q=q-12
                            b=b+13
                            t.penup()
                q=q-20
                b=b+18
                t.penup()
                t.goto(200,q)
                t.pendown()
                t.pencolor('blue')
                
                
                b,i=acha(b,i,oi)
                b=b+20
                t.pencolor('black')
                q=q-22
                t.penup()


    t.penup()
    t.goto(200,q)
    t.pendown()
    t.write("Array is sorted")
    q=q-10

    screen.exitonclick()

 
def openNewWindow():
   
    newWindow = Toplevel(master)
    newWindow.title("New Window") 
    newWindow.geometry("200x200")
    Label(newWindow,text ="Choose the operation to be performed").pack()
    btn = Button(newWindow,text ="Click for SORT Array tutorial ",command = ach)
    btn.pack(pady = 10)
     
 
label = Label(master,text ="DATA STRUCTURE ALGORITHM")
label.pack(pady = 10)
btn = Button(master,text ="ARRAY OPERATIONS",command = openNewWindow)
btn.pack(pady = 10)
btn = Button(master,text ="LINKED LIST OPERATIONS",command = openNewWindow)
btn.pack(pady = 10)
btn = Button(master,text ="STACK & QUEUE OPERATIONS",command = openNewWindow)
btn.pack(pady = 10)
btn = Button(master,text ="GRAPH & TREE OPERATIONS",command = openNewWindow)
btn.pack(pady = 10)


mainloop()
