import random
import os

print("1.easy mode\n2.Normal Mode\n3.HARD MODE\n4.EXTREME MODE!!!!!")
dif=int(input("\nEnter the difficulty you want to play on: "))

if dif==1:
  guessc=15
elif dif==2:
  guessc=10
else:
  guessc=8

number=random.randint(0, 100)
print("\n\nI am thinking of a number between 1 - 100\nYou have", guessc, "guesses\n")

guessc=guessc+1
guessn=1
win=0
lower=0
higher=100
while guessn<guessc and win==0:
  print("Guess number", guessn)
  if dif==1:
    print("The number is between", lower, "and", higher)
  guess=int(input("Enter your guess: "))
  if guess==number:
    win=1
  else:
    if dif==4:
      print("\n\nWrong")
    else:
      if guess<number:
        print("\n\nThe number is higher")
        lower=guess
      elif guess>number:
        print("\n\nThe number is lower")
        higher=guess
    guessn=guessn+1

if win==1:
  print("\nWell done!\nYou guess the number", number, "right!")
else:
  print("you loose rip")

input("\nPress enter to go back to games menu... ")
os.system('python main.py')