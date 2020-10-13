from tkinter import *
root = Tk()
root.title('Calculator')
label01 = Label(root, text = 'CASIO', width = 5, height = 3)
label01.grid(row = 0, column = 0)
e = Entry(root, borderwidth = 10)
e.grid(row = 0,column = 1)

label1 = Label(root)
label1.grid(row = 1, column = 0)

n7 = Button(root, text = 7, width = 5, height = 3, borderwidth = 5)
n7.grid(row = 2 ,column = 0)
n8 = Button(root, text = 8, width = 5, height = 3, borderwidth = 5)
n8.grid(row = 2,column = 1)
n9 = Button(root, text = 9, width = 5, height = 3, borderwidth = 5)
n9.grid(row = 2,column = 2)
n4 = Button(root, text = 4, width = 5, height = 3, borderwidth = 5)
n4.grid(row = 4,column = 0)
n5 = Button(root, text = 5, width = 5, height = 3, borderwidth = 5)
n5.grid(row = 4,column = 1)
n6 = Button(root, text = 6, width = 5, height = 3, borderwidth = 5)
n6.grid(row = 4,column = 2)
n1 = Button(root, text = 1, width = 5, height = 3, borderwidth = 5)
n1.grid(row = 6,column = 0)
n2 = Button(root, text = 2, width = 5, height = 3, borderwidth = 5)
n2.grid(row = 6,column = 1)
n3 = Button(root, text = 3, width = 5, height = 3, borderwidth = 5)
n3.grid(row = 6,column = 2)
n0 = Button(root, text = 0, width = 5, height = 3, borderwidth = 5)
n0.grid(row = 8,column = 0)
ncls = Button(root, text = 'Clear', width = 25, height = 3, borderwidth = 5)
ncls.grid(row = 8,column = 1, columnspan = 5)
nplus = Button(root, text = '+', width = 5, height = 3, borderwidth = 5)
nplus.grid(row = 10,column = 0)
nequal = Button(root, text = '=', width = 25, height = 3, borderwidth = 5)
nequal.grid(row = 10,column = 1, columnspan = 5)


label00 = Label(root)
label00.grid(row = 3, column = 0)
label2 = Label(root)
label2.grid(row = 5, column = 0)
label3 = Label(root)
label3.grid(row = 7, column = 0)
label4 = Label(root)
label4.grid(row = 9, column = 0)



root.mainloop()

# label1 = Label(root, text = 'Entername')
# label1.grid(row = 0, column = 0)
# e = Entry(root, borderwidth = 10)
# e.grid(row = 0,column = 1)
# def gettext():
# 	data = e.get()
# 	label0 = Label(root, text = 'How are you ' +data)
# 	label0.grid(row = 1, column = 1)
# 	e.delete()

# button1 = Button(root, text = 'Submit', width = 19, command = gettext)
# button1.grid(row = 3, column = 1)


# root.mainloop()



# def press(num):
# 	global expression
# 	expression = expression + str(num)
# 	equation.set(expression)

# def equalpress():
# 	try:
# 		global expression
# 		total = str(eval(expression))
# 		equation.set(total)
# 		expression = ''

# def insert():
# 	data = e.insert()
# 	label0 = Label(root, text = data)
# 	label0.grid(row = 1, column = 1)
# 	e.delete()



# label1 = Label(root, text = 'Entername')
# label1.grid(row = 0, column = 0)
# e = Entry(root, borderwidth = 10)
# e.grid(row = 0,column = 1)
# def gettext():
# 	data = e.get()
# 	label0 = Label(root, text = 'Hello ' +data)
# 	label0.grid(row = 1, column = 1)
# 	e.delete()

# button1 = Button(root, text = 'Submit', width = 19, command = gettext)
# button1.grid(row = 3, column = 1)

# label1 = Label(root, text = 'Input a number')
# label1.grid(row = 0, column = 0)
# e = Entry(root, borderwidth = 10)
# e.grid(row = 0, column = 1)
# def gettext():
# 	data = e.get()
# 	label0 = Label(root, text = 500* int(data))
# 	label0.grid(row = 1, column = 1)




# button1 = Button(root, text = 'Submit', width = 19, command = gettext)
# button1.grid(row = 3, column = 1)

# label1 = Label(root)
# label1.grid(row = 2, column = 1)


# root.mainloop()




# label1 = Label(root)
# label1.grid(row = 2, column = 1)



# root.mainloop()




# label1 = Label(root, text = 'my_first_gui', bg = 'red', fg = 'white' )
# label2 = Label(root, text = 'my_second_gui', bg = 'black', fg = 'red')
# label1.grid(row = 0, column = 1)
# label2.grid(row = 0, column = 2)
# button1 = Button(root, text = 'my_button', padx = 10, pady = 5, width = 10, borderwidth = 5, bg = 'blue', fg = 'white') 
# button1.grid(row = 2, column = 0)
# label3 = Label(root)
# label3.grid(row = 1, column = 0)
# e = Entry(root, borderwidth = 10)
# e.grid(row = 0,column = 0)


# root.mainloop()
