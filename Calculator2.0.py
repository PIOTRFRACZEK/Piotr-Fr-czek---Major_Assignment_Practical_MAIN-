from tkinter import*
import math
import tkinter.messagebox 
operator = ""

"""
Code Author: Fraczek Piotr
The purpose of the  app: A simple calculator designed according to the requirements presented by Alice wich you can find in menubar in the app: File\About\
Name of the app: "Calculator for Alice"
Version: 2.0 2021
Copyright details: © Copyright 2021 Piotr Fraczek. All Rights Reserved, © 2021 Alice.
"""
# display whatever the user clicks on
def btnOnClick(numb):
    global operator  # operator will hold my expressions for manipulation
    operator = operator + str(numb);
    text_input.set(operator);

# perfom the user's operation and display the result 
def btnEqual():
    try:
        global operator
        Op_res = str(eval(operator));
        text_input.set(operator + '=' + Op_res);
        operator = "";
# if error is generate then handle/ dividion by 0
    except ZeroDivisionError:# divide by 0
     text_input.set("Division by zero")
    except:# others errors
     text_input.set("Invalid Operation")
# messagebox.showerror("An error has occurred", "Invalid Operation")
     operator = "";
        
# Square root function and catching negative numbers     
def square_root():
	global operator
	Op_res = str(eval(operator))
	if int(Op_res)>=0:
	 Op_res=math.sqrt(int(Op_res));
	 text_input.set('√' + str(operator) + '=' + str(Op_res));
	 operator = "";
	else:
	 text_input.set('No √ for negative numbers. ');
	 operator = "";

# clearing everything on screen
def btnCL():
    global operator
    operator = ""; 
    text_input.set("");
   
AliceCal = Tk();
AliceCal.title("Calculator for Alice")
AliceCal.resizable(width= False, height=False) # window// no change size
calc=Frame(AliceCal) # frame for menu
calc.grid()
operator = ""
text_input = StringVar()

# display screen creation (i.e. an entry text)
txtDisplay = Entry(AliceCal,
           font = ('arial', 20, 'bold'),
           textvariable = text_input,
           bd = 30,
           insertwidth =4,
           fg = 'black',
           bg = 'white',
           width=28, 
           justify = 'right').grid(row=0, columnspan=4, sticky=W+E);


# creation of buttons
# row 1
btn_off = Button(AliceCal,padx = 20, bd = 4,
             fg = 'black',
             bg = 'lightsteelblue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'OFF',
             command = AliceCal.destroy,
             height=1, width=2).grid(row=1, column=0, columnspan=2, sticky=W+E)
btn_clear = Button(AliceCal,
             padx = 20, # you can also add pady = 16
             bd = 4,
             fg = 'black',
             bg = 'lightsteelblue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'CL',
             command = btnCL,
             height=1, width=2).grid(row=1, column=2, sticky=W+E)

btn_square_root = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '√',
             command = square_root, # use destroy to close GUI
             height=1, width=2).grid(row=1, column=3, sticky=W+E)


# row 2
btn7 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '7',
             command = lambda:btnOnClick(7),
             height=1, width=2).grid(row=2, column=0, sticky=W+E)
btn8 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '8',
             command = lambda:btnOnClick(8),
             height=1, width=2).grid(row=2, column=1, sticky=W+E)
btn9 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '9',
             command = lambda:btnOnClick(9),
             height=1, width=2).grid(row=2, column=2, sticky=W+E)
btn_divide = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '÷', 
             command = lambda:btnOnClick("/"), # "/" or '÷' equally as valid
             height=1, width=2).grid(row=2, column=3, sticky=W+E)

# row 3
btn4 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '4',
             command = lambda:btnOnClick(4),
             height=1, width=2).grid(row=3, column=0, sticky=W+E)
btn5 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '5',
             command = lambda:btnOnClick(5),
             height=1, width=2).grid(row=3, column=1, sticky=W+E)
btn6 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '6',
             command = lambda:btnOnClick(6),
             height=1, width=2).grid(row=3, column=2, sticky=W+E)
btn_multiply= Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '*', # or '÷' equally as valid
             command = lambda:btnOnClick("*"), 
             height=1, width=2).grid(row=3, column=3, sticky=W+E)
# row 4
btn1 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '1',
             command = lambda:btnOnClick(1),
             height=1, width=2).grid(row=4, column=0, sticky=W+E)
btn2 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '2',
             command = lambda:btnOnClick(2),
             height=1, width=2).grid(row=4, column=1, sticky=W+E)
btn3 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '3',
             command = lambda:btnOnClick(3),
             height=1, width=2).grid(row=4, column=2, sticky=W+E)
btn_subtract = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '-',
             command = lambda:btnOnClick('-'),
             height=1, width=2).grid(row=4, column=3, sticky=W+E)

# row 5
btn0 = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'whitesmoke',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '0',
             command = lambda:btnOnClick(0),
             height=1, width=2).grid(row=5, column=0,columnspan=2, sticky=W+E)
btn_equal = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '=',
             command = btnEqual,
             height=1, width=2).grid(row=5, column=2, sticky=W+E)
btn_add = Button(AliceCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'light blue',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '+',
             command = lambda:btnOnClick('+'),
             height=1, width=2).grid(row=5, column=3, sticky=W+E)


# About: information about requirements
def iAbout():
	iAbout= tkinter.messagebox.showinfo("Calculator for Alice", '''The App name: "Calculator for Alice"\n\nThe purpose of the  app: \nA simple calculator designed according to the requirements presented by Alice:\n
a. Alice ideally wants this program to be a GUI App.
b. The App must have buttons for whole numbers from 0 to 9, a “clear” button—buttons for addition (+), subtraction (-), multiplication (x) and division (/)—and a button for square root (√).   
Buttons available: 0 1 2 3 4 5 6 7 8 9 + - / * = √ CL OFF
c. Alice must be able to perform division, addition, subtraction and multiplication operations. In addition, she must be able to calculate the square root of a number. Finally, she must be able to clear the screen and start a new operation if she wishes to.
d. The screen must clearly display the operation being performed. For example, suppose Alice wants to add 2 and 3. The screen of the calculator must show “2 + 3 = 5”.
e. Errors: Unless complex numbers are involved, negative numbers don’t outright have square roots. Also, you can’t outright divide by 0.
f. ALTERNATIVE: The calculator can indeed be built without the need for a GUI. However, you must take steps to ensure you meet all of Alice’s demands. That is to say, you wouldn’t have buttons in your program, but it is up to you to ensure Alice can do all she has requested.
\n\nCode Author: Fraczek Piotr
\nVersion: 2.0 2021
\nCopyright details: © Copyright 2021 Piotr Fraczek. All Rights Reserved, © 2021 Alice.  ''')
# Exit y/n function
def iExit():
	iExit = tkinter.messagebox.askyesno("Calculator for Alice",'Confirm if you want to exit?')
	if iExit > 0:
		AliceCal.destroy()
		return


# Menu with EXIT and ABOUT
menubar=Menu(calc)

filemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='About', command=iAbout) # Menu INfo about 
filemenu.add_separator() #separator in the menu/line
filemenu.add_command(label='Exit', command=iExit) # menu Exit y/n
AliceCal.configure(menu=menubar)      
# start the App
AliceCal.mainloop()