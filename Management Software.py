#print('hello this is py managment software.beta.1.1apk by designed by a.s.r')
#print('i have an in my mind idea to make dis for lucky customers spin or do ans and win like something/....')
from tkinter import *
import random
import time



#functions for buttons for f2 for calli.....................................................................
def btnclick(numbers):
    global space_with_num # this variable we write it like this because we want use it dor many times///
    space_with_num =space_with_num + str(numbers)
    text1.set(space_with_num)

def clearup():
    global space_with_num
    #main error in mmngnt sftwr this line imp space_with_num = " "
    space_with_num = " "
    text1.set("")

def evaal():
    global space_with_num
    result=str(eval(space_with_num))
    text1.set(result)   

#func for btns for main pro...............................................................................................
def Ttlfn():# if fun work are big or small no matters but please use function name length large
    obbj=random.randint(123456789,674581320)
    var=str(obbj)
    text2.set(var)
#getting inputing valiues givin by users..
    cs=float(text3.get())
    dk=float(text4.get())
    sr=float(text5.get())
    ck=float(text6.get())
    nnvg=float(text7.get())

    c_and_s=cs*80
    drink=dk*90
    s_request=sr*599
    chakhna=ck*60
    nonvegitems=nnvg*399
    
    sbtotal=int(float('%.2f' %(c_and_s+drink+s_request+chakhna+nonvegitems)))
    text8.set( sbtotal)

    txpyl= int(float('%.2f' %(sbtotal*0.18)))
    servtx=float('%.2f' %(sbtotal/99))
    redemdis=float(-102)
    ttlpybl=float('%.2f' %(sbtotal+txpyl+servtx+(redemdis)))

    text9.set(txpyl)
    text10.set(servtx)
    text11.set(redemdis)
    text12.set(ttlpybl)




def forbt1_clr():
    text2.set('')
    text3.set('')
    text4.set('')
    text5.set('')
    text6.set('')
    text7.set('')
    text8.set('')
    text9.set('')
    text11.set('')
    text10.set('')
    text12.set('')

def forp2_ext():
    window1.destroy()  
#tk work gui..................................................................................................................................
window1=Tk()
window1.geometry("1600x800+0+0")
window1.title('managment beta v1.1')
#assign opert....................................................................
space_with_num=''
text1=StringVar()

#frames column...........................................................................................................................
f1=Frame(window1,width=1600,height=50,bg="blue",relief = SUNKEN)
f1.pack(side=TOP)
f2=Frame(window1,width=300,height=200,bg='powder blue',relief = SUNKEN)
f2.pack(side=RIGHT)
f3=Frame(window1,width=300,height=700,bg='powder blue',relief = SUNKEN)
f3.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))
#setting up first frame..................................................................................................................
l1=Label(f1,font =('arial',40,'bold'),text='MANAGEMENT PRO BETA V1.1',fg='red',bd =10, anchor = 'w')
l1.grid(row=0, column = 0)
l1 = Label(f1, font = ('arial', 15, 'bold'), text = localtime, fg = 'steel blue', bd = 10, anchor ='w')
l1.grid(row=1, column = 0)

#setting up second frame..................................................................................................................
display1=Entry(f2,font=('arial',18,'bold'),textvariable=text1,bd=8,justify='right',insertwidth=4)
display1.grid(columnspan=20)


#setting up buttons for calculators for second frame......................................................................................
#btn1=Button(f2,padx=16,pady=16,font=('arial',30,'bold'),text='1',command=lambda:btnclick(1)).grid(row=2,column=0)
#btn2=Button(f2,padx=16,pady=16,font=('arial',30,'bold'),text='2',command=lambda:btnclick(2)).grid(row=2,column=1)
btn1 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '1', bg = 'powder blue', command = lambda: btnclick(1)).grid(row = 1, column = 0)
btn2 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '2', bg = 'powder blue', command = lambda: btnclick(2)).grid(row = 1, column = 1)
btn3 = Button(f2, padx = 16, pady = 16, bd =5, fg = 'black', font = ('arial', 18, 'bold'), text = '3', bg = 'powder blue', command = lambda: btnclick(3)).grid(row = 1, column = 2)
addi = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '+', bg = 'powder blue', command = lambda: btnclick('+')).grid(row = 1, column = 3)

btn4 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '4', bg = 'powder blue', command = lambda: btnclick(4)).grid(row = 2, column = 0)
btn5 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '5', bg = 'powder blue', command = lambda: btnclick(5)).grid(row = 2, column = 1)
btn6 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '6', bg = 'powder blue', command = lambda: btnclick(6)).grid(row = 2, column = 2)
subb = Button(f2, padx = 16, pady = 16, bd =5, fg = 'black', font = ('arial', 18, 'bold'), text = '-', bg = 'powder blue', command = lambda: btnclick('-')).grid(row = 2, column = 3)

btn7 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '7', bg = 'powder blue', command = lambda: btnclick(7)).grid(row = 3, column = 0)
btn8 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '8', bg = 'powder blue', command = lambda: btnclick(8)).grid(row = 3, column = 1)
btn9 = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '9', bg = 'powder blue', command = lambda: btnclick(9)).grid(row = 3, column = 2)
multi = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 18, 'bold'), text = '*', bg = 'powder blue', command = lambda: btnclick('*')).grid(row = 3, column = 3)

clear = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 7, 'bold'),height=4,text = 'clearup', bg = 'pink', command = lambda: clearup()).grid(row = 4, column = 0)
zer= Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 20, 'bold'), text = '0', bg = 'powder blue', command = lambda: btnclick(0)).grid(row = 4, column = 1)
equul = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 20, 'bold'), text = '=', bg = 'green', command = lambda: evaal()).grid(row = 4, column = 2)
divv = Button(f2, padx = 16, pady = 16, bd = 5, fg = 'black', font = ('arial', 20, 'bold'), text = '/', bg = 'powder blue', command = lambda: btnclick('/')).grid(row = 4, column = 3)

#work on frame3 for systemmain...........................................................................................................................
text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()
text6=StringVar()
text7=StringVar()
text8=StringVar()
text9=StringVar()
text10=StringVar()
text12=StringVar()
text11=StringVar()
text13=StringVar()
text14=StringVar()


lavel1=Label(f3,font=('arial',15,'bold'),text='reference code',bg='powder blue',bd=10).grid(row=0,column=0)
display2=Entry(f3,font=('arial',12,'bold'),textvariable=text2,bg='powder blue',bd=10,justify='right').grid(row=0,column=1)

lavel2=Label(f3,font=('arial',15,'bold'),text='chips and snacks',bg='powder blue',bd=10).grid(row=1,column=0)
display3=Entry(f3,font=('arial',12,'bold'),textvariable=text3,bg='powder blue',bd=10,justify='right').grid(row=1,column=1)

lavel3=Label(f3,font=('arial',15,'bold'),text='drinks',bg='powder blue',bd=10).grid(row=3,column=0)
display3=Entry(f3,font=('arial',12,'bold'),textvariable=text4,bg='powder blue',bd=10,justify='right').grid(row=3,column=1)

lavel4=Label(f3,font=('arial',15,'bold'),text='special requested food',bg='powder blue',bd=10).grid(row=4,column=0)
display4=Entry(f3,font=('arial',12,'bold'),textvariable=text5,bg='powder blue',bd=10,justify='right').grid(row=4,column=1)

lavel5=Label(f3,font=('arial',15,'bold'),text='chakhnaa',bg='powder blue',bd=10).grid(row=5,column=0)
display5=Entry(f3,font=('arial',12,'bold'),textvariable=text6,bg='powder blue',bd=10,justify='right').grid(row=5,column=1)

#from nex line..............................................................................................................
lavel7=Label(f3,font=('arial',15,'bold'),text='non veg items',bg='powder blue',anchor = 'w',bd=10).grid(row=0,column=2)
display7=Entry(f3,font=('arial',12,'bold'),textvariable=text7,bg='powder blue',bd=5, insertwidth =4,justify='left').grid(row=0,column=3)

lavel8=Label(f3,font=('arial',15,'bold'),text='sub total',bg='powder blue',anchor = 'w',fg='orange',bd=10).grid(row=1,column=2)
display7=Entry(f3,font=('arial',12,'bold'),textvariable=text8,bg='powder blue',bd=10, insertwidth =4,justify='left').grid(row=1,column=3)

taxy=Label(f3,font=('arial',15,'bold'),text='tax payble',bg='powder blue',anchor = 'w',fg='black',bd=10).grid(row=2,column=2)
display8=Entry(f3,font=('arial',12,'bold'),textvariable=text9,bg='powder blue',bd=10, insertwidth =4,justify='left').grid(row=2,column=3)

serv_chrg=Label(f3,font=('arial',15,'bold'),text='service tax',bg='powder blue',anchor = 'w',fg='steel blue',bd=10).grid(row=3,column=2)
display9=Entry(f3,font=('arial',12,'bold'),textvariable=text10,bg='powder blue',bd=10, insertwidth =4,justify='left').grid(row=3,column=3)

discnt=Label(f3,font=('arial',15,'bold'),text='reedemable discount',bg='powder blue',anchor = 'w',fg='green',bd=10).grid(row=4,column=2)
display10=Entry(f3,font=('arial',12,'bold'),textvariable=text11,bg='powder blue',bd=10, insertwidth =4,justify='left').grid(row=4,column=3)

ttl=Label(f3,font=('arial',15,'bold'),text='total amt payble',bg='yellow',anchor = 'w',fg='red',bd=10).grid(row=5,column=2)
display10=Entry(f3,font=('arial',12,'bold'),textvariable=text12,bg='powder blue',bd=10, insertwidth =4,justify='left').grid(row=5,column=3)

#three butttons for main pro...............................................................................................

btn_pro1=Button(f3,padx=16,pady=8,font=('arial',16,'bold'),width=10,text='clear',command=forbt1_clr,bg='orange',bd=5).grid(row=7,column=0)

btn_pro2=Button(f3,padx=16,pady=8,font=('arial',16,'bold'),width=10,text='exit',command=forp2_ext,bg='red',bd=5).grid(row=7,column=2)

btn_pro3=Button(f3,padx=16,pady=8,font=('arial',16,'bold'),width=10,text='TOTAL',command=Ttlfn,bg='green',bd=5).grid(row=7,column=3)


window1.mainloop()



