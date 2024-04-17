from tkinter import * #Import for the grafic interface
import random #Import for the dice logic

#Creating the main app and giving it a title
root = Tk()
root.title("Dice Simulator")

#Defining the dice and its logic
def dice():
    #Since a die has 6 possible outcomes, 
    #the range of the random number generator is set between 1 and 6.
    n = random.randint(1,6)
    #Depending on the generated number stored in n, 
    #the faces are painted based on the value
    if n == 1:
        c1.config(bg='white')
        c2.config(bg='white')
        c3.config(bg='white')
        c4.config(bg='white')
        c5.config(bg='black')
        c6.config(bg='white')    
        c7.config(bg='white')
        c8.config(bg='white')
        c9.config(bg='white')
    elif n == 2:
        c1.config(bg='white')
        c2.config(bg='white')
        c3.config(bg='black')
        c4.config(bg='white')
        c5.config(bg='white')
        c6.config(bg='white')
        c7.config(bg='black')
        c8.config(bg='white')
        c9.config(bg='white')
    elif n == 3:
        c1.config(bg='white')
        c2.config(bg='white')
        c3.config(bg='black')
        c4.config(bg='white')
        c5.config(bg='black')
        c6.config(bg='white')
        c7.config(bg='black')
        c8.config(bg='white')
        c9.config(bg='white')
    elif n == 4:
        c1.config(bg='black')
        c2.config(bg='white')
        c3.config(bg='black')
        c4.config(bg='white')
        c5.config(bg='white')
        c6.config(bg='white')
        c7.config(bg='black')
        c8.config(bg='white')
        c9.config(bg='black')
    elif n == 5:
        c1.config(bg='black')
        c2.config(bg='white')
        c3.config(bg='black')
        c4.config(bg='white')
        c5.config(bg='black')
        c6.config(bg='white')
        c7.config(bg='black')
        c8.config(bg='white')
        c9.config(bg='black')
    elif n == 6:
        c1.config(bg='black')
        c2.config(bg='black')
        c3.config(bg='black')
        c4.config(bg='white')
        c5.config(bg='white')
        c6.config(bg='white')
        c7.config(bg='black')
        c8.config(bg='black')
        c9.config(bg='black')

#Creating the button to play
play_button = Button(root, text="Play!",
                     command= lambda:dice(), width=10)
play_button.grid(row=3, column=1)

#Creating the exit button
exit_button = Button(root, text="Exit",
                     command=root.destroy, width=10)
exit_button.grid(row=4, column=1, pady=5)

#Creating each dice coordinate
c1 = Label(root)
c1.config(width=5, height=5)
c1.grid(row=0, padx=5, pady=5)

c2 = Label(root)
c2.config(width=5, height=5)
c2.grid(row=1, padx=5, pady=5)

c3 = Label(root)
c3.config(width=5, height=5)
c3.grid(row=2, padx=5, pady=5)

c4 = Label(root)
c4.config(width=5, height=5)
c4.grid(row=0, column=1, padx=5, pady=5)

c4 = Label(root)
c4.config(width=5, height=5)
c4.grid(row=0, column=1, padx=5, pady=5)

c5 = Label(root)
c5.config(width=5, height=5)
c5.grid(row=1, column=1, padx=5, pady=5)

c6 = Label(root)
c6.config(width=5, height=5)
c6.grid(row=2, column=1, padx=5, pady=5)

c7 = Label(root)
c7.config(width=5, height=5)
c7.grid(row=0, column=2, padx=5, pady=5)

c8 = Label(root)
c8.config(width=5, height=5)
c8.grid(row=1, column=2, padx=5, pady=5)

c9 = Label(root)
c9.config(width=5, height=5)
c9.grid(row=2, column=2, padx=5, pady=5)


#Creating the app loop
root.mainloop()