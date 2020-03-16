from tkinter import *

class Company():
    def __init__(self,master):
        self.master=master







top = Tk()
top.title("tinder For Jobs")
w, h = top.winfo_screenwidth(), top.winfo_screenheight()
log = LoginRegister(w, h)
top.geometry("%dx%d+0+0" % (w, h))
top.mainloop()
