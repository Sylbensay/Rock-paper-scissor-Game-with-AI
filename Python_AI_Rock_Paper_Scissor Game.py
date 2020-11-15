from tkinter import *
import random  

class Rock_paper_scissors(Tk):
    
    def __init__(self):
        super(Rock_paper_scissors, self).__init__()
        self.title("Rock Paper Scissor Game")
        self.rock()
        self.paper()
        self.score_()
        self.scissors()
        self.score = 0
        self.dict_ = ["rock", "paper", "scissors"]

    # buttons for selecting rock 
    def rock(self):
        rock = Button(self,text="Rock",bg='blue')
        rock.bind('<Button-1>', self.Game_rock)
        rock.place(relx=0.3,rely=0,relwidth=0.4)

    # buttons for selecting paper
    def paper(self):
        paper = Button(self,text="Paper",bg='pink')
        paper.bind('<Button-1>', self.Game_paper)
        paper.place(relx=0.3,rely=0.1,relwidth=0.4)

    # buttons for selecting scissors
    def scissors(self):
        scissors = Button(self,text="Scissors",bg='green')
        scissors.bind('<Button-1>', self.Game_scissors)
        scissors.place(relx=0.3,rely=0.2,relwidth=0.4)
        
    #Scoreboards
    def score_(self):
        labelFont = ("Times, 10")
        space = Text(self,font=labelFont,bg='yellow',height=50,width=80).place(relx=0,rely=0.35)

    # Total score text   
    def text_(self):
        labelFont = ("Times, 10")
        text_= "Total Score is {0}".format(self.score)
        space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.3,rely=0.6)

    # win function
    def You_win(self):
            labelFont = ("Times, 15")
            text_= "You win!"
            space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.3,rely=0.4)

    # lose function
    def You_lose(self):
            labelFont = ("Times, 15")
            text_= "You lose!"
            space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.3,rely=0.4)

    # tie function        
    def A_Tie(self):
            labelFont = ("Times, 15")
            text_= " A Tie!"
            space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.3,rely=0.4)

    #AI selecting rock
    def Comp_rock(self):
        labelFont = ("Times, 7")
        text_= "Computer chose Rock!"
        space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.2,rely=0.9)

    #AI selecting paper
    def Comp_paper(self):
        labelFont = ("Times, 7")
        text_= "Computer chose Paper!"
        space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.2,rely=0.9)

    #AI selecting scissors
    def Comp_Scissors(self):
        labelFont = ("Times, 7")
        text_= "Computer chose Scissors!"
        space = Label(self,font=labelFont,bg='yellow',text=text_).place(relx=0.2,rely=0.9)

    #User selecting rock
    def Game_rock(self,event):
        user = "rock"
        comp = random.choice(self.dict_)
        if user > comp:
            self.score -= 1
            self.score_()
            self.text_()
            self.You_lose()
            self.Comp_paper()
        elif user < comp:
            self.score += 1
            self.score_()
            self.text_()
            self.You_win()
            self.Comp_Scissors()
        else:
            self.score += 0
            self.score_()
            self.text_()
            self.A_Tie()
            self.Comp_rock()

    #User selecting paper
    def Game_paper(self,event):
        user = "paper"
        comp = random.choice(self.dict_)
        if user < comp:
            if comp == "rock":
                self.score += 1
                self.score_()
                self.text_()
                self.You_win()
                self.Comp_rock()
            else:
                self.score -= 1
                self.score_()
                self.text_()
                self.You_lose()
                self.Comp_Scissors()        
        elif user == comp:
            self.score += 0
            self.score_()
            self.text_()
            self.A_Tie()
            self.Comp_paper()

    #User selecting scissors       
    def Game_scissors(self,event):
        user = "scissors"
        comp = random.choice(self.dict_)
        if user > comp:
            if comp == "paper":
                self.score += 1
                self.score_()
                self.text_()
                self.You_win()
                self.Comp_paper()
            else:
                self.score -= 1
                self.score_()
                self.text_()
                self.You_lose()
                self.Comp_rock()     
        elif user == comp:
            self.score += 0
            self.score_()
            self.text_()
            self.A_Tie()
            self.Comp_Scissors()

#Play Game
my_gui = Rock_paper_scissors()
my_gui.mainloop()
