import pygame
import random
import time
pygame.init()
pygame.font.init()


# This is a class for the pegs
class Pegs:
    def __init__(self,Colour,Xposition,Yposition):
        self.Colour = Colour 
        self.Xposition = Xposition
        self.Yposition = Yposition
    def get_pegColour(self):
        if self.Colour == "white":
            R = 255
            G = 255 
            B = 255
            return R , G , B
        elif self.Colour == "red":
            R = 255
            G = 0
            B = 0
            return R , G , B
        elif self.Colour == "green":
            R = 0
            G = 255 
            B = 0
            return R , G , B
        elif self.Colour == "blue":
            R = 0
            G = 0 
            B = 255
            return R , G , B
        elif self.Colour == "cyan":
            R = 0 
            G = 255
            B = 255
            return R , G , B
        elif self.Colour == "pink":
            R = 255
            G = 0
            B = 255
            return R , G , B
        elif self.Colour == "yellow":
            R = 255
            G = 255
            B = 0 
            return R , G , B
    def get_position(self):
        return self.Xposition , self.Yposition
    def set_pegColour(self,Current_Colour):
        if Current_Colour == (255,255,255):
            self.Colour = "red"
        elif Current_Colour == (255,0,0):
            self.Colour = "green"
        elif Current_Colour == (0,255,0):
            self.Colour = "blue"
        elif Current_Colour == (0,0,255):
            self.Colour = "cyan"
        elif Current_Colour == (0,255,255):
            self.Colour = "pink"
        elif Current_Colour == (255,0,255):
            self.Colour = "yellow"
        elif Current_Colour == (255,255,0):
            self.Colour = "white"
        
class Player:
    def __init__(self,Num_Guesses,Name):
        self.Num_Guesses = Num_Guesses
        self.Name = Name
    def get_Name(self):
        return self.Name
    def get_Num_Guesses(self):
        return self.Num_Guesses
    def set_Num_Guesses(self):
        pass


#assigning the attributes of the pegs
Peg1 = Pegs('white',450,700)
Peg2 = Pegs('white',550,700)
Peg3 = Pegs('white',650,700)
Peg4 = Pegs('white',750,700)
Peg1colour = Peg1.get_pegColour()
indexPeg1 = Peg1.get_position()
Peg2colour = Peg2.get_pegColour()
indexPeg2 = Peg2.get_position()
Peg3colour = Peg3.get_pegColour()
indexPeg3 = Peg3.get_position()
Peg4colour = Peg4.get_pegColour()
indexPeg4 = Peg4.get_position()





#Defining global variables
NumberOfNames = 0 
WinningStatus = False
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
#This defines the screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Start_Screen = 0 
Game_Screen = 1 
Help_Screen = 2 
Win_Screen = 3 
SettingsPage = 4 
Input_Page = 5 
Leaderboard_screen = 6 
Lose_screen = 7 
Game_State = Start_Screen
Num_Guesses_Allowed = 12 
username = ''
resetusername = True
uppercase = False
#loading images
imp = pygame.image.load("C:\Mastermindproject\\download.jpg").convert()
pygame.display.flip()
YouWinImage = pygame.image.load("C:\Mastermindproject\\YouWinImage.png").convert()
YouWinImage2 = pygame.transform.scale(YouWinImage,(400,500))
Start_ScreenIMG = pygame.image.load("C:\Mastermindproject\\StartPageIMG.png").convert()
Start_ScreenIMG2 = pygame.transform.scale(Start_ScreenIMG,(1200,800))
Help_ScreenIMG = pygame.image.load("C:\Mastermindproject\\Help_ScreenIMG.png").convert()
Help_ScreenIMG2 = pygame.transform.scale(Help_ScreenIMG,(1200,800))
New_GameIMG = pygame.image.load("C:\Mastermindproject\\NEWGAME.png").convert()
New_GameIMG1 = pygame.transform.scale(New_GameIMG,(200,80))
HomeButton = pygame.image.load("C:\Mastermindproject\\Homebutton.png").convert()
HomeButton1 = pygame.transform.scale(HomeButton,(200,200))
Settingspage = pygame.image.load("C:\Mastermindproject\\Settingspage.png").convert()
Settingspage2 = pygame.transform.scale(Settingspage,(1200,800))
Namepage = pygame.image.load("C:\Mastermindproject\\Name.png")
NamePage2 = pygame.transform.scale(Namepage,(1200,800))
Leaderboardpage = pygame.image.load("C:\Mastermindproject\\Leaderboard.png")
Leaderboardpage2 = pygame.transform.scale(Leaderboardpage,(1200,800))
Backbutton = pygame.image.load("C:\Mastermindproject\\Back.jpeg")
Backbutton2 = pygame.transform.scale(Backbutton,(200,200))
YouLoseimg = pygame.image.load("C:\Mastermindproject\\GameOver.jpeg")
YouLoseimg2 = pygame.transform.scale(YouLoseimg, (500,500))


run = True
# Generating a new combination and reseting all global variables to their orignal values when a new game is initialised 
def newgame():
    global correct 
    global CombinationPeg1Colour
    global CombinationPeg2Colour
    global CombinationPeg3Colour
    global CombinationPeg4Colour
    global SubmitCount
    global Win_Status
    global New_Game_Status
    global initnewcolours
    global WinningStatus
    global Peg1colour
    global Peg2colour
    global Peg3colour
    global Peg4colour
    Peg1colour = (255,255,255)
    Peg2colour = (255,255,255)
    Peg3colour = (255,255,255)
    Peg4colour = (255,255,255)
    WinningStatus = False
    Win_Status = False
    New_Game_Status = False
    initnewcolours = False
    SubmitCount = 0 
    Colourindex1 = random.randint(1,7)
    Colourindex2 = random.randint(1,7)
    Colourindex3 = random.randint(1,7)
    Colourindex4 = random.randint(1,7)
    if Colourindex1 == 1:
        CombinationPeg1 = Pegs('white',100,100)
    elif Colourindex1 == 2:
        CombinationPeg1 = Pegs('red',100,100)
    elif Colourindex1 == 3:
        CombinationPeg1 = Pegs('green',100,100)
    elif Colourindex1 == 4:
        CombinationPeg1 = Pegs('blue',100,100)
    elif Colourindex1 == 5:
        CombinationPeg1 = Pegs('cyan',100,100)
    elif Colourindex1 == 6:
        CombinationPeg1 = Pegs('pink',100,100)
    else:
        CombinationPeg1 = Pegs('yellow',100,100)
    if Colourindex2 == 1:
        CombinationPeg2 = Pegs('white',150,100)
    elif Colourindex2 == 2:
        CombinationPeg2 = Pegs('red',150,100)
    elif Colourindex2 == 3:
        CombinationPeg2 = Pegs('green',150,100)
    elif Colourindex2 == 4:
        CombinationPeg2 = Pegs('blue',150,100)
    elif Colourindex2 == 5:
        CombinationPeg2 = Pegs('cyan',150,100)
    elif Colourindex2 == 6:
        CombinationPeg2 = Pegs('pink',150,100)
    else:
        CombinationPeg2 = Pegs('yellow',150,100)
    if Colourindex3 == 1:
        CombinationPeg3 = Pegs('white',200,100)
    elif Colourindex3 == 2:
        CombinationPeg3 = Pegs('red',200,100)
    elif Colourindex3 == 3:
        CombinationPeg3 = Pegs('green',200,100)
    elif Colourindex3 == 4:
        CombinationPeg3 = Pegs('blue',200,100)
    elif Colourindex3 == 5:
        CombinationPeg3 = Pegs('cyan',200,100)
    elif Colourindex3 == 6:
        CombinationPeg3 = Pegs('pink',200,100)
    else:
        CombinationPeg3 = Pegs('yellow',200,100)
    if Colourindex4 == 1:
        CombinationPeg4 = Pegs('white',250,100)
    elif Colourindex4 == 2:
        CombinationPeg4 = Pegs('red',250,100)
    elif Colourindex4 == 3:
        CombinationPeg4 = Pegs('green',250,100)
    elif Colourindex4 == 4:
        CombinationPeg4 = Pegs('blue',250,100)
    elif Colourindex4 == 5:
        CombinationPeg4 = Pegs('cyan',250,100)
    elif Colourindex4 == 6:
        CombinationPeg4 = Pegs('pink',250,100)
    else:
        CombinationPeg4 = Pegs('yellow',250,100)
    CombinationPeg1Colour = CombinationPeg1.get_pegColour()
    CombinationPeg2Colour = CombinationPeg2.get_pegColour()
    CombinationPeg3Colour = CombinationPeg3.get_pegColour()
    CombinationPeg4Colour = CombinationPeg4.get_pegColour()
    correct = (CombinationPeg1Colour, CombinationPeg2Colour, CombinationPeg3Colour, CombinationPeg4Colour)
    
newgame()
#Comparing the colours to each other
def checkcolours():
    positioncounter = sum(g == c for g, c in zip(guess, correct))
    colourcounter = sum(min(guess.count(c), correct.count(c)) for c in set(correct))
    colourcounter -= positioncounter
    return positioncounter , colourcounter
    
def leaderboard():
    global scorelist
    global namelist

    scorelist = []
    namelist = []
    try:
        scorelist.append(Player1.get_Num_Guesses())
        namelist.append(Player1.get_Name())
    except:
        pass
    try:
        scorelist.append(Player2.get_Num_Guesses())
        namelist.append(Player2.get_Name())
    except:
        pass
    try:
        scorelist.append(Player3.get_Num_Guesses())
        namelist.append(Player3.get_Name())
    except:
        pass
    try:
        scorelist.append(Player4.get_Num_Guesses())
        namelist.append(Player4.get_Name())
    except:
        pass
    try:
        scorelist.append(Player5.get_Num_Guesses())
        namelist.append(Player5.get_Name())
    except:
        pass
    
    #zipping the two togehter so the score after being sorted remains with the same name 
    try: 
        scorelist,namelist = zip(*sorted(zip(scorelist,namelist))) 
    except:
        pass
    
    try:
        Score1 = font3.render(str(scorelist[0]),True , (0,0,0))
        Name1 = font3.render(namelist[0],True , (0,0,0))
        Score2 = font3.render(str(scorelist[1]),True , (0,0,0))
        Name2 = font3.render(namelist[1],True , (0,0,0))
        Score3 = font3.render(str(scorelist[2]),True , (0,0,0))
        Name3 = font3.render(namelist[2],True , (0,0,0))
        Score4 = font3.render(str(scorelist[3]),True , (0,0,0))
        Name4 = font3.render(namelist[3],True , (0,0,0))
        Score5 = font3.render(str(scorelist[4]),True , (0,0,0))
        Name5 = font3.render(namelist[4],True , (0,0,0))
        
    except:
        pass 
    
    if Game_State == Leaderboard_screen:
        try:
            Score1rect = Score1.get_rect() 
            Score1rect.center = (850,200)
            screen.blit(Score1,Score1rect)
            Name1rect = Name1.get_rect()
            Name1rect.center = (400,200)
            screen.blit(Name1,Name1rect)
        except:
            pass
        try:
            Score2rect = Score2.get_rect() 
            Score2rect.center = (850,330)
            screen.blit(Score2,Score2rect)
            Name2rect = Name2.get_rect()
            Name2rect.center = (400,330)
            screen.blit(Name2,Name2rect)
        except:
            pass
        try:
            Score3rect = Score3.get_rect() 
            Score3rect.center = (850,460)
            screen.blit(Score3,Score3rect)
            Name3rect = Name3.get_rect()
            Name3rect.center = (400,460)
            screen.blit(Name3,Name3rect)
        except:
            pass
        try:
            Score4rect = Score4.get_rect() 
            Score4rect.center = (850,590)
            screen.blit(Score4,Score4rect)
            Name4rect = Name4.get_rect()
            Name4rect.center = (400,590)
            screen.blit(Name4,Name4rect)
        except:
            pass
        try:
            Score5rect = Score5.get_rect() 
            Score5rect.center = (850,720)
            screen.blit(Score5,Score5rect)
            Name5rect = Name5.get_rect()
            Name5rect.center = (400,720)
            screen.blit(Name5,Name5rect)
        except:
            pass
        
              

def savescore(name,recentscore):
    if NumberOfNames == 1 :
        global Player1
        Player1 = Player(recentscore,name)
    elif NumberOfNames == 2:
        global Player2
        Player2 = Player(recentscore,name)
    elif NumberOfNames == 3:
        global Player3
        Player3 = Player(recentscore,name)
    elif NumberOfNames == 4:
        global Player4
        Player4 = Player(recentscore,name)
    elif NumberOfNames == 5:
        global Player5
        Player5 = Player(recentscore,name)
    leaderboard()
    
     
        
def displaycheckcolours(numbers):

    for counter in range(0,numbers[0]):
        Xincrement = counter * 20
        pygame.draw.circle(screen,(255,0,0),((1000+Xincrement),SubmittedYposition),10)
    for counter1 in range(0,numbers[1]):
        Xincrement = counter1 * 20
        pygame.draw.circle(screen,(255,255,255),((1000 + Xincrement),(SubmittedYposition - 20)),10)
    
    #checking to see if the code is fully correct and assigning it to a global variable
    if numbers[0] == 4:
        pygame.draw.circle(screen,CombinationPeg1Colour,(450, 630),12)
        pygame.draw.circle(screen,CombinationPeg2Colour,(550, 630),12)
        pygame.draw.circle(screen,CombinationPeg3Colour,(650, 630),12)
        pygame.draw.circle(screen,CombinationPeg4Colour,(750, 630),12)
        time.sleep(3.0)
        global Win_Status
        Win_Status = True
        
        
#function to draw around the selected number of guesses allowed
def drawaroundselected(NumberSelected):
    if NumberSelected == 4:
        pygame.draw.circle(screen,(255,0,0,32),(170,270),18)
    if NumberSelected == 5:
        pygame.draw.circle(screen,(255,0,0,32),(270,270),18)
    if NumberSelected == 6:
        pygame.draw.circle(screen,(255,0,0,32),(370,270),18)
    if NumberSelected == 7:
        pygame.draw.circle(screen,(255,0,0,32),(470,270),18)
    if NumberSelected == 8:
        pygame.draw.circle(screen,(255,0,0,32),(563,270),18)
    if NumberSelected == 9:
        pygame.draw.circle(screen,(255,0,0,32),(655,270),18)
    if NumberSelected == 10:
        pygame.draw.circle(screen,(255,0,0,32),(766,270),18)
    if NumberSelected == 11:
        pygame.draw.circle(screen,(255,0,0,32),(874,270),18)
    if NumberSelected == 12:
        pygame.draw.circle(screen,(255,0,0,32),(991,270),18)

        
    
#getting the writing on the screen 
font1 = pygame.font.SysFont('arial',18, bold=True)
Winning_writing = font1.render("Winning combination:", True, (255,255,255))
textrect = Winning_writing.get_rect()
textrect.center = (200,615)
font2 = pygame.font.SysFont('arial',40,bold=True)
Title = font2.render("MASTERMIND", True, (255,255,255))
Titlerect = Title.get_rect()
Titlerect.center = (600,30)
font3 = pygame.font.SysFont('arial', 26, bold=True)
LosingWriting = font1.render("The correct combination was: ", True , (255,255,255))
LosingWritingrect = LosingWriting.get_rect()
LosingWritingrect.center = (240,630)





while run: 
    #check if it is the Start screen 
    
    if Game_State == Start_Screen:
        screen.fill((0,0,0))
        screen.blit(Start_ScreenIMG2,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            #event button one is the left click
                if event.button == 1:
                    if event.pos[1] > 310 and event.pos[0] > 410 :
                        if event.pos[1] < 480 and event.pos[0]< 795 :
                            Game_State = Game_Screen
                            screen.fill((40,40,40))
                    if event.pos[1] > 555 and event.pos[0] > 490 :
                        if event.pos[1] < 643 and event.pos[0]< 715 :
                            Game_State = Help_Screen
                    if event.pos[1] > 0 and event.pos[0] > 1075 :
                        if event.pos[1] < 125 and event.pos[0]< 1200 :
                            Game_State = SettingsPage

    elif Game_State == Input_Page:
        while resetusername:
            username = ''
            resetusername = False
        screen.blit(NamePage2,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] > 560 and event.pos[0] > 423 :
                        if event.pos[1] < 670 and event.pos[0]< 780 :
                            Game_State = Start_Screen
            elif event.type == pygame.KEYDOWN:
                if uppercase :
                    temp = pygame.key.name(event.key)
                    temp2 = temp.upper()
                    username += temp2
                    uppercase = False 
                elif pygame.key.name(event.key) == 'space':
                    username += ' '
                elif pygame.key.name(event.key) == 'left shift':
                    uppercase = True
                else:
                    username += pygame.key.name(event.key)
                
        
    elif Game_State == Lose_screen:
        screen.blit(New_GameIMG1,(1000,00) )
        screen.blit(YouLoseimg2, (330,200))
        screen.blit(HomeButton1,(1000,600))
        screen.blit(LosingWriting,LosingWritingrect)
        pygame.draw.circle(screen,CombinationPeg1Colour,(450, 630),12)
        pygame.draw.circle(screen,CombinationPeg2Colour,(550, 630),12)
        pygame.draw.circle(screen,CombinationPeg3Colour,(650, 630),12)
        pygame.draw.circle(screen,CombinationPeg4Colour,(750, 630),12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] > 0 and event.pos[0] > 1000 :
                        if event.pos[1] < 200 and event.pos[0]< 1200 :
                            New_Game_Status = True 
                            initnewcolours = True
                            Game_State = Game_Screen
                            screen.fill((40,40,40))
                    if event.pos[1] > 620 and event.pos[0] > 1000 :
                        if event.pos[1] < 800 and event.pos[0]< 1200 :
                            Game_State = Start_Screen
                            New_Game_Status = True 
                            initnewcolours = True



    elif Game_State == Leaderboard_screen:
        screen.blit(Leaderboardpage2,(0,0))
        screen.blit(Backbutton,(1000,600))
        leaderboard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] > 600 and event.pos[0] > 1000 :
                        if event.pos[1] < 800 and event.pos[0]< 1200 :
                            Game_State = SettingsPage
            


    elif Game_State == SettingsPage:
        screen.blit(Settingspage2,(0,0))
        drawaroundselected(Num_Guesses_Allowed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] > 605 and event.pos[0] > 1020 :
                        if event.pos[1] < 800 and event.pos[0]< 1200 :
                            Game_State = Start_Screen
                    if event.pos[1] > 0 and event.pos[0] > 0 :
                        if event.pos[1] < 120 and event.pos[0]< 265 :
                            Game_State = Input_Page    
                    if event.pos[1] > 255 and event.pos[0] > 160 :
                        if event.pos[1] < 285 and event.pos[0]< 180 :
                            Num_Guesses_Allowed = 4 
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 260 :
                        if event.pos[1] < 285 and event.pos[0]< 280 :
                            Num_Guesses_Allowed = 5 
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 360 :
                        if event.pos[1] < 285 and event.pos[0]< 380 :
                            Num_Guesses_Allowed = 6 
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 460 :
                        if event.pos[1] < 285 and event.pos[0]< 480 :
                            Num_Guesses_Allowed = 7 
                            drawaroundselected(Num_Guesses_Allowed)

                    if event.pos[1] > 255 and event.pos[0] > 550 :
                        if event.pos[1] < 285 and event.pos[0]< 580 :
                            Num_Guesses_Allowed = 8
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 640 :
                        if event.pos[1] < 285 and event.pos[0]< 680 :
                            Num_Guesses_Allowed = 9
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 750 :
                        if event.pos[1] < 285 and event.pos[0]< 780 :
                            Num_Guesses_Allowed = 10
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 860 :
                        if event.pos[1] < 285 and event.pos[0]< 890 :
                            Num_Guesses_Allowed = 11
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 255 and event.pos[0] > 980 :
                        if event.pos[1] < 285 and event.pos[0]< 1000 :
                            Num_Guesses_Allowed = 12
                            drawaroundselected(Num_Guesses_Allowed)
                    if event.pos[1] > 545 and event.pos[0] > 0:
                        if event.pos[1] < 800 and event.pos[0]< 220 :
                            Game_State = Leaderboard_screen
                    
                    
                            


    elif Game_State == Help_Screen:
        screen.blit(Help_ScreenIMG2,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            #event button one is the left click
                if event.button == 1:
                    if event.pos[1] > 612 and event.pos[0] > 1042 :
                        if event.pos[1] < 790 and event.pos[0]< 1200 :
                            Game_State = Start_Screen
    elif Game_State == Win_Screen:
        screen.fill((0,0,0))
        pygame.draw.circle(screen,CombinationPeg1Colour,(450, 630),12)
        pygame.draw.circle(screen,CombinationPeg2Colour,(550, 630),12)
        pygame.draw.circle(screen,CombinationPeg3Colour,(650, 630),12)
        pygame.draw.circle(screen,CombinationPeg4Colour,(750, 630),12)
        screen.blit(YouWinImage2  ,(400,100))
        screen.blit(Winning_writing,textrect.center)
        screen.blit(New_GameIMG1,(1000,00) )
        screen.blit(HomeButton1,(1000,600))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] > 0 and event.pos[0] > 1000 :
                        if event.pos[1] < 200 and event.pos[0]< 1200 :
                            New_Game_Status = True 
                            initnewcolours = True
                            Game_State = Game_Screen
                            screen.fill((40,40,40))
                    if event.pos[1] > 620 and event.pos[0] > 1000 :
                        if event.pos[1] < 800 and event.pos[0]< 1200 :
                            Game_State = Start_Screen
                            New_Game_Status = True 
                            initnewcolours = True
                            
                        
                        
                    
        

                    
    
    #Loads the submit button (image, (x,y))
    elif Game_State == Game_Screen:
        if initnewcolours :
            newgame()
            initnewcolours = False
        screen.blit(imp,(860,650))
    


    # the syntax is (screen, (colour),(centre(x,y)), radius)
        pygame.draw.circle(screen,Peg1colour,indexPeg1,16)
        pygame.draw.circle(screen,Peg2colour,indexPeg2,16)
        pygame.draw.circle(screen,Peg3colour,indexPeg3,16)
        pygame.draw.circle(screen,Peg4colour,indexPeg4,16)
        Submitstatus = False
        screen.blit(Title,Titlerect)

    #this is telling us that for any event in pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # for when a mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
            #event button one is the left click
                if event.button == 1:
                #Creating the hitbox for the pegs so the colours can be toggled through 
                    if event.pos[1] > (indexPeg1[1] - 18) and event.pos[0] > (indexPeg1[0] - 18):
                        if event.pos[1] < (indexPeg1[1]+18) and event.pos[0]< (indexPeg1[0]+18):
                            Peg1.set_pegColour(Peg1colour)
                            Peg1colour = Peg1.get_pegColour()                       
                        else:
                            pass
                    else:
                        pass
                    if event.pos[1] > (indexPeg2[1] - 18) and event.pos[0] > (indexPeg2[0] - 18):
                        if event.pos[1] < (indexPeg2[1]+18) and event.pos[0]< (indexPeg2[0]+18):
                            Peg2.set_pegColour(Peg2colour)
                            Peg2colour = Peg2.get_pegColour()                       
                        else:
                            pass
                    else:
                        pass
                    if event.pos[1] > (indexPeg3[1] - 18) and event.pos[0] > (indexPeg3[0] - 18):
                        if event.pos[1] < (indexPeg3[1]+18) and event.pos[0]< (indexPeg3[0]+18):
                            Peg3.set_pegColour(Peg3colour)
                            Peg3colour = Peg3.get_pegColour()                       
                        else:
                            pass
                    else:
                        pass
                    if event.pos[1] > (indexPeg4[1] - 18) and event.pos[0] > (indexPeg4[0] - 18):
                        if event.pos[1] < (indexPeg4[1]+18) and event.pos[0]< (indexPeg4[0]+18):
                            Peg4.set_pegColour(Peg4colour)
                            Peg4colour = Peg4.get_pegColour()                       
                        else:
                            pass
                    else:
                        pass
                    if event.pos[0] > 860 and event.pos[1] > 650:
                        if event.pos[0]< 1200 and event.pos[1] <752:
                            Submitstatus = True
                            SubmitCount = SubmitCount + 1 
                    
        if Submitstatus == True and SubmitCount < Num_Guesses_Allowed +1 :
            SubmittedYposition = (SubmitCount * 50)+ 40 
            pygame.draw.circle(screen,Peg1colour,(450,SubmittedYposition),16)
            pygame.draw.circle(screen,Peg2colour,(550,SubmittedYposition),16)
            pygame.draw.circle(screen,Peg3colour,(650,SubmittedYposition),16)
            pygame.draw.circle(screen,Peg4colour,(750,SubmittedYposition),16)
            guess = (Peg1colour,Peg2colour,Peg3colour,Peg4colour)
            pygame.display.update() 
            displaycheckcolours(checkcolours())
        if SubmitCount == Num_Guesses_Allowed + 1  : 
            Game_State = Lose_screen
            screen.fill((0,0,0))
        if Win_Status and not New_Game_Status:
            Game_State = Win_Screen
            NumberOfNames += 1
            savescore(username, SubmitCount)
            
  



            
                         

    pygame.display.update() 




pygame.quit()
 


