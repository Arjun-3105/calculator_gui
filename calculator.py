from tkinter import *

root = Tk()
root.title('Calculator')
e = Entry(root, width= 35, borderwidth = 5)
e.grid(row =0, column=0, columnspan=3, padx = 10, pady= 10 )

def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonclear():
    e.delete(0, END)

def buttonadd( ):
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def buttonequal():
    second_number = e.get()
    e.delete(0, END)

    if math =='addition':

        e.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    elif math == 'Multiply':
        e.insert(0, f_num * int(second_number))
    elif math == 'Divide':
        e.insert(0, f_num / int(second_number))

def buttonminus():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def buttonmul():
    first_number = e.get()
    global f_num
    global math
    math = 'Multiply'
    f_num = int(first_number)
    e.delete(0, END)
    

def buttondiv():
    first_number = e.get()
    global f_num
    global math
    math = 'Divide'
    f_num = int(first_number)
    e.delete(0, END)
    



# defining buttons
b1 = Button(root, text = '1', padx = 40, pady =20, command = lambda : buttonclick(1))
b2 = Button(root, text= '2', padx = 40, pady =20, command = lambda : buttonclick(2))
b3 = Button(root, text='3', padx = 40, pady =20, command = lambda : buttonclick(3))
b4 = Button(root, text='4', padx = 40, pady =20, command = lambda : buttonclick(4))
b5 = Button(root, text='5', padx = 40, pady =20, command = lambda : buttonclick(5))
b6 = Button(root, text= '6', padx = 40, pady =20, command = lambda : buttonclick(6))
b7 = Button(root, text = '7', padx = 40, pady =20, command = lambda : buttonclick(7))
b8 = Button(root, text = '8', padx = 40, pady =20, command = lambda : buttonclick(8))
b9 = Button(root, text = '9', padx = 40, pady =20, command = lambda : buttonclick(9))
b0 = Button(root, text = '0', padx = 40, pady =20, command = lambda : buttonclick(0))
bclear = Button(root, text =  'Clear', padx = 30, pady =20, command = buttonclear)
badd = Button(root, text = '+', padx = 40, pady =20, command = buttonadd)
bminus = Button(root, text = '-', padx = 40, pady =20, command = lambda : buttonminus())
bmul = Button(root, text = '*', padx = 40, pady =20, command = lambda : buttonmul())
bdiv = Button(root, text = '/', padx = 40, pady =20, command = lambda : buttondiv())
bequal = Button(root, text = '=', padx = 40, pady =20, command = buttonequal)

# loading buttons on the screen
b1.grid(row = 3, column =0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)

b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)

b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b0.grid(row = 4, column = 1)
bclear.grid(row = 4, column = 0, columnspan = 1)
badd.grid(row = 1, column =3)
bminus.grid(row = 2, column = 3)
bmul.grid(row = 3, column = 3)
bdiv.grid(row = 4, column = 3 )
bequal.grid(row = 4, column = 2)



root.mainloop()

