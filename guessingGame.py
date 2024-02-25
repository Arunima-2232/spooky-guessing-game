import pygame, sys, tkinter, os, random
from pygame.locals import*
from tkinter import*
from tkinter import messagebox
from string import ascii_uppercase

def newGame():
    
    global the_word_withSpaces
    global numberOfGuesses
    global ind
    global the_word
    global word_list
    global score
    
    hint=" "
    ind +=1
    
    if ind<5:
        the_word=word_list[ind]
        if ind==0:
            hint="It starts with C and ends with N. It is used by all witches to make magical potions. What is it?"
        elif ind==2:
            hint="He loves sleeping and lives in Transylvania. He can shapeshift into a bat. Who is he?"
        elif ind==4:
            hint="It has mighty tall walls, all the riches and a dark prison to capture evil. What is it?"
        elif ind==1:
            hint="It starts with a S and ends with a K. It has thousands of spells that are needed by all witches to learn her way. What is it?"
        elif ind==3:
            hint="It breathes fire and can fly high. If you befriend and train this mighty beast, it can show you around. What is it?"

        messagebox.showinfo("HINT",hint)
        
        the_word=the_word.upper()
        the_word_withSpaces=" ".join(the_word)
        lblWord.set(" ".join("_"*len(the_word)))
        
        

    else: 
        global window
        
        messagebox.showinfo("Congratulations",f"You Won! \nYour Score={score}") 

        close_button=Button(window, text="Exit", command=window.destroy)
        window.mainloop() 

        pygame.quit()
        sys.exit()        

def guess(letter): 
    
    global numberOfGuesses
    global ind
    global score
    global window
    
    txt=list(the_word_withSpaces) 
    guessed=list(lblWord.get()) 
    
    if numberOfGuesses<5:
        if the_word_withSpaces.count(letter)>0: 
            for c in range(len(txt)):
                if txt[c]==letter: ##if letter is in the word
                    guessed[c]=letter ##update the word on tkinter
                lblWord.set("".join(guessed)) ##set func sets the value of lblWord
                if lblWord.get()==the_word_withSpaces: ##if word has been guessed get func gets the current value of lblWord
                    if ind<5:
                        score+=2
                        if ind<4:
                            messagebox.showinfo("Correct","You guessed it!")
                        newGame()
                        window.mainloop()
                    elif ind==4: 
                        
                        newGame()
                   
        else:
            numberOfGuesses+=1
            number=5-numberOfGuesses
            messagebox.showerror("error",f"Wrong input\nYou have {number} guesses left")
            score-=1
    elif numberOfGuesses==5:    
        score-=1
        messagebox.showwarning("Try Again",f"You Lost. \nYour Score={score}")

        close_button=Button(window, text="Exit", command=window.destroy)
        window.mainloop()

        pygame.quit()
        sys.exit()  

def Pass():
    
    global score
    global ind
    
    score-=1
    
    messagebox.showinfo("Level skipped",f"The word was {the_word}")
    
    newGame()
    
def win():
    global window
    window=Tk()
    window.title("ghoulish guessing")
    window.geometry("+290+245")
    window.iconbitmap("C:/Users/Paul/Downloads/ME/code/pygame/final/bat.ico")
    
    global word_list
    global the_word
    global lblWord
    lblWord=StringVar() ##helps manage the value of widget and in taking user input
    Label(window,textvariable=lblWord, font=("candara")).grid(row=0,column=0,columnspan=6,padx=20) 
    
    n=0
    for c in ascii_uppercase: 
        
        Button(window, activebackground='#69408f',activeforeground='#fefcff', text=c,command=lambda c=c: guess(c), font=("candara"), width=4).grid(row=1+n//9, column=n%9)
        n+=1

    Button(window, activebackground='#69408f',activeforeground='#fefcff', text="Pass", command=lambda: Pass(), font=("candara")).grid(row=3,column=8)
    
    newGame()
    window.mainloop()

def game():
    screen.blit(bg2,(0,0)) ##draws the image on the screen
    win()
    
class Buttons():
    def __init__(self,x,y,image):
        
        self.image=image 
        self.rect=self.image.get_rect() 
        self.rect.topleft=(x,y)

    def draw(self):
        
        action=False
        pos=pygame.mouse.get_pos() ##to get position of mouse cursor
        if self.rect.collidepoint(pos): ##if mouse cursor hovers over image (or collides with image's rectangle)
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False: ##if player clicks on image (button)
                
                self.clicked=True 
                action=True
        if pygame.mouse.get_pressed()[0]==0: 
            self.clicked=False

        screen.blit(self.image,(self.rect.x,self.rect.y)) 
        
        return action
        

class Bg():
    def __init__(self):
        self.images=[] 
        
        for num in range(0,22):
            
            bg=pygame.transform.scale(pygame.image.load(f"C:/Users/Paul/Downloads/ME/code/pygame/final/bg/bg{num}.png"),(screen_width,screen_height)) 
            self.images.append(bg)
            
    def update(self):

        for num in range(0,22):
            screen.blit(self.images[num],(0,0))
            pygame.display.update() 
            pygame.time.wait(190) ##waits for 190 seconds (pauses the program)
            
        game()

def main():

    ex=0
    bg=Bg() 
    run=True
    
    while run: 
        screen.blit(bg2,(0,0))

        if exit_button.draw()==True: 
            ex=1
        if start_button.draw()==True:
            bg.update() 
        for event in pygame.event.get(): ##even = input from keyboard/mouse
                if event.type == pygame.QUIT or ex==1: ##if player clicks on X to exit or clicks on exit button
                        
                        run = False
                        
        pygame.display.update() ##the image drawn (screen.blit) appears on screen
    
    pygame.quit()
    sys.exit()
    
screen_width=700
screen_height=600

numberOfGuesses=0
the_word=""
score=0

word_list=['cauldron','spellbook','dracula','dragon','castle']
ind=-1

bg2=pygame.transform.scale(pygame.image.load("C:/Users/Paul/Downloads/ME/code/pygame/final/bg/bg0.png"),(screen_width,screen_height))

screen=pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption('ghoulish guessing')
icon=pygame.image.load("C:/Users/Paul/Downloads/ME/code/pygame/final/bat.png")
pygame.display.set_icon(icon)

start=pygame.transform.scale(pygame.image.load("C:/Users/Paul/Downloads/ME/code/pygame/final/start.jpg"),(300,100))
exits=pygame.transform.scale(pygame.image.load("C:/Users/Paul/Downloads/ME/code/pygame/final/quit.jpg"),(280,100)) 
start_button=Buttons(210,270,start)
exit_button=Buttons(210,380,exits)

main()
