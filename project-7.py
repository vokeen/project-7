import os
from os import system
from tkinter import Y
system("clear")
import random

user=100
usercards=[]
comp=100
compcards=[]
uw=0
cw=0

# Start of Code>>>

def start():
    print(" Hi and welcome to Twenty !!! ")
    u()

def u():
    numcoin = input(" How many coins would you like to play? ")
    if numcoin.isdigit():
        cplay = user - int(numcoin)
        cplay = str(cplay)
        print("You Have " + cplay + " remaining ")
        gen()
    else:
        print(" Please try again and put a number ")
        u()

# Generate the cards>>>

def gen():
    numget= random.randint(1,10)
    usercards.append(numget)
    tot1=sum(usercards)
    print("")
    print(usercards)
    print(f'Your total is {sum(usercards)} in cards. ')

    numget= random.randint(1,10)
    compcards.append(numget)
    tot2=sum(compcards)
    print("")
    print(compcards)
    print(f'Computer total is {sum(compcards)} in cards. ')

# Decides who wins>>>

    if tot1 < 20 and tot2 < 20:
        print(" Keep Drawing Maybe??? ")
    elif tot1 > 20 and tot2 > 20:
        print(" Nobody Wins... ")
    elif tot1 == 20 and tot2 == 20:
        print(" Its a Draw!!! ")
    elif tot1 >= 20 or tot2 < tot1: 
        print("The Computer Wins!!! ")
        cwin = cw + 1
        print(" The computer has " + str(cwin) + " wins ")
    elif tot2 >= 20 or tot1 < tot2:
        print("You Win!!! ")
        uwin = uw + 1
        print(" You have " + str(uwin) + " wins ")
    else:
        print("")
    huh()
# Decides whether to keep going or not>>>
def huh():
    ask = input("Would you like more cards? (y) or (n) ")
    x=ask
    if ask == ("y"):
        system("clear")
        gen()
    elif ask == ("n"):
        runitback(x)
    else:
        ask = input(" Please Enter A Letter ")
        huh()
def runitback(x):
    if x == "y": 
        system('clear')
        u()
    elif x=="n":
        redo = input(" Would you like to continue to play ? (y) or (n) ")
        if redo == "y":
            system('clear')
            usercards.clear()
            compcards.clear()
            u()
        elif redo == "n":
            system('clear')
            print("")
            print(" Have a Nice Day ")
            print("")
        else:
            print("Please enter a letter (y) or (n)... ")
            runitback(x)
    else:
        print("Please enter a letter (y) or (n)... ")
        runitback()
start()
