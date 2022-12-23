import turtle as t
import random
t.speed(0)
t.hideturtle()
def draw_base():
  t.penup()
  t.goto(-100, -70)
  t.pendown()
  t.fd(80)
  t.bk(40)
  t.lt(90)
  t.fd(140)
  t.rt(90)
  t.fd(60)
  t.rt(90)
  t.fd(25)
def draw_face():
  t.penup()
  t.goto(-12, 33)
  t.pendown()
  t.circle(12, 360)
def draw_body():
  t.penup()
  t.goto(0, 21)
  t.pendown()
  t.fd(45)
def left_leg():
  t.penup()
  t.goto(0, -23)
  t.pendown()
  t.setheading(-120)
  t.fd(30)
def right_leg():
  t.penup()
  t.goto(0, -23)
  t.pendown()
  t.setheading(-55)
  t.fd(30)
def right_arm():
  t.penup()
  t.goto(0, 10)
  t.pendown()
  t.fd(30)
def left_arm():
  t.penup()
  t.goto(0, 10)
  t.pendown()
  t.setheading(-120)
  t.fd(30)
def draw_hangman(error):
  draw_base()
  if (error == 1):
    draw_face()
  elif (error == 2):
    draw_body()
  elif (error == 3):
    left_leg()
  elif (error == 4):
    right_leg()
  elif (error == 5):
    left_arm()
  elif (error == 6):
    right_arm()
  elif (error > 6):
    t.clear()
    t.bgcolor("black")
    t.pencolor("white")
    t.penup()
    t.goto(-120, -50)
    t.write("Game\n Over", font=("Arial", 50, 'normal', 'bold'))
def draw_letters(input_letter, word):
  t.penup()
  t.goto(100, 50)
  for letter in word:
    print(letter)
    if input_letter == letter:
      t.write(input_letter + "  ", True, font=("Courier", 14, "normal"))
    else:
      t.write("_  ", True, font=("Courier", 14, "normal"))
  t.pendown()
def draw_win():
  t.clear()
  t.bgcolor("black")
  t.pencolor("white")
  t.penup()
  t.goto(-145, -55)
  t.write("You Won", font=("Arial", 50, 'normal', 'bold'))
word_bank = [
  'treaty', 'activity', 'program', 'impress', 'scrap', 'factor', 'mouse',
  'undermine', 'basic', 'metal']
random_idx = random.randint(0, len(word_bank)-1)
word = word_bank[random_idx]
print(word)
t.penup()
t.goto(100, 50)
for letter in word:
  t.write("_  ", True, font=("Courier", 14, "normal"))
t.pendown()
error = 0
correct_num_letters = 0
win = False
input_letters = set()

while error < 7 and not win:
  input_letter = t.textinput("Hangman", "choose a letter(lower case)")
  if input_letter in input_letters:
    print("Your letter has already been used. Try again")
    continue
  else:
    input_letters.add(input_letter)
  if input_letter not in word:
    error += 1
  else:
    correct_num_letters += word.count(input_letter)
  t.setheading(0)
  draw_hangman(error)
  draw_letters(input_letter, word)
  if correct_num_letters == len(word):
    win = True
draw_win()