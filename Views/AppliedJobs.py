from tkinter import *
from Views import JobView
from Controllers.JoinController import JoinController
from Controllers.StateController import *


class AppliedJobs(Frame):
    def __init__(self,jobviewTk):
        #self.join = JoinController()
        #self.applicant_email_id = get_account().email_id
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
        # [{'company_name': 'varun company', 'response': 'Applied', 'job_requirements': 'some requiremets... who cares'}]
        # ESA AAYEGA LIST KE ANDAR DICTIONARY---------------------------------------------------------------------------
        # SAMJHA?!!!!!!!!!!!!

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

        viewCanvas = Canvas(AppliedJobsFrame, bg='black', width=1000, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=200, y=0)

        innerFrame = Frame(viewCanvas, bg='black', width=16, height=250)
        innerFrame.place(x=5, y=10)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=985, y=2, height=400)

        frameList = []
        # ESA AAYEEEGGGAAAA -------------------------------------------------------------------
        my_list = [{'company_name': 'varun company', 'response': 'Applied','job_requirements': 'some requiremets... who cares'},{'company_name': 'vinay company', 'response': 'Accepted',
                    'job_requirements': 'Ethical Hacker'},{'company_name': 'abbas company', 'response': 'Applied',
                    'job_requirements': 'Software Developer'},{'company_name': 'Sri1.0 company', 'response': 'Applied',
                    'job_requirements': 'Bhikhari'},{'company_name': 'Sri2.0 company', 'response': 'Applied',
                    'job_requirements': 'Saras Brother'},{'company_name': 'Daksh company', 'response': 'Applied',
                    'job_requirements': 'fast bowler'}]
        #var_get= self.join.get_applied_jobs(self.applicant_email_id))
        for val in my_list:
            frameList.append(Frame(innerFrame, bg='black', bd=1, relief='sunken'))
            frameList[-1].pack()
            nameVar = f"Company Name: {val['company_name']}"
            statusVar = f"Status: {val['response']}"
            jobdescVar = f"Job Description: {val['job_requirements']}"

            Label(frameList[-1], text=nameVar, bg='black', fg='white', width=90, height=3,font = ('Chalet New York', 15)).grid(row=0, columnspan=2)

            Label(frameList[-1], text=jobdescVar, bg='black', fg='white', width=90, height=3,font = ('Chalet New York', 15)).grid(row=1, columnspan=2)

            Label(frameList[-1], text=statusVar, bg='black', fg='white', width=90, height=3,font = ('Chalet New York', 15)).grid(row=2, columnspan=2)
            viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
            #viewCanvas.create_window(0, 0, anchor='se', window=innerFrame)
            viewCanvas.update_idletasks()
            viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)

    def back(self):
            JobView.jobview(self.appliedjobTk)


def appliedjobs(jobviewTk):
    log = AppliedJobs(jobviewTk)
