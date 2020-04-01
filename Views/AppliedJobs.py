from tkinter import *
from Views import JobView

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
        BackButton = Button(AppliedJobsFrame, text='Back', width=10, height=1, bg='#434343',
                              fg='white',
                              activebackground='#666666', font=('Chalet New York',),
                              command=self.back)
        BackButton.place(x=5, y=0)

        viewCanvas = Canvas(AppliedJobsFrame, bg='black', width=670, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=450, y=85)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=655, y=2, height=400)

        innerFrame = Frame(viewCanvas, bg='black', width=650, height=250)
        innerFrame.place(x=5, y=10)

        counter = 0
        frameList = []
        my_dict={
            {"company_name": 'string', "response": 'string', "job_requirements": 'string'}
        }
        for val in my_dict:
            frameList.append(Frame(innerFrame, bg='black', bd=1, relief='sunken'))
            frameList[-1].pack()



    def back(self):
        JobView.jobview(self.appliedjobTk)




def appliedjobs(jobviewTk):
    log = AppliedJobs(jobviewTk)
