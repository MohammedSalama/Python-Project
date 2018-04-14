from tkinter import*
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisply():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
    


cal = Tk()
cal.title("calculator")
operator=""
text_Input =StringVar()


txtDisply = Entry(cal,font=('arial', 20,'bold') ,textvariable=text_Input, bd=20,
                  insertwidth=4, bg="#5B2458" , justify='right').grid(columnspan=4)
#=============================================================================
btn7 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="7" ,bg="#ECE03A" ,command=lambda:btnClick(7)).grid(row=1,column=0)

btn8 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="8" , bg="#ECE03A",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="9" , bg="#ECE03A",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="+" ,bg="#ECE03A",command=lambda:btnClick("+")).grid(row=1,column=3)
#==============================================================================
btn4 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="4" ,bg="#ECE03A",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="5" , bg="#ECE03A",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="6" , bg="#ECE03A",command=lambda:btnClick(6)).grid(row=2,column=2)

Subtraction = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="-" ,bg="#ECE03A",command=lambda:btnClick("-")).grid(row=2,column=3)
#===============================================================================
btn1 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="1" ,bg="#ECE03A",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="2" , bg="#ECE03A",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="3" , bg="#ECE03A",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiply = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="*" ,bg="#ECE03A",command=lambda:btnClick("*")).grid(row=3,column=3)
#===============================================================================
btnClear = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="C" , bg="#ECE03A",command=btnClearDisply).grid(row=4,column=1)

btn0 = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="0" ,bg="#ECE03A",command=lambda:btnClick(0)).grid(row=4,column=0)

btnEquals= Button(cal,padx=16,pady=16 ,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="=" , bg="#ECE03A",command=btnEqualsInput).grid(row=4,column=2)

Division = Button(cal,padx=16,pady=16,bd=8 , fg="black" ,font=('arial', 20,'bold'),
              text="/" ,bg="#ECE03A",command=lambda:btnClick("/")).grid(row=4,column=3)
#==============================================================================
cal.mainloop()
