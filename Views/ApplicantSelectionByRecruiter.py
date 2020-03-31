from tkinter import *


class SelectApplicant(Frame):
    def __init__(self, recTk):
        recTk.destroy()
        self.selectApplicantTk = Tk()
        self.selectApplicantTk.title("tinder For Jobs")
        w, h = self.selectApplicantTk.winfo_screenwidth(), self.selectApplicantTk.winfo_screenheight()
        self.selectApplicantTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.selectApplicantTk.mainloop()

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        viewJobsFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH * 0.75)
        viewJobsFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='green', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME THREE: Viewing Jobs"""
        viewJobsLabel = Label(viewJobsFrame, text='Applicants for This Job: ', bg='black', fg='white',
                              font=('Chalet New York', 30))
        viewJobsLabel.place(x=457, y=0)

        viewCanvas = Canvas(viewJobsFrame, bg='black', width=self.widthW, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=0, y=85)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=1345, y=2, height=400)

        innerFrame = Frame(viewCanvas, bg='black', width=650, height=250)
        innerFrame.place(x=5, y=10)

        self.sampleList = [{'application': 'value00', 'key01': 'value01'},
                           {'application': 'value10', 'key11': 'value11'},
                           {'application': 'value20', 'key21': 'value21'},
                           {'application': 'value30', 'key31': 'value31'}]
        counter = 0
        frameList = []
        for i in self.sampleList:
            frameList.append(Frame(innerFrame, bg='black', width=self.widthW, bd=1, relief='sunken'))
            frameList[-1].pack()
            keyVar = StringVar(innerFrame, ' ')
            valueVar = StringVar(innerFrame, ' ')
            integer = IntVar(innerFrame)
            for j, k in i.items():
                if j == 'application':
                    keyVar = k

                    Label(frameList[-1], text=keyVar, bg='black', fg='white', width=121, height=5,
                          font=('Chalet New York', 15)).grid(row=0, columnspan=2)

                    Button(frameList[-1], text='Reject', bg='#434343', fg='white',
                           activebackground='#666666', width=20, height=2,
                           command=lambda iteration=counter: self.jobsList(iteration)).grid(row=1, column=0)

                    Button(frameList[-1], text='Accept', bg='#434343', fg='white',
                           activebackground='#666666', width=20, height=2,
                           command=lambda iteration=counter: self.jobsList(iteration)).grid(row=1, column=1)
            counter += 1

        viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
        viewCanvas.update_idletasks()
        viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)


def createSelectApplicant(recTK, dictionary):
    log = SelectApplicant(recTK)

# log = SelectApplicant()
