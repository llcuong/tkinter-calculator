from tkinter import *
import numpy as np
from math import *
from sympy import Symbol,integrate,expand,simplify
import matplotlib.pyplot as plt

def Click(numbers):
    global operator
    operator+=str(numbers)
    text_input.set(operator)
def Equal():
    global operator
    try:
        operator = str(eval(operator))
    except:
        try:
            if 'P' in operator:
                a = operator.split('P')
                operator = str(factorial(int(a[0]))/(factorial(int(a[0])-int(a[1]))))
            if 'C' in operator:
                a = operator.split('C')
                operator = str(factorial(int(a[0]))/(factorial(int(a[0])-int(a[1]))*factorial(int(a[1]))))
            if 'Σ' in operator:
                a = operator[2:len(operator) - 1]
                b = a.split('.')
                ans = 0
                if eval(b[1]) >= eval(b[0]):
                    for i in range(eval(b[0]),eval(b[1])+1):
                        ans+=i
                    operator = str(ans)
                else:operator = 'Error'
            if 'π' in operator:
                a = operator[2:len(operator) - 1]
                b = a.split('.')
                ans = 1
                if eval(b[1])>=eval(b[0]):
                    for i in range(eval(b[0]),eval(b[1])+1):
                        ans*=i
                    operator = str(ans)
                else:operator = 'Error'
            if '!' in operator:
                a = operator.split('!')
                P1 = factorial(int(a[0]))
                if(len(a)>1):
                    if(len(a[1])>0):
                        P2 = eval(a[1])
                    else:
                        P2 = 0
                operator = P1 + P2
        except:
            operator = 'Error'
    text_input.set(operator)
def Clear():
    global operator
    operator = ''
    text_input.set(operator)
def der():
    global operator
    try:
        x = Symbol('x')
        y = eval((text_input.get()))
        operator = y.diff()
    except:
        operator = 0
    text_input.set(operator)
def inder():
    global operator
    try:
        x = Symbol('x')
        y = eval((text_input.get()))
        operator = integrate(y)
    except:
        operator = str(operator)+'*x'
    text_input.set(operator)
def GE():
    global operator
    operator = text_input.get()[:-1]
    text_input.set(operator)
def Sin():
    global operator
    operator+=str('sin(')
    text_input.set(operator)
def Cos():
    global operator
    operator+=str('cos(')
    text_input.set(operator)
def Tan():
    global operator
    operator+=str('tan(')
    text_input.set(operator)
def Sqrt():
    global operator
    operator+=str('sqrt(')
    text_input.set(operator)
def Log():
    global operator
    operator+=str('log(')
    text_input.set(operator)
def Log10():
    global operator
    operator+=('log10(')
    text_input.set(operator)
def Abs():
    global operator
    operator+=str('abs(')
    text_input.set(operator)
def Exp():
    global operator
    operator+=str('exp(')
    text_input.set(operator)
def E10():
    global operator
    operator+=str('10**(')
    text_input.set(operator)
def Asin():
    global operator
    operator+=str('asin(')
    text_input.set(operator)
def Acos():
    global operator
    operator+=str('acos(')
    text_input.set(operator)
def Atan():
    global operator
    operator+=str('atan(')
    text_input.set(operator)
def Shift():
    shift = Toplevel()
    shift.title('Shift')
    shift.configure(background='black')
    shift_text=StringVar()
    shift_text.set('Answer Here')
    shift_display= Label(shift, text='Shift',bg='black',fg='orange',font=('arial',20)).grid(row=1,column=0,columnspan=2)
    button_cramer_1 = Button(shift, padx=10, bd=0, fg='white', bg='black', text='Simul Equation 1', font=('arial', 20),
                          command=lambda:Cramer_1()).grid(row=2,column=0)
    button_cramer_2 = Button(shift, padx=10, bd=0, fg='white', bg='black', text='Simul Equation 2', font=('arial', 20),
                           command=lambda:Cramer_2()).grid(row=3, column=0)
    button_cramer_3 = Button(shift,padx=10, bd=0, fg='white', bg='black', text='Simul Equation 3', font=('arial', 20),
                           command=lambda:Cramer_3()).grid(row=4, column=0)
    button_cramer_4 = Button(shift,padx=10, bd=0, fg='white', bg='black', text='Simul Equation 4', font=('arial', 20),
                           command=lambda:Cramer_4()).grid(row=5, column=0)
    button_poly2 = Button(shift, padx=10, bd=0, fg='white', bg='black', text='Polynomial 2',font=('arial', 20),
                         command=lambda: Poly2()).grid(row=6, column=0)
    button_poly3 = Button(shift, padx=10, bd=0, fg='white', bg='black', text='Polynomial 3',font=('arial', 20),
                         command=lambda: Poly3()).grid(row=7, column=0)
    button_plt = Button(shift,padx=10,bg='black',fg='white',bd=0,text='Plot',font=('arial',20),command=lambda:Plot()).grid(row=8,column=0)
    button_expa = Button(shift, padx=10, bd=0, fg='white', bg='black', text='Expand/Simply', font=('arial', 20),
                          command=lambda: Expa()).grid(row=9, column=0)
    def Cramer_1():
        cramer = Toplevel()
        cramer.title('Simul 1')
        cramer.configure(background='black')
        answer_display = StringVar()
        A = StringVar()
        B = StringVar()
        cramer_display = Entry(cramer, width=14, font=('arial', 20), textvariable=answer_display,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=4)
        label_a = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A', bg='black',
                         command=lambda: Click1('')).grid(row=2, column=0)
        input_a = Entry(cramer, textvariable=A, width=8, font=('arial', 20), bd=1, bg='white', justify='right')
        input_a.grid(row=2, column=1,columnspan=2)

        label_b = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B', bg='black',
                         command=lambda: Click2('')).grid(row=3, column=0)
        input_b = Entry(cramer, textvariable=B, width=8, font=('arial', 20), bd=1, bg='white', justify='right')
        input_b.grid(row=3, column=1,columnspan=2)
        ans = Button(cramer,bd=0,fg='white',bg='black', text='Answer', font=('arial', 20), command=lambda:Check_cramer1()).grid(row=4,column=1)
        def Check_cramer1():
            a = eval(A.get())
            b = eval(B.get())
            try:
                if (a == 0):
                    if (b == 0): answer_display.set('Vo so nghiem')
                    if (b != 0): answer_display.set('Vo nghiem')
                else:
                    answer_display.set(-b/a)
            except:
                answer_display.set('Error')
        def Click1(numbers):
            global operator
            operator += str(numbers)
            A.set(operator)
        def Click2(numbers):
            global operator
            operator += str(numbers)
            B.set(operator)
    def Cramer_2():
        cramer = Toplevel()
        cramer.title('Simul 2')
        cramer.configure(background='black')
        answer_display1,answer_display2 = StringVar(),StringVar()
        A1,A2,B1,B2,C1,C2 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        cramer_display1 = Entry(cramer, width=20, font=('arial', 20), textvariable=answer_display1,
                               bd=10, insertwidth=6, justify='right').grid(row=0,column=0,columnspan=4)
        cramer_display2 = Entry(cramer, width=20, font=('arial', 20), textvariable=answer_display2,
                               bd=10, insertwidth=6, justify='right').grid(row=1,column=0,columnspan=4)
        label_a1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A1', bg='black',
                         command=lambda: ClickA1('')).grid(row=2, column=0)
        input_a1 = Entry(cramer,textvariable=A1, width=4, font=('arial', 20), bd=1, justify='right')
        input_a1.grid(row=2, column=1)
        label_b1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B1', bg='black',
                         command=lambda: ClickB1('')).grid(row=2, column=2)
        input_b1 = Entry(cramer,textvariable=B1, width=4, font=('arial', 20), bd=1,justify='right')
        input_b1.grid(row=2, column=3)
        label_a2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A2', bg='black',
                         command=lambda: ClickA2('')).grid(row=3, column=0)
        input_a2 = Entry(cramer,textvariable=A2, width=4, font=('arial',20), bd=1, justify='right')
        input_a2.grid(row=3, column=1)
        label_b2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B2', bg='black',
                         command=lambda: ClickB2('')).grid(row=3, column=2)
        input_b2 = Entry(cramer,textvariable=B2, width=4, font=('arial',20), bd=1, justify='right')
        input_b2.grid(row=3, column=3)
        label_c1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C1', bg='black',
                         command=lambda: ClickC1('')).grid(row=2, column=4)
        input_c1 = Entry(cramer,textvariable=C1, width=4, font=('arial', 20),bd=1, justify='right')
        input_c1.grid(row=2, column=5)
        label_c2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C2', bg='black',
                         command=lambda: ClickC2('')).grid(row=3, column=4)
        input_c2 = Entry(cramer,textvariable=C2, width=4, font=('arial', 20), bd=1,justify='right')
        input_c2.grid(row=3, column=5)
        ans = Button(cramer, padx=20, text='Answer',fg='white',bg='black', font=('arial',20),command=lambda:Check_cramer2()).grid(row=0,column=4,columnspan=2)
        def Check_cramer2():
            try:
                a1 = float(input_a1.get())
                a2 = float(input_a2.get())
                b1 = float(input_b1.get())
                b2 = float(input_b2.get())
                c1 = float(input_c1.get())
                c2 = float(input_c2.get())
                D = a1*b2 - a2*b1
                Dx= c1*b2 - c2*b1
                Dy= a1*c2 - a2*c1
                if (D==0):
                    if(Dx==Dy==0):answer_display1.set('Vo so nghiem')
                    if(Dx!=0 or Dy!=0): answer_display1.set('Vo nghiem')
                else:
                    answer_display1.set('x='+str(Dx/D))
                    answer_display2.set('y='+str(Dy/D))
            except:
                answer_display1.set('Error')
                answer_display2.set('Error')
        def ClickA1(numbers):
            global operator
            operator += str(numbers)
            A1.set(operator)
        def ClickA2(numbers):
            global operator
            operator += str(numbers)
            A2.set(operator)
        def ClickB1(numbers):
            global operator
            operator += str(numbers)
            B1.set(operator)
        def ClickB2(numbers):
            global operator
            operator += str(numbers)
            B2.set(operator)
        def ClickC1(numbers):
            global operator
            operator += str(numbers)
            C1.set(operator)
        def ClickC2(numbers):
            global operator
            operator += str(numbers)
            C2.set(operator)
    def Cramer_3():
        cramer = Toplevel()
        cramer.title('Simul 3')
        cramer.configure(background='black')
        answer_display1,answer_display2,answer_display3 = StringVar(),StringVar(),StringVar()
        A1,A2,A3,B1,B2,B3,C1,C2,C3,D1,D2,D3 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        cramer_display1 = Entry(cramer, width=10, font=('arial', 20), textvariable=answer_display1,
                               bd=10, insertwidth=6, justify='right').grid(row=0,column=0,columnspan=2)
        cramer_display2 = Entry(cramer, width=10, font=('arial', 20), textvariable=answer_display2,
                               bd=10, insertwidth=6, justify='right').grid(row=0,column=2,columnspan=2)
        cramer_display3 = Entry(cramer, width=10, font=('arial', 20), textvariable=answer_display3,
                               bd=10, insertwidth=6, justify='right').grid(row=0,column=4,columnspan=2)
        label_a1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A1', bg='black',
                         command=lambda: ClickA1('')).grid(row=2, column=0)
        input_a1 = Entry(cramer, textvariable=A1, width=4, font=('arial', 20), bd=1,justify='right')
        input_a1.grid(row=2, column=1)

        label_b1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B1', bg='black',
                         command=lambda: ClickB1('')).grid(row=2, column=2)
        input_b1 = Entry(cramer, textvariable=B1, width=4, font=('arial', 20), bd=1,justify='right')
        input_b1.grid(row=2, column=3)

        label_c1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C1', bg='black',
                         command=lambda: ClickC1('')).grid(row=2, column=4)
        input_c1 = Entry(cramer, textvariable=C1, width=4, font=('arial', 20),bd=1,justify='right')
        input_c1.grid(row=2, column=5)

        label_d1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D1', bg='black',
                         command=lambda: ClickD1('')).grid(row=2, column=6)
        input_d1 = Entry(cramer, textvariable=D1, width=4, font=('arial', 20), bd=1, justify='right')
        input_d1.grid(row=2, column=7)

        label_a2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A2', bg='black',
                         command=lambda: ClickA2('')).grid(row=3, column=0)
        input_a2 = Entry(cramer, textvariable=A2, width=4, font=('arial', 20), bd=1,justify='right')
        input_a2.grid(row=3, column=1)

        label_b2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B2', bg='black',
                         command=lambda: ClickB2('')).grid(row=3, column=2)
        input_b2 = Entry(cramer, textvariable=B2, width=4, font=('arial', 20), bd=1,justify='right')
        input_b2.grid(row=3, column=3)

        label_c2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C2', bg='black',
                         command=lambda: ClickC2('')).grid(row=3, column=4)
        input_c2 = Entry(cramer, textvariable=C2, width=4, font=('arial', 20), bd=1,justify='right')
        input_c2.grid(row=3, column=5)

        label_d2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D2', bg='black',
                         command=lambda: ClickD2('')).grid(row=3, column=6)
        input_d2 = Entry(cramer, textvariable=D2, width=4, font=('arial', 20), bd=1,justify='right')
        input_d2.grid(row=3, column=7)

        label_a3 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A3', bg='black',
                         command=lambda: ClickA3('')).grid(row=4, column=0)
        input_a3 = Entry(cramer, textvariable=A3, width=4, font=('arial', 20), bd=1,justify='right')
        input_a3.grid(row=4, column=1)

        label_b3 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B3', bg='black',
                         command=lambda: ClickB3('')).grid(row=4, column=2)
        input_b3 = Entry(cramer, textvariable=B3, width=4, font=('arial', 20), bd=1,justify='right')
        input_b3.grid(row=4, column=3)

        label_c3 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C3', bg='black',
                         command=lambda: ClickC3('')).grid(row=4, column=4)
        input_c3 = Entry(cramer, textvariable=C3, width=4, font=('arial', 20), bd=1,justify='right')
        input_c3.grid(row=4, column=5)

        label_d3 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D3', bg='black',
                         command=lambda: ClickD3('')).grid(row=4, column=6)
        input_d3 = Entry(cramer, textvariable=D3, width=4, font=('arial', 20), bd=1,justify='right')
        input_d3.grid(row=4, column=7)

        ans = Button(cramer, padx=20, text='Answer', font=('arial', 20), fg='white', bg='black',
                     command=lambda: Check_cramer3()).grid(row=0, column=6,columnspan=2)
        def Check_cramer3():
            try:
                a1 = float(input_a1.get())
                a2 = float(input_a2.get())
                a3 = float(input_a3.get())
                b1 = float(input_b1.get())
                b2 = float(input_b2.get())
                b3 = float(input_b3.get())
                c1 = float(input_c1.get())
                c2 = float(input_c2.get())
                c3 = float(input_c3.get())
                d1 = float(input_d1.get())
                d2 = float(input_d2.get())
                d3 = float(input_d3.get())
                h = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
                hx= np.array([[b1,c1,d1],[b2,c2,d2],[b3,c3,d3]])
                hy= np.array([[a1,c1,d1],[a2,c2,d2],[a3,c3,d3]])
                hz= np.array([[a1,b1,d1],[a2,b2,d2],[a3,b3,d3]])
                d = np.linalg.det(h)
                dx= np.linalg.det(hx)
                dy= np.linalg.det(hy)
                dz= np.linalg.det(hz)
                if (d==0):
                    if (dx==0 and dy== 0 and dz==0):
                        answer_display1.set('Vo so nghiem')
                        answer_display2.set('')
                        answer_display3.set('')
                    if (dx !=0 or dy !=0 or dz !=0):
                        answer_display1.set('Vo nghiem')
                        answer_display2.set('')
                        answer_display3.set('')
                else:
                    answer_display1.set('x='+str(dx/d))
                    answer_display2.set('y='+str(-dy/d))
                    answer_display3.set('z='+str(dz/d))
            except:
                answer_display1.set('Error')
                answer_display2.set('Error')
                answer_display3.set('Error')
        def ClickA1(numbers):
            global operator
            operator += str(numbers)
            A1.set(operator)
        def ClickA2(numbers):
            global operator
            operator += str(numbers)
            A2.set(operator)
        def ClickA3(numbers):
            global operator
            operator += str(numbers)
            A3.set(operator)
        def ClickB1(numbers):
            global operator
            operator += str(numbers)
            B1.set(operator)
        def ClickB2(numbers):
            global operator
            operator += str(numbers)
            B2.set(operator)
        def ClickB3(numbers):
            global operator
            operator += str(numbers)
            B3.set(operator)
        def ClickC1(numbers):
            global operator
            operator += str(numbers)
            C1.set(operator)
        def ClickC2(numbers):
            global operator
            operator += str(numbers)
            C2.set(operator)
        def ClickC3(numbers):
            global operator
            operator += str(numbers)
            C3.set(operator)
        def ClickD1(numbers):
            global operator
            operator += str(numbers)
            D1.set(operator)
        def ClickD2(numbers):
            global operator
            operator += str(numbers)
            D2.set(operator)
        def ClickD3(numbers):
            global operator
            operator += str(numbers)
            D3.set(operator)
    def Cramer_4():
        cramer = Toplevel()
        cramer.title('Simul 4')
        cramer.configure(background='black')
        operator = ''
        answer_display1,answer_display2,answer_display3,answer_display4 = StringVar(),StringVar(),StringVar(),StringVar()
        A1,A2,A3,A4,B1,B2,B3,B4 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        C1,C2,C3,C4,D1,D2,D3,D4 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        E1,E2,E3,E4 = StringVar(),StringVar(),StringVar(),StringVar()
        cramer_label1 = Label(cramer,padx=10,text='x',font=('arial',20),bg='black',fg='white').grid(row=0,column=0)
        cramer_display1 = Entry(cramer, width=15, font=('arial', 20), textvariable=answer_display1,
                                    bd=10, insertwidth=6 , justify='right').grid(row=0, column=1,columnspan=2)
        cramer_label2 = Label(cramer,padx=10,text='y',font=('arial',20),bg='black',fg='white').grid(row=1,column=0)
        cramer_display2 = Entry(cramer, width=15, font=('arial', 20), textvariable=answer_display2,
                                    bd=10, insertwidth=6, justify='right').grid(row=1, column=1,columnspan=2)
        cramer_label3 = Label(cramer,padx=10,text='z',font=('arial',20),bg='black',fg='white').grid(row=0,column=3)
        cramer_display3 = Entry(cramer, width=15, font=('arial', 20), textvariable=answer_display3,
                                    bd=10, insertwidth=6, justify='right').grid(row=0, column=4,columnspan=2)
        cramer_label4 = Label(cramer,padx=10,text='t',font=('arial',20),bg='black',fg='white').grid(row=1,column=3)
        cramer_display4 = Entry(cramer, width=15, font=('arial', 20), textvariable=answer_display4,
                                    bd=10, insertwidth=6, justify='right').grid(row=1, column=4,columnspan=2)
        label_a1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A1', bg='black',
                         command=lambda: ClickA1('')).grid(row=4, column=0)
        input_a1 = Entry(cramer, textvariable=A1, width=4, font=('arial', 20), bd=1, justify='right')
        input_a1.grid(row=4, column=1)
        label_b1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B1', bg='black',
                         command=lambda: ClickB1('')).grid(row=4, column=2)
        input_b1 = Entry(cramer, textvariable=B1, width=4, font=('arial', 20), bd=1, justify='right')
        input_b1.grid(row=4, column=3)
        label_c1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C1', bg='black',
                         command=lambda: ClickC1('')).grid(row=4, column=4)
        input_c1 = Entry(cramer, textvariable=C1, width=4, font=('arial', 20), bd=1, justify='right')
        input_c1.grid(row=4, column=5)
        label_d1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D1', bg='black',
                         command=lambda: ClickD1('')).grid(row=4, column=6)
        input_d1 = Entry(cramer, textvariable=D1, width=4, font=('arial', 20), bd=1, justify='right')
        input_d1.grid(row=4, column=7)
        label_e1 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='E1', bg='black',
                         command=lambda: ClickE1('')).grid(row=4, column=8)
        input_e1 = Entry(cramer, textvariable=E1, width=4, font=('arial', 20), bd=1, justify='right')
        input_e1.grid(row=4, column=9)
        label_a2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A2', bg='black',
                         command=lambda: ClickA2('')).grid(row=5, column=0)
        input_a2 = Entry(cramer, textvariable=A2, width=4, font=('arial', 20), bd=1, justify='right')
        input_a2.grid(row=5, column=1)
        label_b2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B2', bg='black',
                         command=lambda: ClickB2('')).grid(row=5, column=2)
        input_b2 = Entry(cramer, textvariable=B2, width=4, font=('arial', 20), bd=1, justify='right')
        input_b2.grid(row=5, column=3)
        label_c2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C2', bg='black',
                         command=lambda: ClickC2('')).grid(row=5, column=4)
        input_c2 = Entry(cramer, textvariable=C2, width=4, font=('arial', 20), bd=1, justify='right')
        input_c2.grid(row=5, column=5)
        label_d2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D2', bg='black',
                         command=lambda: ClickD2('')).grid(row=5, column=6)
        input_d2 = Entry(cramer, textvariable=D2, width=4, font=('arial', 20), bd=1, justify='right')
        input_d2.grid(row=5, column=7)
        label_e2 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='E2', bg='black',
                         command=lambda: ClickE2('')).grid(row=5, column=8)
        input_e2 = Entry(cramer, textvariable=E2, width=4, font=('arial', 20), bd=1, justify='right')
        input_e2.grid(row=5, column=9)
        label_a3 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A3', bg='black',
                         command=lambda: ClickA3('')).grid(row=6, column=0)
        input_a3 = Entry(cramer, textvariable=A3, width=4, font=('arial', 20), bd=1, justify='right')
        input_a3.grid(row=6, column=1)
        label_b3 =  Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B3', bg='black',
                         command=lambda: ClickB3('')).grid(row=6, column=2)
        input_b3 = Entry(cramer, textvariable=B3, width=4, font=('arial', 20), bd=1, justify='right')
        input_b3.grid(row=6, column=3)
        label_c3 =  Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C3', bg='black',
                         command=lambda: ClickC3('')).grid(row=6, column=4)
        input_c3 = Entry(cramer, textvariable=C3, width=4, font=('arial', 20), bd=1, justify='right')
        input_c3.grid(row=6, column=5)
        label_d3 =  Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D3', bg='black',
                         command=lambda: ClickD3('')).grid(row=6, column=6)
        input_d3 = Entry(cramer, textvariable=D3, width=4, font=('arial', 20), bd=1 ,justify='right')
        input_d3.grid(row=6, column=7)
        label_e3 =  Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='E3', bg='black',
                         command=lambda: ClickE3('')).grid(row=6, column=8)
        input_e3 = Entry(cramer, textvariable=E3, width=4, font=('arial', 20), bd=1, justify='right')
        input_e3.grid(row=6, column=9)
        label_a4 =  Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='A4', bg='black',
                         command=lambda: ClickA4('')).grid(row=7, column=0)
        input_a4 = Entry(cramer, textvariable=A4, width=4, font=('arial', 20), bd=1, justify='right')
        input_a4.grid(row=7, column=1)
        label_b4 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='B4', bg='black',
                         command=lambda: ClickB4('')).grid(row=7, column=2)
        input_b4 = Entry(cramer, textvariable=B4, width=4, font=('arial', 20), bd=1, justify='right')
        input_b4.grid(row=7, column=3)
        label_c4 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='C4', bg='black',
                         command=lambda: ClickC4('')).grid(row=7, column=4)
        input_c4 = Entry(cramer, textvariable=C4, width=4, font=('arial', 20), bd=1, justify='right')
        input_c4.grid(row=7, column=5)
        label_d4 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='D4', bg='black',
                         command=lambda: ClickD4('')).grid(row=7, column=6)
        input_d4 = Entry(cramer, textvariable=D4, width=4, font=('arial', 20), bd=1, justify='right')
        input_d4.grid(row=7, column=7)
        label_e4 = Button(cramer, padx=10, bd=0, fg='white', font=('arial', 20), text='E4', bg='black',
                         command=lambda: ClickE4('')).grid(row=7, column=8)
        input_e4 = Entry(cramer, textvariable=E4, width=4, font=('arial', 20), bd=1 ,justify='right')
        input_e4.grid(row=7, column=9)
        ans = Button(cramer, padx=20, text='Answer', font=('arial', 20), fg='white', bg='black',command=lambda: Check_cramer4()).grid(row=1, column=7,columnspan=3)
        def Check_cramer4():
            try:
                a1 = float(input_a1.get())
                a2 = float(input_a2.get())
                a3 = float(input_a3.get())
                a4 = float(input_a4.get())
                b1 = float(input_b1.get())
                b2 = float(input_b2.get())
                b3 = float(input_b3.get())
                b4 = float(input_b4.get())
                c1 = float(input_c1.get())
                c2 = float(input_c2.get())
                c3 = float(input_c3.get())
                c4 = float(input_c4.get())
                d1 = float(input_d1.get())
                d2 = float(input_d2.get())
                d3 = float(input_d3.get())
                d4 = float(input_d4.get())
                e1 = float(input_e1.get())
                e2 = float(input_e2.get())
                e3 = float(input_e3.get())
                e4 = float(input_e4.get())
                h = np.array([[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3],[a4,b4,c4,d4]])
                hx= np.array([[b1,c1,d1,e1],[b2,c2,d2,e2],[b3,c3,d3,e3],[b4,c4,d4,e4]])
                hy= np.array([[a1,c1,d1,e1],[a2,c2,d2,e2],[a3,c3,d3,e3],[a4,c4,d4,e4]])
                hz= np.array([[a1,b1,d1,e1],[a2,b2,d2,e2],[a3,b3,d3,e3],[a4,b4,d4,e4]])
                ht= np.array([[a1,b1,c1,e1],[a2,b2,c2,e2],[a3,b3,c3,e3],[a4,b4,c4,e4]])
                d = np.linalg.det(h)
                dx= np.linalg.det(hx)
                dy= np.linalg.det(hy)
                dz= np.linalg.det(hz)
                dt= np.linalg.det(ht)
                if (d==0):
                    if (dx==0 and dy==0 and dz==0 and dt==0):
                        answer_display1.set('Vo so nghiem')
                        answer_display2.set('')
                        answer_display3.set('')
                        answer_display4.set('')
                    else:
                        answer_display1.set('Vo nghiem')
                        answer_display2.set('')
                        answer_display3.set('')
                        answer_display4.set('')
                else:
                    answer_display1.set('x='+str(-dx/d))
                    answer_display2.set('y='+str(dy/d))
                    answer_display3.set('z='+str(-dz/d))
                    answer_display4.set('t='+str(dt/d))
            except:
                answer_display1.set('Error')
                answer_display2.set('Error')
                answer_display3.set('Error')
                answer_display4.set('Error')
        def ClickA1(numbers):
            global operator
            operator += str(numbers)
            A1.set(operator)
        def ClickA2(numbers):
            global operator
            operator += str(numbers)
            A2.set(operator)
        def ClickA3(numbers):
            global operator
            operator += str(numbers)
            A3.set(operator)
        def ClickA4(numbers):
            global operator
            operator += str(numbers)
            A4.set(operator)
        def ClickB1(numbers):
            global operator
            operator += str(numbers)
            B1.set(operator)
        def ClickB2(numbers):
            global operator
            operator += str(numbers)
            B2.set(operator)
        def ClickB3(numbers):
            global operator
            operator += str(numbers)
            B3.set(operator)
        def ClickB4(numbers):
            global operator
            operator += str(numbers)
            B4.set(operator)
        def ClickC1(numbers):
            global operator
            operator += str(numbers)
            C1.set(operator)
        def ClickC2(numbers):
            global operator
            operator += str(numbers)
            C2.set(operator)
        def ClickC3(numbers):
            global operator
            operator += str(numbers)
            C3.set(operator)
        def ClickC4(numbers):
            global operator
            operator += str(numbers)
            C4.set(operator)
        def ClickD1(numbers):
            global operator
            operator += str(numbers)
            D1.set(operator)
        def ClickD2(numbers):
            global operator
            operator += str(numbers)
            D2.set(operator)
        def ClickD3(numbers):
            global operator
            operator += str(numbers)
            D3.set(operator)
        def ClickD4(numbers):
            global operator
            operator += str(numbers)
            D4.set(operator)
        def ClickE1(numbers):
            global operator
            operator += str(numbers)
            E1.set(operator)
        def ClickE2(numbers):
            global operator
            operator += str(numbers)
            E2.set(operator)
        def ClickE3(numbers):
            global operator
            operator += str(numbers)
            E3.set(operator)
        def ClickE4(numbers):
            global operator
            operator += str(numbers)
            E4.set(operator)
    def Poly2():
        poly = Toplevel()
        poly.title('Polynomial 2')
        poly.configure(background='black')
        answer_display1 = StringVar()
        answer_display2 = StringVar()
        A = StringVar()
        B = StringVar()
        C = StringVar()
        poly_display_1 = Entry(poly, width=30, font=('arial', 20), textvariable=answer_display1,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=5)

        poly_display_2 = Entry(poly, width=30, font=('arial', 20), textvariable=answer_display2,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=5)

        label_a = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='A', bg='black',
                         command=lambda: ClickA('')).grid(row=2, column=0)
        input_a = Entry(poly,textvariable=A, width=4, font=('arial',20), bd=1, justify='right')
        input_a.grid(row=3, column=0)

        label_b = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='B', bg='black',
                         command=lambda: ClickB('')).grid(row=2, column=1)
        input_b = Entry(poly, textvariable=B, width=4, font=('arial',20), bd=1, justify='right')
        input_b.grid(row=3, column=1)

        label_c = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='C', bg='black',
                         command=lambda: ClickC('')).grid(row=2, column=2)
        input_c = Entry(poly, textvariable=C, width=4, font=('arial',20), bd=1, justify='right')
        input_c.grid(row=3, column=2)
        ans = Button(poly, padx=20, text='Answer', font=('arial',20),fg='white',bg='black', command=lambda:Check_poly()).grid(row=3,column=4,columnspan=2)
        def Check_poly():
            global operator
            try:
                a = float(input_a.get())
                b = float(input_b.get())
                c = float(input_c.get())
                if (a == 0):
                    if (b == 0):
                        if (c == 0):
                            answer_display1.set('Vo so nghiem')
                            answer_display2.set('')
                        else:
                            answer_display1.set('Vo nghiem')
                            answer_display2.set('')
                    else:
                        answer_display1.set('Nghiem duy nhat')
                        answer_display2.set(-b/a)
                else:
                    delta = b**2 - 4*a*c
                    if (delta == 0):
                        answer_display1.set('Nghiem kep')
                        answer_display2.set(-b/(2*a))
                    if (delta >  0):
                        answer_display1.set((-b + sqrt(delta))/(2*a))
                        answer_display2.set((-b - sqrt(delta))/(2*a))
                    if (delta <  0):
                        answer_display1.set(complex(-b / (2 * a), ((np.sqrt(abs(delta))) / (2 * a))))
                        answer_display2.set(complex(-b / (2 * a),-((np.sqrt(abs(delta))) / (2 * a))))
            except:
                answer_display1.set('Error')
                answer_display2.set('')
        def ClickA(numbers):
            global operator
            operator += str(numbers)
            A.set(operator)
        def ClickB(numbers):
            global operator
            operator += str(numbers)
            B.set(operator)
        def ClickC(numbers):
            global operator
            operator += str(numbers)
            C.set(operator)
    def Poly3():
        poly = Toplevel()
        poly.title('Polynomial 3')
        poly.configure(background='black')
        answer_display1 = StringVar()
        answer_display2 = StringVar()
        answer_display3 = StringVar()
        A = StringVar()
        B = StringVar()
        C = StringVar()
        D = StringVar()
        poly_display_1 = Entry(poly, width=30, font=('arial', 20), textvariable=answer_display1,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=5)

        poly_display_2 = Entry(poly, width=30, font=('arial', 20), textvariable=answer_display2,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=5)
        poly_display_3 = Entry(poly, width=30, font=('arial', 20), textvariable=answer_display3,
                               bd=10, insertwidth=6, bg='white', justify='right').grid(columnspan=5)
        label_a = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='A', bg='black',
                         command=lambda: ClickA('')).grid(row=3, column=0)
        input_a = Entry(poly, textvariable=A, width=4, font=('arial', 20), bd=1, fg='white', bg='black',
                        justify='right')
        input_a.grid(row=4, column=0)

        label_b = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='B', bg='black',
                         command=lambda: ClickB('')).grid(row=3, column=1)
        input_b = Entry(poly, textvariable=B, width=4, font=('arial', 20), bd=1, fg='white', bg='black',
                        justify='right')
        input_b.grid(row=4, column=1)

        label_c = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='C', bg='black',
                         command=lambda: ClickC('')).grid(row=3, column=2)
        input_c = Entry(poly, textvariable=C, width=4, font=('arial', 20), bd=1, fg='white', bg='black',
                        justify='right')
        input_c.grid(row=4, column=2)

        label_d = Button(poly, padx=10, bd=0, fg='white', font=('arial', 20), text='D', bg='black',
                         command=lambda: ClickD('')).grid(row=3, column=3)
        input_d = Entry(poly, textvariable=D, width=4, font=('arial', 20), bd=1, fg='white', bg='black',
                        justify='right')
        input_d.grid(row=4, column=3)
        ans = Button(poly, padx=20, text='Answer', font=('arial', 20), fg='white', bg='black',
                     command=lambda: Check_poly3()).grid(row=4, column=4)

        def Check_poly3():
            global operator
            try:
                a = float(input_a.get())
                b = float(input_b.get())
                c = float(input_c.get())
                d = float(input_d.get())
                if (a == 0):
                    if (b == 0):
                        if (c == 0):
                            if (d == 0):
                                answer_display1.set('Vo so nghiem')
                                answer_display2.set('')
                                answer_display3.set('')
                            else:
                                answer_display1.set('Vo nghiem')
                                answer_display2.set('')
                                answer_display3.set('')
                        else:
                            answer_display1.set('Suy bien ve bac 1')
                            answer_display2.set('Nghiem duy nhat')
                            answer_display3.set('x='+str(-d/c))
                    else:
                        delta1 = c ** 2 - 4 * b * d
                        if (delta1 == 0):
                            answer_display1.set('Suy bien ve bac 1')
                            answer_display2.set('Nghiem kep')
                            answer_display3.set('x='+str(-c/(2 * b)))
                        if (delta1 > 0):
                            answer_display1.set('Suy bien ve bac 2')
                            answer_display2.set((-c + sqrt(delta1)) / (2 * b))
                            answer_display3.set((-c - sqrt(delta1)) / (2 * b))
                        if (delta1 < 0):
                            answer_display1.set('Suy bien ve bac 2')
                            answer_display2.set(complex(-c / (2 * b), ((sqrt(abs(delta1))) / (2 * b))))
                            answer_display3.set(complex(-c / (2 * b), -((sqrt(abs(delta1))) /(2 * b))))
                else:
                    delta = b ** 2 - 3 * a * c
                    k = (9 * a * b * c - 2 * (b ** 3) - 27 * (a ** 2) * d) / (2 * (sqrt((abs(delta)) ** 3)))
                    if delta > 0:
                        if abs(k) <= 1:
                            answer_display1.set('x='+str((2 * sqrt(delta) * cos((acos(k)) / 3) - b) / (3 * a)))
                            answer_display2.set('x='+str((2 * sqrt(delta) * cos((acos(k)) / 3 - (2 * pi / 3)) - b) / (3 * a)))
                            answer_display3.set('x='+str((2 * sqrt(delta) * cos((acos(k)) / 3 + (2 * pi / 3)) - b) / (3 * a)))
                        else:
                            answer_display1.set('Nghiem duy nhat')
                            answer_display2.set(((sqrt(delta)) * abs(k) / (3 * a * k))*((abs(k) + sqrt(k * 2 - 1)) ** (1 / 3) + (abs(k) - sqrt(k ** 2 - 1)) ** (1 / 3)) - (b / (3 * a)))
                            answer_display3.set('')
                    if delta == 0:
                        answer_display1.set('Nghiem boi')
                        answer_display2.set((-b + (b ** 3 - 27 * (a ** 2) * d) ** (1 / 3)) / (3 * a))
                        answer_display3.set('')
                    if delta < 0:
                        answer_display1.set('Nghiem duy nhat')
                        answer_display2.set((sqrt(abs(delta))/(3*a))*(((k+sqrt(k**2+1))**(1/3)) + ((k-sqrt(k**2+1))**(1/3))) - b/(3*a))
            except:
                answer_display1.set('Error')
                answer_display2.set('Error')
                answer_display3.set('Error')
        def ClickA(numbers):
            global operator
            operator += str(numbers)
            A.set(operator)
        def ClickB(numbers):
            global operator
            operator += str(numbers)
            B.set(operator)
        def ClickC(numbers):
            global operator
            operator += str(numbers)
            C.set(operator)
        def ClickD(numbers):
            global operator
            operator += str(numbers)
            D.set(operator)
    def Plot():
        plot = Toplevel()
        plot.title("PLot")
        plot.geometry('820x480')
        plot.configure(background='black')
        answer_display = StringVar()
        plot_display = Entry(plot, width=25, font=('arial', 20), textvariable=answer_display,
                             bd=10, insertwidth=6, bg='white', justify='left').grid(row=0, column=0, columnspan=5)
        button_plot = Button(plot, padx=10, bg='black', fg='white', bd=0, text='Plot', font=('arial', 20),
                             command=lambda: plot1()).grid(row=5, column=2, columnspan=3)
        button_nth = Button(plot, padx=10, bd=0, fg='white', bg='black', text='ⁿ√', font=('arial', 20),
                            command=lambda: Click('**(1/')).grid(row=2, column=0)
        button_sqr = Button(plot, padx=10, bd=0, fg='white', bg='black', text='²', font=('arial', 20),
                            command=lambda: Click('**2')).grid(row=2, column=1)
        button_sin1 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='asin', font=('arial', 20),
                             command=lambda: Asin()).grid(row=2, column=2)
        button_cos1 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='acos', font=('arial', 20),
                             command=lambda: Acos()).grid(row=2, column=3)
        button_tan1 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='atan', font=('arial', 20),
                             command=lambda: Atan()).grid(row=2, column=4)
        button_pow = Button(plot, padx=10, bd=0, fg='white', bg='black', text='ⁿ', font=('arial', 20),
                            command=lambda: Click('**')).grid(row=3, column=0)
        button_sqrt = Button(plot, padx=10, bd=0, fg='white', bg='black', text='√', font=('arial', 20),
                             command=lambda: Sqrt()).grid(row=3, column=1)
        button_sin = Button(plot, padx=10, bd=0, fg='white', bg='black', text='sin', font=('arial', 20),
                            command=lambda: Sin()).grid(row=3, column=2)
        button_cos = Button(plot, padx=10, bd=0, fg='white', bg='black', text='cos', font=('arial', 20),
                            command=lambda: Cos()).grid(row=3, column=3)
        button_tan = Button(plot, padx=10, bd=0, fg='white', bg='black', text='tan', font=('arial', 20),
                            command=lambda: Tan()).grid(row=3, column=4)
        button_ln = Button(plot, padx=10, bd=0, fg='white', bg='black', text='ln', font=('arial', 20),
                           command=lambda: Log()).grid(row=4, column=1)
        button_log = Button(plot, padx=10, bd=0, fg='white', bg='black', text='log', font=('arial', 20),
                            command=lambda: Log10()).grid(row=4, column=2)
        button_exp = Button(plot, padx=10, bd=0, fg='white', bg='black', text='exp', font=('arial', 20),
                            command=lambda: Exp()).grid(row=4, column=3)
        button_10 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='10ⁿ', font=('arial', 19),
                           command=lambda: E10()).grid(row=4, column=4)
        button_abs = Button(plot, padx=10, bd=0, fg='white', bg='black', text='abs', font=('arial', 20),
                            command=lambda: Abs()).grid(row=4, column=0)
        button_bracket1 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='(', font=('arial', 20),
                                 command=lambda: Click('(')).grid(row=5, column=0)
        button_bracket2 = Button(plot, padx=10, bd=0, fg='white', bg='black', text=')', font=('arial', 20),
                                 command=lambda: Click(')')).grid(row=5, column=1)
        button7 = Button(plot, padx=10, bd=0, fg='white', font=('arial', 20), text='7', bg='black',
                         command=lambda: Click(7)).grid(row=6, column=0)
        button8 = Button(plot, padx=10, bd=0, fg='white', font=('arial', 20), text='8', bg='black',
                         command=lambda: Click(8)).grid(row=6, column=1)
        button9 = Button(plot, padx=10, bd=0, fg='white', font=('arial', 20), text='9', bg='black',
                         command=lambda: Click(9)).grid(row=6, column=2)
        button_ge = Button(plot, padx=10, bd=0, fg='white', bg='black', text='DEL', font=('arial', 19),
                           command=lambda: GE()).grid(row=6, column=3)
        button_ac = Button(plot, padx=10, bd=0, fg='white', bg='black', text='C', font=('arial', 19),
                           command=lambda: Clear()).grid(row=6, column=4)
        button4 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='4', font=('arial', 20),
                         command=lambda: Click(4)).grid(row=7, column=0)
        button5 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='5', font=('arial', 20),
                         command=lambda: Click(5)).grid(row=7, column=1)
        button6 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='6', font=('arial', 20),
                         command=lambda: Click(6)).grid(row=7, column=2)
        button_mul = Button(plot, padx=10, bd=0, fg='white', bg='black', text='x', font=('arial', 20),
                            command=lambda: Click('*')).grid(row=7, column=3)
        button_div = Button(plot, padx=10, bd=0, fg='white', bg='black', text=chr(247), font=('arial', 20),
                            command=lambda: Click('/')).grid(row=7, column=4)
        button1 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='1', font=('arial', 20),
                         command=lambda: Click(1)).grid(row=8, column=0)
        button2 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='2', font=('arial', 20),
                         command=lambda: Click(2)).grid(row=8, column=1)
        button3 = Button(plot, padx=10, bd=0, fg='white', bg='black', text='3', font=('arial', 20),
                         command=lambda: Click(3)).grid(row=8, column=2)
        button_add = Button(plot, padx=10, bd=0, fg='white', bg='black', text='+', font=('arial', 20),
                            command=lambda: Click('+')).grid(row=8, column=3)
        button_sub = Button(plot, padx=10, bd=0, fg='white', bg='black', text='-', font=('arial', 20),
                            command=lambda: Click('-')).grid(row=8, column=4)
        button0 = Button(plot, padx=10, bd=0, fg='white', bg='black', text="0", font=('arial', 20),
                         command=lambda: Click(0)).grid(row=9, column=0)
        button_ = Button(plot, padx=10, bd=0, fg='white', bg='black', text=".", font=('arial', 20),
                         command=lambda: Click('.')).grid(row=9, column=1)
        button_pi = Button(plot, padx=10, bd=0, fg='white', bg='black', text='π', font=('arial', 20),
                           command=lambda: Click(np.pi)).grid(row=9, column=2)
        button_e = Button(plot, padx=10, bd=0, fg='white', bg='black', text='e', font=('arial', 20),
                          command=lambda: Click(np.e)).grid(row=9, column=3)
        button_x = Button(plot, padx=10, bd=0, fg='white', bg='black', text='x', font=('arial', 20),
                          command=lambda: Click('x')).grid(row=9, column=4)

        def plot1():
            try:
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
                y = str(answer_display.get())
                if 'asin' in y or 'acos'in y or 'atan' in y :
                    X = np.linspace(-1, 1, 100)
                    Y = []
                    for x in X:
                        Y.append(eval(y))
                else:
                    try:
                        X = np.linspace(-50, 50,100)
                        Y = []
                        for x in X:
                            Y.append(eval(y))
                    except:
                        X = np.linspace(0.1, 50, 100)
                        Y = []
                        for x in X:
                            Y.append(eval(y))
                fig = plt.figure(figsize=(4, 4.5))
                plt.plot(X,Y)
                canvas = FigureCanvasTkAgg(fig, master=plot)
                canvas.get_tk_widget().grid(row=0, column=5, rowspan=11, columnspan=10)
                toolbarFrame = Frame(master=plot)
                toolbarFrame.grid(row=0, column=7)
                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid()
            except:
                answer_display.set('Cannot draw with out x variable')
        def Click(numbers):
            global text
            text += str(numbers)
            answer_display.set(text)
        def Clear():
            global text
            text = ''
            answer_display.set('')
        def GE():
            global text
            text = answer_display.get()[:-1]
            answer_display.set(text)
        def Sin():
            global text
            text += str('sin(')
            answer_display.set(text)
        def Cos():
            global text
            text += str('cos(')
            answer_display.set(text)
        def Tan():
            global text
            text += str('tan(')
            answer_display.set(text)
        def Sqrt():
            global text
            text += str('sqrt(')
            answer_display.set(text)
        def Log():
            global text
            text += str('log(')
            answer_display.set(text)
        def Log10():
            global text
            text += ('log10(')
            answer_display.set(text)
        def Abs():
            global text
            text += str('abs(')
            answer_display.set(text)
        def Exp():
            global text
            text += str('exp(')
            answer_display.set(text)
        def E10():
            global text
            text += str('10**(')
            answer_display.set(text)
        def Asin():
            global text
            text += str('asin(')
            answer_display.set(text)
        def Acos():
            global text
            text += str('acos(')
            answer_display.set(text)
        def Atan():
            global text
            text += str('atan(')
            answer_display.set(text)
    def Expa():
        expa = Toplevel()
        expa.title('Simul 1')
        expa.configure(background='black')
        expan,A,B = StringVar(),StringVar(),StringVar()
        label_a = Button(expa, padx=10, bd=0, fg='white', font=('arial', 20), text='Expand', bg='black',
                         command=lambda:expandx()).grid(row=1, column=0)
        input_a = Entry(expa, textvariable=A, width=24, font=('arial', 20), bd=10, bg='white', justify='right')
        input_a.grid(row=1, column=1,columnspan=4)
        label_b = Button(expa, padx=10, bd=0, fg='white', font=('arial', 20), text='Simply', bg='black',
                         command=lambda:symply()).grid(row=2, column=0)
        input_b = Entry(expa, textvariable=B, width=24, font=('arial', 20), bd=10, bg='white', justify='right')
        input_b.grid(row=2, column=1,columnspan=4)
        def symply():
            global operator
            try:
                x = Symbol('x')
                a = eval(text_input.get())
                operator = simplify(a)
                B.set(operator)
            except:
                B.set('Error')
        def expandx():
            global operator
            try:
                x = Symbol('x')
                a = eval(text_input.get())
                operator = expand(a)
                A.set(operator)
            except:
                A.set('Error')
cal = Tk()
cal.configure(background='black')
cal.title('My Calculator')
operator = ""
text = ''
text_input = StringVar()
text_display = Entry(cal,width=24,font=('arial',20),textvariable=text_input,bd=10,insertwidth=4, bg = 'white',justify='left').grid(columnspan=5)

button_per = Button(cal,padx=10, fg='white',bg='black',bd = 0,text='nPr',font=('arial',20),command=lambda:Click('P')).grid(row=1,column=0)
button_der = Button(cal,padx=10, fg='white',bg='black',bd = 0,text='y\'',font=('arial',20),command=lambda:der()).grid(row=1,column=2)
button_com = Button(cal,padx=10, fg='white',bg='black',bd = 0,text='nCr',font=('arial',20),command=lambda:Click("C")).grid(row=1,column=1)
button_ider = Button(cal,padx=10, fg='white',bg='black',bd = 0,text='∫',font=('arial',20),command=lambda:inder()).grid(row=1,column=3)
button_shift = Button(cal,padx=10,bd=0,fg='white',bg='black',text='⇧',font=('arial',20),command=lambda:Shift()).grid(row=1,column=4)

button_sum = Button(cal,padx=10,bd=0,fg='white',bg='black',text='Σ',font=('arial',20),command=lambda:Click('Σ(')).grid(row=2,column=4)
button_m = Button(cal,padx=10,bd=0,fg='white',bg='black',text='π',font=('arial',20),command=lambda:Click('π(')).grid(row=2,column=3)
button_bin = Button(cal,padx=10,bd=0,fg='white',bg='black',text='Bin',font=('arial',20),command=lambda:Click('bin(')).grid(row=2,column=0)
button_hex = Button(cal,padx=10,bd=0,fg='white',bg='black',text='Hex',font=('arial',20),command=lambda:Click('hex(')).grid(row=2,column=1)
button_oct = Button(cal,padx=10,bd=0,fg='white',bg='black',text='Oct',font=('arial',20),command=lambda:Click('oct(')).grid(row=2,column=2)

button_nth = Button(cal,padx=10,bd=0,fg='white',bg='black',text='ⁿ√',font=('arial',20),command=lambda:Click('**(1/')).grid(row=3,column=0)
button_sqr = Button(cal,padx=10,bd=0,fg='white',bg='black',text='²',font=('arial',20),command=lambda:Click('**2')).grid(row=3,column=1)
button_sin1 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='asin',font=('arial',20),command=lambda:Asin()).grid(row=3,column=2)
button_cos1 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='acos',font=('arial',20),command=lambda:Acos()).grid(row=3,column=3)
button_tan1 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='atan',font=('arial',20),command=lambda:Atan()).grid(row=3,column=4)

button_pow = Button(cal,padx=10,bd=0,fg='white',bg='black',text='ⁿ',font=('arial',20),command=lambda:Click('**')).grid(row=4,column=0)
button_sqrt = Button(cal,padx=10,bd=0,fg='white',bg='black',text='√',font=('arial',20),command=lambda:Sqrt()).grid(row=4,column=1)
button_sin = Button(cal,padx=10,bd=0,fg='white',bg='black',text='sin',font=('arial',20),command=lambda:Sin()).grid(row=4,column=2)
button_cos = Button(cal,padx=10,bd=0,fg='white',bg='black',text='cos',font=('arial',20),command=lambda:Cos()).grid(row=4,column=3)
button_tan = Button(cal,padx=10,bd=0,fg='white',bg='black',text='tan',font=('arial',20),command=lambda:Tan()).grid(row=4,column=4)

button_fac = Button(cal,padx=10,bd=0,fg='white',bg='black',text='!',font=('arial',20),command=lambda:Click('!')).grid(row=5,column=0)
button_ln = Button(cal,padx=10,bd=0,fg='white',bg='black',text='ln',font=('arial',20),command=lambda:Log()).grid(row=5,column=1)
button_log = Button(cal,padx=10,bd=0,fg='white',bg='black',text='log',font=('arial',20),command=lambda:Log10()).grid(row=5,column=2)
button_exp = Button(cal,padx=10,bd=0,fg='white',bg='black',text='exp',font=('arial',20),command=lambda:Exp()).grid(row=5,column=3)
button_10 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='10ⁿ',font=('arial',19),command=lambda:E10()).grid(row=5,column=4)

button_abs = Button(cal,padx=10,bd=0,fg='white',bg='black',text='|x|',font=('arial',20),command=lambda:Abs()).grid(row=6,column=0)
button_bracket1 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='(',font=('arial',20),command=lambda:Click('(')).grid(row=6,column=1)
button_bracket2 = Button(cal,padx=10,bd=0,fg='white',bg='black',text=')',font=('arial',20),command=lambda:Click(')')).grid(row=6,column=2)
button_x = Button(cal,padx=10, fg='white',bg='black',bd = 0,text='x',font=('arial',20),command=lambda:Click('x')).grid(row=6,column=3)
button_per = Button(cal,padx=10,bd=0,fg='white',bg='black',text='%',font=('arial',20),command=lambda:Click('*0.01')).grid(row=6,column=4)

button7 = Button(cal,padx=10,bd=0,fg='white',font=('arial',20),text='7',bg='black',command=lambda:Click(7)).grid(row=7,column=0)
button8 = Button(cal,padx=10,bd=0,fg='white',font=('arial',20),text='8',bg='black',command=lambda:Click(8)).grid(row=7,column=1)
button9 = Button(cal,padx=10,bd=0,fg='white',font=('arial',20),text='9',bg='black',command=lambda:Click(9)).grid(row=7,column=2)
button_ge = Button(cal,padx=10,bd=0,fg='white',bg='black',text='DEL',font=('arial',19),command=lambda:GE()).grid(row=7,column=3)
button_ac = Button(cal,padx=10,bd=0,fg='white',bg='black',text='C',font=('arial',19),command=lambda:Clear()).grid(row=7,column=4)

button4 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='4',font=('arial',20),command=lambda:Click(4)).grid(row=8,column=0)
button5 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='5',font=('arial',20),command=lambda:Click(5)).grid(row=8,column=1)
button6 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='6',font=('arial',20),command=lambda:Click(6)).grid(row=8,column=2)
button_mul = Button(cal,padx=10,bd=0,fg='white',bg='black',text='x',font=('arial',20),command=lambda:Click('*')).grid(row=8,column=3)
button_div = Button(cal,padx=10,bd=0,fg='white',bg='black',text=chr(247),font=('arial',20),command=lambda:Click('/')).grid(row=8,column=4)

button1 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='1',font=('arial',20),command=lambda:Click(1)).grid(row=9,column=0)
button2 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='2',font=('arial',20),command=lambda:Click(2)).grid(row=9,column=1)
button3 = Button(cal,padx=10,bd=0,fg='white',bg='black',text='3',font=('arial',20),command=lambda:Click(3)).grid(row=9,column=2)
button_add = Button(cal,padx=10,bd=0,fg='white',bg='black',text='+',font=('arial',20),command=lambda:Click('+')).grid(row=9,column=3)
button_sub = Button(cal,padx=10,bd=0,fg='white',bg='black',text='-',font=('arial',20),command=lambda:Click('-')).grid(row=9,column=4)

button0 = Button(cal,padx=10,bd=0,fg='white',bg='black',text="0",font=('arial',20),command=lambda:Click(0)).grid(row=10,column=0)
button_ = Button(cal,padx=10,bd=0,fg='white',bg='black',text=".",font=('arial',20),command=lambda:Click('.')).grid(row=10,column=1)
button_pi = Button(cal,padx=10,bd=0,fg='white',bg='black',text='𝞹',font=('arial',20),command=lambda:Click(np.pi)).grid(row=10,column=2)
button_e = Button(cal,padx=10,bd=0,fg='white',bg='black',text='e',font=('arial',20),command=lambda:Click(np.e)).grid(row=10,column=3)
button_equal = Button(cal,padx=10,bd=0,fg='white',bg='black',text='=' ,font=('arial',19),command=lambda:Equal()).grid(row=10,column=4)

cal.mainloop()