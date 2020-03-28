from tkinter import *


class Recruiter(Frame):
    def __init__(self, recLogin):
        recLogin.destroy()
        recruiterTK = Tk()
        recruiterTK.title("tinder For Jobs")
        w, h = recruiterTK.winfo_screenwidth(), recruiterTK.winfo_screenheight()
        recruiterTK.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        recruiterTK.mainloop()

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        createJobFrame = Frame(self, bg='black', width=self.widthW / 2 + 1, height=self.heightH * 0.75)
        createJobFrame.grid(row=1, column=0)

        viewJobsFrame = Frame(self, bg='black', width=self.widthW / 2, height=self.heightH * 0.75)
        viewJobsFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='green', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO: Create Jobs"""

        createJobLabel = Label(createJobFrame, text='Create A Job Listing', bg='black', fg='white',
                               font=('Chalet New York', 30))
        createJobLabel.place(x=155, y=20)

        requirementsLabel = Label(createJobFrame, text='Requirements: ', bg='black', fg='white',
                                  font=('Chalet New York', 15))
        requirementsLabel.place(x=150, y=120)

        self.requirementsEntry = Text(createJobFrame, bg='#434343', fg='white', width=30, height=7)
        self.requirementsEntry.place(x=300, y=126)

        locationLabel = Label(createJobFrame, text='Location: ', bg='black', fg='white',
                              font=('Chalet New York', 15))
        locationLabel.place(x=189, y=244)

        self.locationEntry = Entry(createJobFrame, bg='#434343', fg='white', width=40, show='*')
        self.locationEntry.place(x=300, y=250)

        createJobButton = Button(createJobFrame, text='Create Job', width=20, height=2, bg='#434343', fg='white',
                                 activebackground='#666666')
        createJobButton.place(x=266, y=293)

        """FRAME THREE: Viewing Jobs"""
        viewJobsLabel = Label(viewJobsFrame, text='Created Jobs: ', bg='black', fg='white',
                              font=('Chalet New York', 30))
        viewJobsLabel.place(x=145, y=20)

        viewCanvas = Canvas(viewJobsFrame, bg='black', width=670, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=0, y=85)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=655, y=2, height=400)

        innerFrame = Frame(viewCanvas, bg='black', width=650, height=250)
        innerFrame.place(x=5, y=10)

        for i in range(100):
            Label(innerFrame, text=i, bg='green', fg='white').pack()

        viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
        viewCanvas.update_idletasks()
        viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)


def createRecruiter(recLogin):
    log = Recruiter(recLogin)

# log = Recruiter()
