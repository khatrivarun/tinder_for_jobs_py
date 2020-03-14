from tkinter import *


class LoginRegister(Frame):
    def __init__(self, widthW, heightH):
        super().__init__()
        self.widthW = widthW
        self.heightH = heightH
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()

    def createWidgets(self):
        """CREATING FRAMES"""
        self.textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        self.textFrame.grid(row=0, column=0, columnspan=2)

        self.loginFrame = Frame(self, bg='black', width=self.widthW / 2 + 1, height=self.heightH * 0.75)
        self.loginFrame.grid(row=1, column=0)

        self.registerFrame = Frame(self, bg='black', width=self.widthW / 2, height=self.heightH * 0.75)
        self.registerFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(self.textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(self.textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO FOR LOGIN"""
        self.login = Button(self.loginFrame, text='Login', width=20, height=2, bg='#434343', fg='white',
                            activebackground='#666666')
        self.login.place(x=(self.widthW / 4) - 75, y=(self.heightH / 4) + 100)

        self.loginTextLabelVetUser = Label(self.loginFrame, text='Veteran User?', bg='black', fg='white',
                                           font=('Chalet New York', 30))
        self.loginTextLabelVetUser.place(x=(self.widthW / 4) - 123, y=100)

        self.loginTextLabelWelBack = Label(self.loginFrame, text='Welcome Back!', bg='black', fg='white',
                                           font=('Chalet New York', 20))
        self.loginTextLabelWelBack.place(x=245, y=175)

        self.loginTextLabelPrompt = Label(self.loginFrame, text='Restart Your Search By Logging In.', bg='black',
                                          fg='white',
                                          font=('Chalet New York', 10))
        self.loginTextLabelPrompt.place(x=235, y=350)

        """FRAME THREE FOR REGISTERING"""
        self.registerTextLabelFreshUser = Label(self.registerFrame, text='Fresher Here?', bg='black', fg='white',
                                                font=('Chalet New York', 30))
        self.registerTextLabelFreshUser.place(x=222, y=100)

        self.registerTextLabelFirstSteps = Label(self.registerFrame, text='Take Your First Step!', bg='black',
                                                 fg='white',
                                                 font=('Chalet New York', 20))
        self.registerTextLabelFirstSteps.place(x=210, y=175)

        self.registerTextLabelPrompt = Label(self.registerFrame, text='Register Your Details.', bg='black',
                                             fg='white',
                                             font=('Chalet New York', 10))
        self.registerTextLabelPrompt.place(x=277, y=350)

        self.register = Button(self.registerFrame, text='Register', width=20, height=2, bg='#434343', fg='white',
                               activebackground='#666666')
        self.register.place(x=(self.widthW / 4) - 75, y = (self.heightH / 4) + 100)


top = Tk()
top.title("tinder For Jobs")
w, h = top.winfo_screenwidth(), top.winfo_screenheight()
log = LoginRegister(w, h)
top.geometry("%dx%d+0+0" % (w, h))
top.mainloop()
