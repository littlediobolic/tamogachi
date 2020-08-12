#!/usr/bin/env python
#Written by Diobolic

import time, threading

#Main Gachi class
class gachi:


    def __init__(self, name):
        self.name = name.capitalize()
        self.health = 1
        self.hunger = 0

    #Gives the gachi health and does some chesks to ensure numbers are in range
    def feed(self):
        self.hunger -= 3
        self.health += 2

        if self.hunger < 0:
            self.hunger = 0

        if self.health > 10:
            self.health = 10

    #Does damage to gachi
    def harm(self, damage):
        self.health -= damage

        if self.health <= 0:
            print("DEAD!")
            self.health = 0
            pause()

def pause():
    input("Press enter to continue...")
    print("\n\n")

#Create gachi with name
print("Welcome to Tamogachi!")
player_gachi = gachi(input("Please name your gachi: "))

#Main loop
def main():
    loop = True
    global timer_thread
    global run_timer

    while loop:
        print("What would you like to do: ")
        print("1 - feed gachi")
        print("2 - show gachi health")
        print("3 - show gachi hunger")
        print("8 - damage gachi")
        print("9 - exit")

        print("\n")
        
        choice = input("Select 1-9: ")
        
        #Verify entry is an int
        try:
            choice = int(choice)
        except:
            print("An error occured. Please enter a number between 1 and 9.")

        if choice == 1: #feed gachi
            player_gachi.feed()
            print("Yum!!")
            pause()
        elif choice == 2: #get health
            print(player_gachi.name + "'s current health is: " + str(player_gachi.health))
            pause()
        elif choice == 3:#get hunger
            print(player_gachi.name + "'s current hunger is: " + str(player_gachi.hunger))
            pause()
        elif choice == 8: #harm gachi
            player_gachi.harm(3)
        elif choice == 9: #close
            timer_thread.cancel()
            run_timer = False
            print("Goodbye!")
            exit()
        else:
            print("Invalid Option...")

#Main timer fucntion that is called by timer thread
def main_timer():
    global run_timer
    last_time = time.time()

    while run_timer == True:
        
        #If number of seconds pass since last check, do thing
        if abs(last_time - time.time()) >= 15:
            player_gachi.harm(1)
            print("\nHURT BY 1\n")
            last_time = time.time()

#Start the timer thread
run_timer = True
timer_thread = threading.Timer(1, main_timer)
timer_thread.start()

#Call main loop
main()

