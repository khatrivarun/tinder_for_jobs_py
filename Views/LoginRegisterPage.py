from tkinter import *


class LoginRegister(Frame):
    def __init__(self, master, widthW, heightH):
        super().__init__()
        self.widthW = widthW
        self.heightH = heightH
        self.configure(background='black')
        self.pack(fill = 'both', expand = True)
        self.createWidgets()


    def createWidgets(self):
        self.loginFrame = Frame(self, bg = 'green', width = self.widthW/2, height = self.heightH)
        self.loginFrame.grid(row = 0, column = 0)

        self.registerFrame = Frame(self, bg = 'red', width = self.widthW/2, height = self.heightH)
        self.registerFrame.grid(row = 0, column = 1)

        self.grid_columnconfigure(0, uniform = 'g1')
        self.grid_columnconfigure(1, uniform = 'g1')
        # self.login = Button(self.loginFrame, text = 'Login', width = 10, height = 1, bg = '#434343', fg = 'white', activebackground = '#666666')
        # self.login.grid(row = 0, column = 0)


top = Tk()
w, h = top.winfo_screenwidth(), top.winfo_screenheight()
log = LoginRegister(top, w, h)
top.geometry("%dx%d+0+0" % (w, h))
top.mainloop()