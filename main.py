import tkinter

#Defining Window
root=tkinter.Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry("300x400")
root.resizable(0,0)

#Defining Colors and fonts
dark_green="#93af22"
light_green='#acc253'
white_green="#edefe0"
button_font=("Arial",18)
display_font=("Arial",30)

#Define Functions
def submit_number(number):
    '''Adding number or decimal to the display box'''
    display_box.insert(tkinter.END,number) #Adding the number to the end of the string

    #If decimal was pressed disable the decimal button
    if '.' in display_box.get():
        decimal_button.config(state='disable')

def operate(operator):
    '''Store the first number of expression and the operand to be used '''
    global first_number
    global operation

    operation=operator
    first_number=display_box.get()

    #Clearing the display box
    display_box.delete(0,tkinter.END)

    #Disable all operator buttons until equal or clear is pressed
    add_button.config(state='disable')
    substract_button.config(state='disable')
    multiplication_button.config(state='disable')
    division_button.config(state='disable')
    inverse_button.config(state='disable')
    square_button.config(state='disable')
    exponent_button.config(state='disable')

    # Returning decimal button to normal state
    decimal_button.config(state='normal')

def equal():
    '''Run the stored operations for 2 numbers'''
    if operation=="add":
        value=float(first_number)+float(display_box.get())
    elif operation=="substract":
        value=float(first_number)-float(display_box.get())
    elif operation=='division':
        if display_box.get()==0:
            value="Error"
        else:
            value=float(first_number)/float(display_box.get())
    elif operation=="multiplication":
        value=float(first_number)*float(display_box.get())
    elif operation=="exponent":
        value=float(first_number)**float(display_box.get())

    #Display result
    #Remove current value
    display_box.delete(0,tkinter.END)
    display_box.insert(0,value)

    #Enabling the operators back
    enable()

    
def enable():
    add_button.config(state='normal')
    substract_button.config(state='normal')
    multiplication_button.config(state='normal')
    division_button.config(state='normal')
    inverse_button.config(state='normal')
    square_button.config(state='normal')
    exponent_button.config(state='normal')

def clear():
    '''clearing display'''
    display_box.delete(0,tkinter.END)
    
    #return button to normal state
    decimal_button.config(state='normal')
    enable()

def inverse():
    '''Calculate the inverse of the number'''
    #checking for 1/0
    if display_box.get()=='0':
        value="Error"
    else:
        value=1/float(display_box.get())
    display_box.delete(0,tkinter.END)
    display_box.insert(0,value)

def square():
    '''Calculate the square of a number'''
    value=float(display_box.get())**2
    display_box.delete(0,tkinter.END)
    display_box.insert(0,value) 

def negate():
    '''changing the sign of the button'''
    if display_box.get()=='0':
        value="Error"
    else:
        value= -1 * float(display_box.get())
    display_box.delete(0,tkinter.END)
    display_box.insert(0,value) 



#GUI layout
#Define frames
display_frame=tkinter.LabelFrame(root)
button_frame=tkinter.LabelFrame(root)
display_frame.pack(padx=2,pady=(5,20))
button_frame.pack(padx=2,pady=5)


#layout for widgets
display_box=tkinter.Entry(display_frame,width=50,font=display_font,bg=white_green,borderwidth=3,justify= tkinter.RIGHT, validatecommand= callable) #Justifying right for right alignment
display_box.pack(padx=5,pady=5)

#Layout for the button Frame
clear_button=tkinter.Button(button_frame,text="CLEAR",font=button_font,bg=dark_green,command=clear)
quit_button=tkinter.Button(button_frame,text="QUIT",font=button_font,bg=dark_green,command=root.destroy)

inverse_button=tkinter.Button(button_frame,text="1/x",font=button_font,bg=light_green,command=inverse)
square_button=tkinter.Button(button_frame,text="x^2",font=button_font,bg=light_green,command=square)
exponent_button=tkinter.Button(button_frame,text="x^n",font=button_font,bg=light_green, command=lambda: operate("exponent"))
division_button=tkinter.Button(button_frame,text=" / ",font=button_font,bg=light_green, command=lambda: operate("division"))
multiplication_button=tkinter.Button(button_frame,text="*",font=button_font,bg=light_green, command=lambda: operate("multiplication"))
substract_button=tkinter.Button(button_frame,text="-",font=button_font,bg=light_green, command=lambda: operate("substract"))
add_button=tkinter.Button(button_frame,text="+",font=button_font,bg=light_green, command=lambda: operate("add"))
equal_button=tkinter.Button(button_frame,text="=",font=button_font,bg=dark_green,command=equal)
decimal_button=tkinter.Button(button_frame,text=".",font=button_font,bg="black",fg="white",command= lambda: submit_number('.'))
#decimal_button.bind('<.>',submit_number('.'))
negate_button=tkinter.Button(button_frame,text="+/-",font=button_font,bg='black',fg='white',command=negate)

nine_button=tkinter.Button(button_frame,text='9',font=button_font,bg='black',fg='white',command= lambda: submit_number(9))
eight_button=tkinter.Button(button_frame,text='8',font=button_font,bg='black',fg='white',command= lambda: submit_number(8))
seven_button=tkinter.Button(button_frame,text='7',font=button_font,bg='black',fg='white',command= lambda: submit_number(7))
six_button=tkinter.Button(button_frame,text='6',font=button_font,bg='black',fg='white',command= lambda: submit_number(6))
five_button=tkinter.Button(button_frame,text='5',font=button_font,bg='black',fg='white',command= lambda: submit_number(5))
four_button=tkinter.Button(button_frame,text='4',font=button_font,bg='black',fg='white',command= lambda: submit_number(4))
three_button=tkinter.Button(button_frame,text='3',font=button_font,bg='black',fg='white',command= lambda: submit_number(3))
two_button=tkinter.Button(button_frame,text='2',font=button_font,bg='black',fg='white',command= lambda: submit_number(2))
one_button=tkinter.Button(button_frame,text='1',font=button_font,bg='black',fg='white',command= lambda: submit_number(1))
zero_button=tkinter.Button(button_frame,text='0',font=button_font,bg='black',fg='white',command= lambda: submit_number(0))

#first row
clear_button.grid(row=0,column=0,columnspan=2,sticky='WE',pady=1)
quit_button.grid(row=0,column=2,columnspan=2,sticky='WE',pady=1)
#Second row
inverse_button.grid(row=1,column=0,sticky="WE",pady=1)
square_button.grid(row=1,column=1,sticky='WE',pady=1)
exponent_button.grid(row=1,column=2,sticky='WE',pady=1)
division_button.grid(row=1,column=3,sticky='WE',pady=1)
#Third row
seven_button.grid(row=2,column=0,sticky="WE",pady=1,ipadx=20)
eight_button.grid(row=2,column=1,sticky="WE",pady=1,ipadx=20)
nine_button.grid(row=2,column=2,sticky="WE",pady=1,ipadx=20)
multiplication_button.grid(row=2,column=3,sticky="WE",pady=1,ipadx=20)
#4th row
six_button.grid(row=3,column=0,sticky="WE",pady=1,ipadx=20)
five_button.grid(row=3,column=1,sticky="WE",pady=1,ipadx=20)
four_button.grid(row=3,column=2,sticky="WE",pady=1,ipadx=20)
substract_button.grid(row=3,column=3,sticky="WE",pady=1,ipadx=20)
#5th row
three_button.grid(row=4,column=0,sticky="WE",pady=1,ipadx=20)
two_button.grid(row=4,column=1,sticky="WE",pady=1,ipadx=20)
one_button.grid(row=4,column=2,sticky="WE",pady=1,ipadx=20)
add_button.grid(row=4,column=3,sticky="WE",pady=1,ipadx=20)
#6th row
negate_button.grid(row=5,column=0,sticky="WE",pady=1,ipadx=10)
zero_button.grid(row=5,column=1,sticky="WE",pady=1,ipadx=20)
decimal_button.grid(row=5,column=2,sticky="WE",pady=1,ipadx=20)
equal_button.grid(row=5,column=3,sticky="WE",pady=1,ipadx=20)

root.mainloop()