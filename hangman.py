import tkinter as tk
from tkinter import messagebox
import random

# Word list for the Hangman game
word_list = [ 'python' , 'language' , 'javascript' , 'visual' , 'hangman' , 'ambassador' , 'windows' , 'agile' , 'backed' , 'button' , 'print' , 'cancel' ]

chosen_word = ""
guessed_word = []
chances = 6
letters_guessed = []

def choose_word() :
    return random.choice ( word_list ).lower ( )

def reset_game() :
    global chosen_word , guessed_word , chances , letters_guessed
    canvas.delete ( "hangman" )
    chosen_word = choose_word ( )
    guessed_word = [ '_' for _ in chosen_word ]
    chances = 6
    letters_guessed = [ ]
    update_display ( )

def update_display() :
    word_label.config ( text=" ".join ( guessed_word ) )
    chances_label.config ( text=f"Chances Left: {chances}" )
    guessed_label.config ( text=f"Letters Guessed: {', '.join ( letters_guessed )}" )

def draw_hangman() :
    if chances == 5 :
        canvas.create_line ( 20 , 180 , 120 , 180 , fill="black" , width=3 , tags="hangman" )  # base
    elif chances == 4 :
        canvas.create_line ( 70 , 180 , 70 , 40 , fill="black" , width=3 , tags="hangman" )  # pole
    elif chances == 3 :
        canvas.create_line ( 70 , 40 , 140 , 40 , fill="black" , width=3 , tags="hangman" )  # beam
    elif chances == 2 :
        canvas.create_line ( 140 , 40 , 140 , 60 , fill="black" , width=3 , tags="hangman" )  # rope
    elif chances == 1 :
        canvas.create_oval ( 120 , 60 , 160 , 100 , outline="green" , width=3 , tags="hangman" )  # head
    elif chances == 0 :
        canvas.create_line ( 140 , 100 , 140 , 140 , fill="green" , width=3 , tags="hangman" )  # body
        canvas.create_line ( 140 , 120 , 120 , 100 , fill="green" , width=3 , tags="hangman" )  # left arm
        canvas.create_line ( 140 , 120 , 160 , 100 , fill="green" , width=3 , tags="hangman" )  # right arm
        canvas.create_line ( 140 , 140 , 120 , 160 , fill="green" , width=3 , tags="hangman" )  # left leg
        canvas.create_line ( 140 , 140 , 160 , 160 , fill="green" , width=3 , tags="hangman" )  # right leg


def guess_letter(event=None):
    global chances
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if len ( letter ) != 1 or not letter.isalpha ( ) :
        messagebox.showerror ( "Invalid Input" , "Please enter a single letter." )
        return

    if letter in letters_guessed :
        messagebox.showinfo ( "Duplicate Guess" , "You already guessed this letter." )
        return

    letters_guessed.append ( letter )

    if letter in chosen_word :
        for i , char in enumerate ( chosen_word ) :
            if char == letter :
                guessed_word [ i ] = letter
    else :
        chances -= 1
        draw_hangman ( )

    update_display ( )

    if "_" not in guessed_word :
        messagebox.showinfo ( "Game Over" , "Congratulations, You Won!" )
        reset_game ( )
    elif chances == 0 :
        messagebox.showinfo ( "Game Over" , f"You Lost! The word was: {chosen_word}" )
        reset_game ( )


# Set up tkinter window
window = tk.Tk ( )
window.title ( "Hangman Game" )
window.geometry ( "500x500" )
window.configure ( bg="#f2f2f2" )

# Create canvas for drawing hangman
canvas = tk.Canvas ( window , width=200 , height=200 , bg="#f2f2f2" , highlightthickness=0 )
canvas.pack ( pady=20 )

# Display word
word_label = tk.Label ( window , font=('Arial' , 24 , 'bold') , fg="#333" , bg="#f2f2f2" )
word_label.pack ( )

# Display chances left
chances_label = tk.Label ( window , font=('Arial' , 14) , fg="red" , bg="#f2f2f2" )
chances_label.pack ( )

# Display letters guessed
guessed_label = tk.Label ( window , font=('Arial' , 12) , fg="blue" , bg="#f2f2f2" )
guessed_label.pack ( )

# Entry for guessing a letter
letter_entry = tk.Entry ( window , font=('Arial' , 16) , width=5 , justify='center' )
letter_entry.pack ( pady=10 )

window.bind ( '<Return>' , guess_letter )
# '<Return>' is the Enter key

# Frame to hold buttons
button_frame = tk.Frame ( window , bg="#f2f2f2" )
button_frame.pack ( pady=20 )

# Guess button
guess_button = tk.Button ( button_frame , text="Guess" , font=('Arial' , 14) , bg="#4CAF50" , fg="white" ,
                           command=guess_letter )
guess_button.grid ( row=0 , column=0 , padx=10 )

# Reset button
reset_button = tk.Button ( button_frame , text="Reset Game" , font=('Arial' , 14) , bg="#2196F3" , fg="white" ,
                           command=reset_game )
reset_button.grid ( row=0 , column=1 , padx=10 )

# Initialize game
reset_game ( )

# Run the tkinter loop
window.mainloop ( )







