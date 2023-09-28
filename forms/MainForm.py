import tkinter
from tkinter import filedialog
import os
from tkPDFViewer import tkPDFViewer as pdf


pdfframe = None
# Function to open a new window

image_path = 'Images\Icons\icon_pdf.ico'

def open_main_window():
    window = tkinter.Tk()
    window.title("Main")
    form_bg_color = '#343838'
    window.title("Paper Generator")
    window.iconbitmap(image_path)
    window.geometry('1500x800')
    window.configure(bg=form_bg_color)
    filename =''
    
    def clear_file():
        global pdfframe  
        if pdfframe is not None:           
                pdfframe.destroy()
                print("Deactivated" , filename)


    def browse_file():

        global pdfframe  
        if pdfframe is not None:           
                pdfframe.destroy()
                print("Deactivated" , filename)
                
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select pdf File",
                                          filetypes=(("PDF File",".pdf"),
                                            ("PDF File",".PDF"),
                                            ("All File",".txt"),
                                            ))
        print(filename)
        
        pdfviewer = pdf.ShowPdf()
        pdfframe = pdfviewer.pdf_view(window, pdf_location=open(filename, 'r'), width=150, height=50)   
        pdfframe.pack()
        window.mainloop()
       

    frame = tkinter.Frame(bg=form_bg_color)
    username_label = tkinter.Label(frame, text="File: ", bg=form_bg_color, fg="#ffffff", font=("Arial", 14))
    username_entry = tkinter.Entry(frame, font=("Arial", 14), bg=form_bg_color,fg="#ffffff")
    login_button = tkinter.Button(frame, text="Upload File", bg="#4955e3", fg="#ffffff",command=browse_file, font=("Arial", 12))
    clear_button = tkinter.Button(frame, text="ClearFile", bg="#4955e3", fg="#ffffff",command=clear_file, font=("Arial", 12))
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    login_button.grid(row=1, column=2 ,padx= 20)
    clear_button.grid(row=1, column=3 ,padx= 20)
    frame.pack(padx=0, pady=0)
    window.mainloop()
