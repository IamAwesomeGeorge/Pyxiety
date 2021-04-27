import os

def next():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def mainmenu():
  next()
  print("\n   ___            _      _         \n  / _ \_   ___  _(_) ___| |_ _   _ \n / /_)/ | | \ \/ / |/ _ \ __| | | |\n/ ___/| |_| |>  <| |  __/ |_| |_| |\n\/     \__, /_/\_\_|\___|\__|\__, |\n       |___/                 |___/ \n\n")
  print("1.         Show heart rate\n2.         Games\n3.         Credits\n")
  menuM=input("Please select from the menu above:  ")

  if menuM == '1':
    next()
    os.system('python Raspberry-Pi-Heartbeat-Pulse-Sensor-master/example.py')
    input("\nPress enter to go back... ")
    mainmenu()
  elif menuM == '2':
    gamemenu()
  elif menuM == '3':
    credits()
  else:
    mainmenu()


def gamemenu():
  next()
  print("\n\n   ___                _             \n  / _ \__ _ _ __ ___ (_)_ __   __ _ \n / /_\/ _` | '_ ` _ \| | '_ \ / _` |\n/ /_\\\ (_| | | | | | | | | | | (_| |\n\____/\__,_|_| |_| |_|_|_| |_|\__, |\n                              |___/ \n\n")
  print("1.         Paint\n2.         Snake\n3.         Blackjack\n4.         Number Guesser\n5.         Back\n")
  menuG=input("Please select from the game menu above:  ")
  if menuG == '1':
    print("\nPaint has opened. Close the window when you have finished.")
    os.system('python Paint.py')
    input("\nPress enter to go back to games menu... ")
    gamemenu()
  elif menuG == '2':
    print("\nSnake has opened. Close the window when you have finished.\n")
    os.system('python rkn.py')
    input("\nPress enter to go back to games menu... ")
    gamemenu()
  elif menuG == '3':
    next()
    os.system('python blackjack.py')
  elif menuG == '4':
    next()
    os.system('python NumberGuesser.py')
  elif menuG == '5':
    mainmenu()
  else:
    gamemenu()

def credits():
  next()
  print("\n\n   ___             _ _ _       \n  / __\ __ ___  __| (_) |_ ___ \n / / | '__/ _ \/ _` | | __/ __|\n/ /__| | |  __/ (_| | | |_\__ \\\n\____/_|  \___|\__,_|_|\__|___/\n")

  print("\nMade by John F. Kennedy School's 2021 Year 12 class of Computer Science\n")
  print("Circuit:                             Caelan Woodstock")
  print("Coding:                              George Keen")
  print("Write up:                            Gordon Saad and Ryan Tam Lit-Taylor")
  print("Paint and Snake:                     Oskar Maslanka and Theo Tyszkiewicz")
  print("Blackjack:                           Ryan Tam Lit-Taylor")
  print("Number Guesser:                      George Keen")
  print("\nMany thanks to Mr Ahern for his support!")
  print("\n©Pyxiety                             Ver 1.0.1\n\n")
  input("Press enter to go back...")
  mainmenu()

mainmenu()