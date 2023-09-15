from  tkinter import * 

window = Tk()
window.title("First Code Base")

lbl = Label(window, text="Hello There" ,font=("Arial Bold",50))
lbl.grid(column=0, row=0, )

label = Label(
    window,
    text="Hello, Tkinter",
    foreground="Black",  # Set the text color to white
    background="White"  # Set the background color to black
)


button = Button(
    window,
    text="Click me!",
    width=12,
    height=4,
    bg="blue",
    fg="yellow",
)

label.grid(column=1 , row=1)
button.grid(column=0 , row=2)
window.mainloop()