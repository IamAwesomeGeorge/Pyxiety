def chooseCard ():

 import random
 suit = (random.randint(1,4))

 if suit == 1:
   suit = ("Spades")

 if suit == 2:
   suit = ("Hearts")

 if suit == 3:
   suit = ("Clubs")

 if suit == 4:
   suit = ("Diamonds")


 import random 
 num = (random.randint(1,13))

 if num == 1:
   num = ("Ace")
   value = 11

 if num == 2:
   num = ("Two")
   value = 2

 if num == 3:
   num = ("Three")
   value = 3

 if num == 4:
   num = ("Four")
   value = 4

 if num == 5:
   num = ("Five")
   value = 5

 if num == 6:
   num = ("Six")
   value = 6

 if num == 7:
   num = ("Seven")
   value = 7

 if num == 8:
   num = ("Eight")
   value = 8

 if num == 9:
   num = ("Nine")
   value = 9

 if num == 10:
   num = ("Ten")
   value = 10

 if num == 11:
   num = ("Jack")
   value = 10

 if num == 12:
   num = ("Queen")
   value = 10

 if num == 13:
   num = ("King")
   value = 10

 return suit, value, num