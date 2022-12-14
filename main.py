import tkinter as tk
import random
import playsound

# GUI, randomizer, and mp3-playing modules

root = tk.Tk()
# canvas name

root.title('Word Guesser')
# title above canvas

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()
# canvas dimensions

label1 = tk.Label(root, text='Word Guessing Game')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
# title inside canvas

my_words = ["rainbow", "dog", "gold"]
random_word = random.choice(my_words)
# random words

entry1 = tk.Entry(root)

# entry widget

def create_canvas():
    canvas1.delete("all")
    # to clear canvas

    label1 = tk.Label(root, text='Word Guessing Game')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    canvas1.create_window(200, 140, window=entry1)

    button1 = tk.Button(text='Enter', command=see_if_correct, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    my_disclaimer = tk.Label(root, text='Type in all lowercase.')
    my_disclaimer.config(font=('helvetica', 10))
    canvas1.create_window(200, 200, window=my_disclaimer)

    # new widgets

    if random_word == "rainbow":
        label2 = tk.Label(root, text='I am a seven-letter word. I am colorful, \nand I only show myself '
                                     'in the rain. \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "gold":
        label2 = tk.Label(root, text='I am a four-letter word and I am a very expensive metal. \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "dog":
        label2 = tk.Label(root, text="I am a three letter word that is man's best friend. \nWhat am I?")
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    else:
        print("Something went wrong!")

    # hint for word and error message


def see_if_correct():
    guess_num = 3
    # no. of guesses
    if random_word in entry1.get():
        canvas1.delete("all")
        result = tk.Label(root, text="You are correct! Congratulations!\n\n\n :D")
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=result)
        playsound.playsound('winner.mp3')
    # if guess correct: clears canvas and plays sound
    else:
        guess_num -= 1
        result = tk.Label(root, text="Try again. You have " + str(guess_num) + " guesses left.")
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 230, window=result)
        create_canvas2()
        playsound.playsound('loser.mp3')
    # if guess incorrect: removes one guess and plays sound


def create_canvas2():
    canvas1.delete("all")

    label1 = tk.Label(root, text='Word Guessing Game')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    canvas1.create_window(200, 140, window=entry1)

    button1 = tk.Button(text='Enter', command=see_if_correct2, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    result = tk.Label(root, text="Try again. You have 2 guesses left.")
    result.config(font=('helvetica', 10))
    canvas1.create_window(200, 230, window=result)

    my_disclaimer = tk.Label(root, text='Type in all lowercase.')
    my_disclaimer.config(font=('helvetica', 10))
    canvas1.create_window(200, 200, window=my_disclaimer)

    if random_word == "rainbow":
        label2 = tk.Label(root, text='I am often seen when the rain and sunlight collide. \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "gold":
        label2 = tk.Label(root, text='I am a very heavy metal that is worth a lot of money. \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "dog":
        label2 = tk.Label(root, text="When I want to communicate, I bark. \nWhat am I?")
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    else:
        print("Something went wrong!")


def see_if_correct2():
    guess_num = 2
    # no. of guesses
    if random_word in entry1.get():
        canvas1.delete("all")
        result = tk.Label(root, text="You are correct! Congratulations!\n\n\n :D")
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=result)
        playsound.playsound('winner.mp3')
    else:
        guess_num -= 1
        create_canvas3()
        playsound.playsound('loser.mp3')


def create_canvas3():
    canvas1.delete("all")

    label1 = tk.Label(root, text='Word Guessing Game')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    canvas1.create_window(200, 140, window=entry1)

    button1 = tk.Button(text='Enter', command=see_if_correct3, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    my_disclaimer = tk.Label(root, text='Type in all lowercase.')
    my_disclaimer.config(font=('helvetica', 10))
    canvas1.create_window(200, 200, window=my_disclaimer)

    result = tk.Label(root, text="Try again. You have 1 guess left.")
    result.config(font=('helvetica', 10))
    canvas1.create_window(200, 230, window=result)

    if random_word == "rainbow":
        label2 = tk.Label(root, text='I start with "R" and end with "W". \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "gold":
        label2 = tk.Label(root, text='I start with "G" and end with "D". \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    elif random_word == "dog":
        label2 = tk.Label(root, text='I start with "D" and end with "G". \nWhat am I?')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
    else:
        print("Something went wrong!")


def see_if_correct3():
    guess_num = 1
    # no. of guesses
    if random_word in entry1.get():
        canvas1.delete("all")
        result = tk.Label(root, text="You are correct! Congratulations!\n\n\n :D")
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=result)
        playsound.playsound('winner.mp3')
    else:
        canvas1.delete("all")
        result = tk.Label(root, text="You have no more guesses left. Try again!\n\n\n :(")
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=result)
        playsound.playsound('loser.mp3')


# code repeated for number of guesses


button1 = tk.Button(text='Generate Random Word', command=create_canvas, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 150, window=button1)
# button to start the process


root.mainloop()
# shows window
