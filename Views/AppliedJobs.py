from tkinter import *
from Views.JobView import *

class AppliedJobs(Frame):
    def __init__(self,jobviewTk):
        jobviewTk.destroy()
        self.appliedjobTk = Tk()
        self.appliedjobTk.title("tinder For Jobs")
        w, h = self.appliedjobTk.winfo_screenwidth(), self.appliedjobTk.winfo_screenheight()
        self.appliedjobTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='black')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.appliedjobTk.mainloop()

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        AppliedJobsFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH * 0.75)
        AppliedJobsFrame.grid()


        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)


        """FRAME TWO FOR APPLIED JOBS"""

        listNodes = Listbox(AppliedJobsFrame, width=50, height=20, bg='black',fg='white',font=("Chalet New York", 12))
        listNodes.place(x=550,y=0)

        scrollbar = Scrollbar(AppliedJobsFrame,orient="vertical")
        scrollbar.config(command=listNodes.yview)
        scrollbar.place(x=985.5,y=0)

        listNodes.config(yscrollcommand=scrollbar.set)

        for x in range(100):
            listNodes.insert(END, str(x))


def appliedjobs(jobviewTk):
    log = AppliedJobs(jobviewTk)
