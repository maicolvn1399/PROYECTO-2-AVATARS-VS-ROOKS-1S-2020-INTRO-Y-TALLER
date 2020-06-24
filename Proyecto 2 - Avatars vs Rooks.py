
"""
Instituto Tecnológico de Costa Rica
Área de Ingeniería en Computadores
CE1102 - Taller de Programación
Profesor: Jason Leitón Jiménez
Estudiantes: Raquel Lizano y Michael Valverde
II Proyecto - I Semestre - 2020
"""

from tkinter import *
from tkinter import messagebox
import os

def MainMenu():
    """This function is the first window the player sees, it provides the instructions for the game
 the credits, and the login"""

    mainWindow = Tk()
    mainWindow.title("Welcome - Avatars Vs Rooks")
    mainWindow.minsize(450,600)
    mainWindow.resizable(width=NO,height=NO)


    """Background image"""
    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(mainWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0)

    welcomeLabel = Label(mainWindow, text="Welcome - Avatars Vs Rooks", font="Fixedsys 17", bg="#b89bba", fg="black")
    welcomeLabel.place(x=15, y=60)

    loginLabel = Label(mainWindow, text="Player login", font="Fixedsys 16", bg="#b89bba", fg="black")
    loginLabel.place(x=25, y=220)

    nameEntry = Entry(mainWindow, width=25, bg="#b89bba", fg="black")
    nameEntry.place(x=150, y=220)

    playButton = Button(mainWindow, font="Fixedsys 16", text="Play", bg="#b89bba", fg="black")
    playButton.place(x=150, y=280)

    instructionsButton = Button(mainWindow, font="Fixedsys 16", text="Game Instructions", bg="#b89bba", fg="black",
                                command= lambda : InstructionsWindow())
    instructionsButton.place(x=150, y=320)

    creditsButton = Button(mainWindow, font="Fixedsys 16", text="Credits", bg="#b89bba", fg="black",
                           command= lambda : CreditsWindow())
    creditsButton.place(x=150, y=360)

    mainWindow.mainloop()

def InstructionsWindow():
    """GUI  to show the instructions of the game to the players"""
    instructionsWindow = Toplevel()
    instructionsWindow.minsize(600, 500)
    instructionsWindow.resizable(width=NO, height=NO)
    instructionsWindow.title("Instructions")

    """backgroundImage = LoadImage()
    labelBackground = Label(instructionsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage"""
    message = Message(instructionsWindow, text="GAME INSTRUCTIONS...\n"
                      , bg="#b89bba", justify="left", relief="ridge", font="Fixedsys 13")
    message.place(x=50, y=50)
    instructionsWindow.mainloop()

def CreditsWindow():
    """GUI for the credits of the game"""
    creditsWindow = Toplevel()
    creditsWindow.minsize(600, 500)
    creditsWindow.resizable(width=NO, height=NO)
    creditsWindow.title("Credits")
    """backgroundImage = LoadImage("bgCredits.gif")
    labelBackground = Label(creditsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage"""

    message = Message(creditsWindow, text="País: Costa Rica\n\n"
                                          "Instituto Tecnológico de Costa Rica - Ingeniería en Computadores\n\n"
                                          "CE1102 - Taller de Programación - Grupo #4\n\n"
                                          "II Proyecto - I Semestre 2020"
                                          "Profesor: Jason Leitón Jiménez\n\n"
                                          "V0.0\n\n"
                                          "Autores: Raquel Lizano y Michael Valverde Navarro\n\n"
                                          , bg="#b89bba", justify="left", relief="ridge", font="Fixedsys 16")

    message.place(x=100, y=100)

    creditsWindow.mainloop()


def ReadFile():
    """This function reads the file of the scores
    and return the content in a list"""
    path = ""
    file = open(path)
    content = file.readlines()
    file.close()
    return content

def WriteInFile(score):
    """This function writes the score on the file"""
    path = ""
    file = open(path,"a")
    file.write(score+"\n")
    file.close()


def LoadImage(ImgName):
    """Loads and image"""
    path = os.path.join('media', ImgName)
    imageToLoad = PhotoImage(file=path)
    return imageToLoad


MainMenu()