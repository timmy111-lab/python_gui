from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Scientific Calculator')
root.iconbitmap('c:\python_gui\logo.ico')
image_one = ImageTk.PhotoImage(Image.open('computer.jpg'))
image_label = Label(root, image = image_one)	
image_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
label01 = Label(root, text = 'CASIO ', width = 5, height = 3)
label01.grid(row = 0, column = 0)
e = Entry(root, borderwidth = 10, width = 50)
e.grid(row = 0,column = 1, columnspan = 5, padx = 10, pady = 30)



def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))
def clear_click():
	e.delete(0, END)

def plus_click():
	global first_num
	global math
	math = 'addition'
	first_num = e.get()
	e.delete(0, END)

def minus_click():
	global first_num
	global math
	math = 'substraction'
	first_num = e.get()
	e.delete(0, END)

def divide_click():
	global first_num 
	global math
	math = 'division'
	first_num = e.get()
	e.delete(0, END)

def mult_click():
	global first_num
	global math
	math = 'multiplication'
	first_num = e.get()
	e.delete(0, END)

def mod_click():
	global first_num
	global math
	math = '%'
	first_num = e.get()
	e.delete(0, END)

def DEL_click():
	e.delete(0)
	e.insert(len(e.text_box.get(str(current) + str(number)))-1)

def pos_click():
	e.eq = False
	e.current = -(float(e.text_box.get(current)))
	e.insert(e.current)

def equal_click():
	second_num = e.get()
	e.delete(0, END)

	if math == 'addition':
		e.insert(0, int(first_num) + int(second_num))

	if math == 'multiplication':
		e.insert(0, int(first_num) * int(second_num))

	if math == 'division':
		e.insert(0, int(first_num) / int(second_num))

	if math == 'substraction':
		e.insert(0, int(first_num) - int(second_num))

	if math == '%':
		e.insert(0, int(first_num) % int(second_num))

	if math == '^':
		e.insert(0, int(first_num) * int(first_num))





btn1 = Button(root, text = 1, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(1))
btn2 = Button(root, text = 2, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(2))
btn3 = Button(root, text = 3, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(3))
btn4 = Button(root, text = 4, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(4))
btn5 = Button(root, text = 5, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(5))
btn6 = Button(root, text = 6, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(6))
btn7 = Button(root, text = 7, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(7))
btn8 = Button(root, text = 8, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(8))
btn9 = Button(root, text = 9, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(9))
btn_0 = Button(root, text = 0, padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(0))
btn_equal = Button(root, text = '=', padx = 55, pady = 40, borderwidth = 5, width = 22, command = equal_click)
btn_clear = Button(root, text = 'clear', padx = 55, pady = 40, borderwidth = 5, width = 22,command = clear_click)
btn_plus = Button(root, text = '+', padx = 55, pady = 40, borderwidth = 5, width = 2, command = plus_click)
btn_minus = Button(root, text = '-', padx = 55, pady = 40, borderwidth = 5, width = 2, command = minus_click)
btn_divide = Button(root, text = '/', padx = 55, pady = 40, borderwidth = 5, width = 2, command = divide_click)
btn_mult = Button(root, text = '*', padx = 55, pady = 40, borderwidth = 5, width = 2, command = mult_click)
btn_hyp = Button(root, text = 'hyp', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('hyp'))
btn_sin = Button(root, text = 'sin', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('sin'))
btn_cos = Button(root, text = 'cos', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('cos'))
btn_tan = Button(root, text = 'tan', padx = 55, pady = 40, borderwidth = 5, width =2, command = lambda: button_click('tan'))
btn_log = Button(root, text = 'log', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('log'))
btn_in = Button(root, text = 'in', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('in'))
btn_dot = Button(root, text = '.', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('.'))
btn_ob = Button(root, text = '(', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('('))
btn_cb = Button(root, text = ')', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click(')'))
btn_del = Button(root, text = 'DEL', padx = 55, pady = 40, borderwidth = 5, width =2, command = DEL_click)
btn_rr = Button(root, text = 'x10^x', padx = 55, pady = 40, borderwidth = 5, width = 2)
btn_r = Button(root, text = '^', padx = 55, pady = 40, borderwidth = 5, width = 2, command = lambda: button_click('^'))
btn_rminus = Button(root, text = 'X^-1', padx = 55, pady = 40, borderwidth = 5, width = 2)
btn_ans = Button(root, text = 'Ans', padx = 53, pady = 40, borderwidth = 5, width = 2)
btn_mod = Button(root, text = '%', padx = 55, pady = 40, borderwidth = 5, width = 2, command = mod_click)
btn_ox = Button(root, text = '1/x', padx = 55, pady = 40, borderwidth = 5, width = 2)
btn_pos = Button(root, text = '+/-', padx = 55, pady = 40, borderwidth = 5, width = 2, command = pos_click)



btn1.grid(row = 3, column = 2)
btn2.grid(row = 3, column = 3)
btn3.grid(row = 3, column = 4)
btn4.grid(row = 2, column = 2)
btn5.grid(row = 2, column = 3)
btn6.grid(row = 2, column = 4)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 1, column = 4)
btn_0.grid(row = 4, column = 3)
btn_equal.grid(row = 5, column = 5, columnspan = 2)
btn_clear.grid(row = 5, column = 3, columnspan = 2)
btn_plus.grid(row = 4, column = 4)
btn_minus.grid(row = 3, column = 5)
btn_divide.grid(row = 1, column = 5)
btn_mult.grid(row = 2, column = 5)
btn_hyp.grid(row = 1, column = 0)
btn_sin.grid(row = 1, column = 1)
btn_cos.grid(row = 2, column = 0)
btn_tan.grid(row = 2, column = 1)
btn_log.grid(row = 3, column = 0)
btn_in.grid(row = 3, column = 1)
btn_dot.grid(row = 4, column = 2)
btn_ob.grid(row = 4, column = 0)
btn_cb.grid(row = 4, column = 1)
btn_del.grid(row = 5, column = 0)
btn_rr.grid(row = 1, column = 6)
btn_r.grid(row = 2, column = 6)
btn_rminus.grid(row = 3, column = 6)
btn_ans.grid(row = 5, column = 2)
btn_mod.grid(row = 5, column = 1)
btn_ox.grid(row = 4, column = 6)
btn_pos.grid(row = 4, column = 5)




root.mainloop()