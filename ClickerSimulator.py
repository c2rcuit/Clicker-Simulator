from tkinter import *

totalclicks = 0
soggycat = None
versalink = "https://github.com/c2rcuit/Versa"

def click():
    global totalclicks
    totalclicks += 1
    label.config(text=f"{totalclicks}")
    finishgame()

def clickx2():
    global totalclicks
    totalclicks += 2
    label.config(text=f"{totalclicks}")
    finishgame()

def clickx4():
    global totalclicks
    totalclicks += 8
    label.config(text=f"{totalclicks}")
    finishgame()

def getx2clicks():
    global totalclicks
    if totalclicks >= 100:
        totalclicks -= 100
        button.config(command=clickx2)
        buttonx2.config(command=getx4clicks, text="Click Me To Get X4 Clicks!(300)")
        label.config(text=f"{totalclicks}")
    else:
        print("not enough money")
def getx4clicks():
    global totalclicks
    if totalclicks >= 300:
        totalclicks -= 300
        button.config(command=clickx4)
        buttonx2.config(state=DISABLED,text="",font=("Arial",1))
        label.config(text=f"{totalclicks}")
        finishgame()
    else:
        print("not enough money")

def finishgame():
    global totalclicks, soggycat
    if totalclicks >= 500:
        if soggycat is None:
            soggycat = PhotoImage(file="funnypicture.png")
            label.config(text="Thank You For Playing!")
            button.config(text=f"Go get versa here! {versalink}")
            button.config(fg="black")
            button.config(font=("Arial",30))
            button.config(state=DISABLED)
            buttonx2.config(image=soggycat)
            buttonx2.config(state=DISABLED, text="", font=("Arial", 50))

window = Tk()
window.geometry("1200x1000")
window.title("Clicker Simulator")

button = Button(window,text="Click Me!")
button.config(font=("Arial",50,"bold"))
button.config(command=click)
button.place(relx=0.5, y=70, anchor='n')

buttonx2 = Button(window,text="Click Me To Get X2 Clicks!(100)")
buttonx2.config(font=("Arial",50,))
buttonx2.config(command=getx2clicks)
buttonx2.place(relx=0.5, y=150, anchor='n')

label = Label(window,
              text=f"{totalclicks}",
              font=("Arial",40,"bold"),
              )
label.place(relx=0.5, y=10, anchor='n')

window.mainloop()
