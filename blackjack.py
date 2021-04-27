import os

ready = input("Ready?")

#Selecting first card for each player



ace = 0
cace = 0
playing = 0
cplaying = 0

from Card import chooseCard

suit, value, num = chooseCard()

suitA = suit
valueA = value
numA = num
if num == "Ace":
  ace = ace + 1

print ("")
print ("Your first card is the", numA,"of",suitA)
print ("Your current value is",valueA)
continyou = input("Continue?")

from Card import chooseCard

suit, value, num = chooseCard()

csuitA = suit
cvalueA = value
cnumA = num
if num == "Ace":
  cace = cace + 1
print ("")
print ("Computer's first card is the", cnumA,"of",csuitA)
print ("Computer's current value is",cvalueA)
continyou = input("Continue?")

#now selecting second card for each player

from Card import chooseCard

suit, value, num = chooseCard()

suitB = suit
valueA = valueA + value
numB = num
if num == "Ace":
  ace = ace + 1

print ("")
print ("Your second card is the", numB,"of",suitB)
print ("Your current value is",valueA)
continyou = input("Continue?")

from Card import chooseCard

suit, value, num = chooseCard()

csuitB = suit
cvalueA = cvalueA + value
cnumB = num
if num == "Ace":
  cace = cace + 1
print ("")
print ("Computer's second card is hidden  ")
print ("")
continyou = input("Continue?")
print ("")

#Now asking the player whether to hit or stick

while valueA != 21 and playing == 0 :
  hos = input("Would you like to hit (H) or stick (S)")
  if hos == "H" or hos == "h":
    from Card import chooseCard

    suit, value, num = chooseCard()

    suitC = suit
    valueA = valueA + value
    numC = num
    if num == "Ace":
      ace = ace + 1

    if valueA > 21:
      if (ace - 1)>= 0:
        valueA = valueA - 10
        ace = ace - 1


    print ("")
    print ("Your new card is the", numC,"of",suitC)
    print ("Your current value is",valueA)

  if hos == "S" or hos == "s":
    print ("")
    print ("Ok. You have chosen to stick")
    print ("")
    print ("Computer will now choose to hit or stick")
    playing = 1

  if valueA > 21:

    if (ace - 1)>= 0:
      valueA = valueA - 10
      ace = ace - 1

    else:
      print ("")
      print ("Game over")
      print ("Your value is",valueA, ". You have Gone bust")
      playing = 1
      cplaying = 1

if playing == 0:
  print ("")
  print ("You got blackjack. The worst that can happen is a draw")

print ("")
continyou = input("Continue?")

while cvalueA != 21 and cplaying == 0:
  if cvalueA <= 15 :
    hosr = 1

  if cvalueA > 15 and cvalueA < 18:
    import random 
    hosr = (random.randint(1,5))

  if cvalueA >= 18:
    import random
    hosr = (random.randint(1,10))

  if hosr == 1:
    hos = "H"

  else:
    hos = "S"
    print ("Computer has decided to stick")
    cplaying = 1

  if hos == "H" or hos == "h":
    from Card import chooseCard

    suit, value, num = chooseCard()

    csuitC = suit
    cvalueA = cvalueA + value
    cnumC = num
    if num == "Ace":
      cace = cace + 1

    print ("")
    print ("Computer has decided to hit")
    print ("Computer's new card is the", cnumC,"of",csuitC)

  if cvalueA > 21:

    if (cace - 1)>= 0:
      cvalueA = cvalueA - 10
      cace = cace - 1

    else:
      print ("")
      print ("You Win!!")
      print ("Computer's value is",cvalueA, ". They have Gone bust")
      cplaying = 1

continyou = input("Continue?")
print ("Your value is", valueA)
print ("")
print ("Computer's value is",cvalueA)
if (valueA - cvalueA) > 0 and valueA <= 21 and cvalueA <= 21:
  print ("You Win!!!")

if (valueA - cvalueA) < 0 and valueA <= 21 and cvalueA <= 21:
  print ("You Lose :(")


if (valueA - cvalueA) == 0 and valueA <= 21 and cvalueA <= 21:
  print ("Its a Tie!!!")

input("\nPress enter to go back to games menu... ")
os.system('python main.py')