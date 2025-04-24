from tkinter import *

def click(event):
    text = event.widget.cget('text')
    current = display.get()
    
    if text == "C":
        display.delete(0, END)  
    elif text == "=":
        try:
            result = str(eval(current))  
            display.delete(0, END)
            display.insert(END, result)
        except Exception as e:
            display.delete(0, END)
            display.insert(END, "Error")  
    else:
        display.insert(END, text)  

window=Tk()
window.title("Calculator")

display= Entry(window,font=("Arial",25), justify="right")
display.pack(fill=X, padx=20, pady=20,ipady=10)

btn_frame = Frame(window)
btn_frame.pack()

button_labels = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0","=","+"
]
i=0
for label in button_labels:
    button=Button(btn_frame, text=label, font=("Arial",18), padx=20, pady=20)
    button.grid(row=i//4, column=i%4, padx=10,pady=10)
    button.bind("<Button-1>", click)  
    i+=1

window.mainloop()