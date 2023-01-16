from tkinter import *
import random
import time;

#------------------------------------------------Function --------------------------------for calculator

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def cleardisplay():
    global operator
    operator = " "
    text_input.set(" ")

def Equal():
    global operator
    res = str(eval(operator))
    text_input.set(res)
    operator = " "

#-------------------------------------------------------------------creating function for other buttons--------------------------------------

def TotalFunc():
    var = random.randint(10908, 50876)
    randomTotalFunct = str(var)
    text_input1.set(randomTotalFunct)

    CoF = float(text_input2.get())
    CoB = float(text_input3.get())
    CoR = float(text_input4.get())
    CoP = float(text_input5.get())
    CoC = float(text_input6.get())
    CoD = float(text_input7.get())

    CostOfFries = CoF *120
    CostOfBurger = CoB*85.86
    CostOfRice = CoR*72.37
    CostOfPasta = CoP*78.93
    CostOfChicken = CoC * 320.65
    CostOfDrink = CoD*20

    CostOfMeal =  "Rs", str('%.2f' %(CostOfFries + CostOfBurger  + CostOfRice+ CostOfRice + CostOfPasta + CostOfChicken + CostOfDrink))
    PayTax =  ((CostOfFries + CostOfBurger  + CostOfRice+ CostOfRice + CostOfPasta + CostOfChicken + CostOfDrink) * 0.18)

    Service_charge =  ((CostOfFries + CostOfBurger  + CostOfRice+ CostOfRice + CostOfPasta + CostOfChicken + CostOfDrink)/99)
    TotalCost = (CostOfFries + CostOfBurger  + CostOfRice+ CostOfRice + CostOfPasta + CostOfChicken + CostOfDrink)

    Service = "Rs", str('%.2f' % Service_charge)

    OverAllCost = "Rs", str('%.2f' % (Service_charge+PayTax+TotalCost))
    PaidTax = "Rs", str('%.2f' % PayTax)

    text_input8.set(CostOfMeal)
    text_input9.set(Service)
    text_input10.set(PaidTax)
    text_input11.set(CostOfMeal)
    text_input12.set(OverAllCost)
                                     

    

def QuitFunc():
    window.destroy()

def ResetFunc():
    text_input1.set(' ')
    text_input2.set(' ')
    text_input3.set(' ')
    text_input4.set(' ')
    text_input5.set(' ')
    text_input6.set(' ')
    text_input7.set(' ')
    text_input8.set(' ')
    text_input9.set(' ')
    text_input10.set(' ')
    text_input11.set(' ')
    text_input12.set(' ')
    


#---------------------------------------------------------------------------------------------
window = Tk()
window.geometry("1600x800+0+0")
window.title("Management System Software")
image_icon = PhotoImage(file = "C:\\Users\\neha\\Links\\Project mangmnt\\spdir.png")
window.iconphoto(True, image_icon)

#-----------------------------Text Varaible------------------------------------------
text_input = StringVar()
operator = " "

#---------------------------------Frames for Window-----------------------------------
f1 = Frame(window, width = 1600, height = 50, bg = "powder blue", relief = SUNKEN)
f1.pack(side=TOP)

f2 = Frame(window, width = 700, height = 700, relief = SUNKEN)
f2.pack(side=LEFT)

f3 = Frame(window, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
f3.pack(side=RIGHT)



localtime = time.asctime(time.localtime(time.time()))

l1 = Label(f1, font = ('arial', 40, 'bold'), text = "Management System Software", fg = "steel blue", bd =10, anchor = 'w')
l1.grid(row=0, column = 0)
l1 = Label(f1, font = ('arial', 15, 'bold'), text = localtime, fg = 'steel blue', bd = 10, anchor ='w')
l1.grid(row=1, column = 0)

#----------------------------------------------Text Box----------------------------------
display1 = Entry(f3, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 30, insertwidth =4, bg = 'powder blue', justify = 'right')
display1.grid(columnspan = 4)
#display1.place(x = 160, y = 20)

btn7 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '7', bg = 'powder blue', command = lambda: btnclick(7)).grid(row = 2, column = 0)
btn8 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '8', bg = 'powder blue', command = lambda: btnclick(8)).grid(row = 2, column = 1)
btn9 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '9',
              bg = 'powder blue', command = lambda: btnclick(9)).grid(row = 2, column = 2)
Addition = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '+', bg = 'powder blue', command = lambda: btnclick("+")).grid(row = 2, column = 3)

btn4 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '4', bg = 'powder blue', command = lambda: btnclick(4)).grid(row = 3, column = 0)
btn5 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '5', bg = 'powder blue', command = lambda: btnclick(5)).grid(row = 3, column = 1)
btn6 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '6',
              bg = 'powder blue', command = lambda: btnclick(6)).grid(row = 3, column = 2)
Subtraction = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '-', bg = 'powder blue', command = lambda: btnclick("-")).grid(row = 3, column = 3)



btn1 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '1', bg = 'powder blue', command = lambda: btnclick(1)).grid(row = 4, column = 0)
btn2 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '2', bg = 'powder blue', command = lambda: btnclick(2)).grid(row = 4, column = 1)
btn3 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '3',
              bg = 'powder blue', command = lambda: btnclick(3)).grid(row = 4, column = 2)
Multiplication = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = 'x', bg = 'powder blue', command = lambda: btnclick("*")).grid(row = 4, column = 3)

btn0 = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '0', bg = 'powder blue', command = lambda: btnclick(0)).grid(row = 5, column = 0)
clear = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = 'Clr', bg = 'powder blue', command = lambda: cleardisplay()).grid(row = 5, column = 1)
equal = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '=',
              bg = 'powder blue', command = Equal).grid(row = 5, column = 2)
division = Button(f3, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '/', bg = 'powder blue', command = lambda: btnclick("/")).grid(row = 5, column = 3)


#----------------------------------------------------Second Frame task------------------------------------

text_input1 = StringVar()
text_input2 = StringVar()
text_input3 = StringVar()
text_input4 = StringVar()
text_input5 = StringVar()
text_input6 = StringVar()
text_input7 = StringVar()
text_input8 = StringVar()
text_input9 = StringVar()
text_input10 = StringVar()
text_input11 = StringVar()
text_input12 = StringVar()

l2 = Label(f2, font = ('arial', 16, 'bold'), text = 'Reference', bd = 16, anchor = 'w').grid(row = 0, column =0)
display2 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input1, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 0, column = 1)

l3 = Label(f2, font = ('arial', 16, 'bold'), text = 'French Fries', bd = 16, anchor = 'w').grid(row =1, column =0)
display3 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input2, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 1, column = 1)

l4 = Label(f2, font = ('arial', 16, 'bold'), text = 'Burger Meal', bd = 16, anchor = 'w').grid(row =2, column =0)
display4 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input3, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 2, column = 1)

l5 = Label(f2, font = ('arial', 16, 'bold'), text = 'Rice Meal', bd = 16, anchor = 'w').grid(row =3, column =0)
display5 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input4, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 3, column = 1)


l6 = Label(f2, font = ('arial', 16, 'bold'), text = 'Cheese Pasta', bd = 16, anchor = 'w').grid(row =4, column =0)
display6 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input5, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 4,  column = 1)

l7 = Label(f2, font = ('arial', 16, 'bold'), text = 'Chicken Meal', bd = 16, anchor = 'w').grid(row =5, column =0)
display7 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input6, bd = 10, insertwidth =4,
                 bg = 'powder blue', justify = 'right').grid(row = 5,  column = 1)

#-----------------------------------------------------------Information with display-------------------------------------------------------------------
l8 = Label(f2, font = ('arial', 16, 'bold'), text = 'Drinks', bd = 16, anchor = 'w').grid(row =0, column =2)
display8 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input7, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 0,  column = 3)

l9 = Label(f2, font = ('arial', 16, 'bold'), text = 'Cost of Meal', bd = 16, anchor = 'w').grid(row =1, column =2)
display9 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input8, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 1,  column = 3)

l10 = Label(f2, font = ('arial', 16, 'bold'), text = 'Service Charges', bd = 16, anchor = 'w').grid(row =2, column =2)
display10 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input9, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 2,  column = 3)

l11 = Label(f2, font = ('arial', 16, 'bold'), text = 'Tax', bd = 16, anchor = 'w').grid(row =3, column =2)
display11 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input10, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 3,  column = 3)

l12 = Label(f2, font = ('arial', 16, 'bold'), text = 'Sub Total', bd = 16, anchor = 'w').grid(row =4, column =2)
display8 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input11, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 4,  column = 3)

l13 = Label(f2, font = ('arial', 16, 'bold'), text = 'Total Cost', bd = 16, anchor = 'w').grid(row =5, column =2)
display13 = Entry(f2, font = ('arial', 16, 'bold'), textvariable = text_input12, bd = 10, insertwidth =4,
                 bg = '#ffffff', justify = 'right').grid(row = 5,  column = 3)


#------------------------------------------------------------------Creating Buttons--------------------------------------------------------
btnTotal = Button(f2, padx = 16, pady = 8, fg = 'black', font=('arial', 16, 'bold'), width = 10, text = 'Total', bg = 'powder blue', command = TotalFunc).grid(row = 7, column = 1)

btnRst = Button(f2, padx = 16, pady = 8, fg = 'black', font=('arial', 16, 'bold'), width = 10, text = 'Reset', bg = 'powder blue', command = ResetFunc).grid(row = 7, column = 2)

btnQuit = Button(f2, padx = 16, pady = 8, fg = 'black', font=('arial', 16, 'bold'), width = 10, text = 'Quit', bg = 'powder blue', command = QuitFunc).grid(row = 7, column = 3)






window.mainloop()
