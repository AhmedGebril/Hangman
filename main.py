import random
import turtle
import collections
import tkinter
import threading

words_diff = ["cat", "dog", "cow", "bird", "snail", "camael"]
already_in = []
wrong_count = 0
word = random.choice(words_diff)
hmTC = (0, 0)


def create_boxes():
    boxes = []
    x_position = -150
    for letter in range(len(word)):
        boxes.append(turtle.Turtle())
        boxes[letter].hideturtle()
        boxes[letter].penup()
        boxes[letter].goto(x_position, -220)
        draw_box(boxes[letter])
        x_position += 80
    return boxes


# drawing the boxes of the letters
def draw_box(drawing_turtle):
    drawing_turtle.pendown()
    drawing_turtle.fd(50)
    drawing_turtle.lt(90)
    drawing_turtle.fd(50)
    drawing_turtle.lt(90)
    drawing_turtle.fd(50)
    drawing_turtle.lt(90)
    drawing_turtle.fd(50)
    drawing_turtle.lt(90)


# responsible for drawing the hangman
def Hangman(num):
    global hmTC
    hm = turtle.Turtle()
    if num == 0:
        hm.penup()
        hm.setpos(-670, -340)
        hm.pendown()
        hm.ht()
        hm.begin_fill()
        hm.fd(400)
        hm.lt(90)
        hm.fd(50)
        hm.lt(90)
        hm.fd(390)

        hm.rt(90)
        hm.fd(600)
        hm.rt(90)
        hm.fd(400)
        hm.rt(90)
        hm.fd(20)
        hm.lt(90)
        hm.fd(10)

        hm.lt(90)
        hmTC = hm.pos()
        hm.fd(30)

        hm.lt(90)
        hm.fd(420)
        hm.lt(90)
        hm.fd(550)
        hm.end_fill()
        hm.pensize(5)

    elif (num == 1):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.rt(180)
        hm.fd(5)
        hm.pendown()
        hm.circle(40)
    elif (num == 2):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1] - 80)
        hm.lt(90)
        hm.pendown()
        hm.fd(140)
        hmTC = hm.pos()
    elif (num == 3):
        hm.penup()
        hm.rt(30)
        hm.pendown()
        hm.fd(100)
        hm.rt(60)
        hm.fd(10)
        hm.penup()
        hm.rt(180)
        hm.fd(10)
        hm.rt(30)
        hm.fd(100)
        hm.rt(90)
        hm.pendown()

    elif (num == 4):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.pendown()
        hm.lt(60)
        hm.fd(100)
        hm.lt(60)
        hm.fd(10)
    elif (num == 5):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.lt(90)
        hm.fd(90)
        hm.lt(180)
        hm.rt(30)
        hm.pendown()
        hm.fd(80)
        hm.rt(60)

    elif (num == 6):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.rt(90)
        hm.fd(90)
        hm.lt(180)
        hm.lt(30)
        hm.pendown()
        hm.fd(80)
    elif (num == 7):
        hm.penup()
        hm.setpos(-235.00, 265.00)
        hm.rt(90)
        hm.pendown()
        hm.circle(4)

    elif (num == 8):
        hm.penup()
        hm.setpos(-265, 265.00)
        hm.rt(90)
        hm.pendown()
        hm.circle(4)
    else:
        hm.penup()
        hm.setpos(hm.pos()[0] + 25, hm.pos()[1] - 35)
        hm.pendown()
        hm.rt(30)
        hm.circle(10, 180)


def check_answer(user_input,boxes_list):
    global wrong_count

    # keep tracking the index of the correct letter
    count = 0

    # checks if the user already typed the letter
    if user_input in already_in:
        print("you already guessed that number")
        wrong_count += 1

    elif user_input=="":
        wrong_count+=1
        print("Please Enter A valid Letter")
    # Loops the user input and puts the letter in the box with the correct index
    else:
        for letter in word:
            if user_input == letter:
                already_in.append(user_input)
                boxes_list[count].write(f" {letter}", align="left", font=("Arial", 30, "bold"))
            count += 1
    # checks if user has put a wrong letter
    if user_input not in word:
        Hangman(wrong_count)
        wrong_count += 1
        print("wrong! take another guess: ")


# Checks if the user has won or not
def repeat(answer,entry,screen,boxes_list,win):
    DidWin(answer,win,screen)

    if wrong_count != 10:
        screen.update()
        user_input = entry.get()
        check_answer(user_input,boxes_list=boxes_list)
        clear_text(entry)
        print(answer, already_in)
    elif wrong_count == 10:
        label = tkinter.Label(win, text="You Lose", font=("Courier 22 bold"))
        label.pack()
        tkinter.Button(win, text="Do you want to retry ?", width=20,command= lambda :Restart(win,screen)).pack(pady=20)
        tkinter.Button(win, text="Exit ", width=20,command=ExitProgram).pack(pady=50)





def DidWin(answer,win,screen):
    if collections.Counter(answer) == collections.Counter(already_in):
        label = tkinter.Label(win, text="You win", font=("Courier 22 bold"))
        label.pack()
        tkinter.Button(win, text="Do you want to retry ?", width=20,command= lambda :Restart(win,screen)).pack(pady=20)
        tkinter.Button(win, text="Exit ", width=20,command=ExitProgram).pack(pady=50)
    else:
        return


# Clears the text
def clear_text(entry):
    entry.delete(0, tkinter.END)

# Exits the program
def ExitProgram():
    exit()

def game():
    # Create an instance of Tkinter frame
    win = tkinter.Tk()

    # Set the geometry of Tkinter frame
    win.geometry("450x350")

    # set Up the turtle
    screen = turtle.Screen()
    screen.tracer(0)
    answer = list(word)
    boxes_list = create_boxes()

    label = tkinter.Label(win, text="Choose a letter", font=("Courier 22 bold"))
    label.pack()

    # Create an Entry widget to accept User Input
    entry = tkinter.Entry(win, width=40)
    entry.focus_set()
    entry.pack()


    print(word)

    # Create a Button to validate Entry Widget
    tkinter.Button(win, text="Okay", width=20, command=lambda: repeat(answer,entry,screen,boxes_list,win)).pack(pady=20)
    screen.update()

    screen.exitonclick()

def Restart(win,screen):
    global wrong_count
    wrong_count=0
    screen.reset()
    win.destroy()
    game()

game()