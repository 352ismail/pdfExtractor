from tkinter import * 

root = Tk()
root.title("Simple Calculator")

textbox = Entry(root , width=20)
textbox.grid( row=0, column=0,columnspan=3 , padx=10,pady=10)


button_1 = Button(root, text="1" ,padx=40, pady=20 )
button_2 = Button(root, text="2" ,padx=40, pady=20 )
button_3 = Button(root, text="3" ,padx=40, pady=20 )
button_4 = Button(root, text="4" ,padx=40, pady=20 )
button_5 = Button(root, text="5" ,padx=40, pady=20 )
button_6 = Button(root, text="6" ,padx=40, pady=20 )
button_7 = Button(root, text="7" ,padx=40, pady=20 )
button_8 = Button(root, text="8" ,padx=40, pady=20 )
button_9 = Button(root, text="9" ,padx=40, pady=20 )
button_0 = Button(root, text="0" ,padx=40, pady=20 )
button_plus = Button(root, text="+" ,padx=40, pady=20 )
button_minus = Button(root, text="-" ,padx=40, pady=20 )

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
# button_plus.grid(row=,column=)
# button_minus.grid(row=,column=)


root.mainloop()
