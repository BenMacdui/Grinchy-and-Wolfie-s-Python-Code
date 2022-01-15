import random, sys, time, requests, os, re

def clear():
    """This function checks whether we are in windows 'nt' or
    and if so uses cls command to clear the sreen all other
    systems, incl. Mac are based on unix and use clear.
    It will clear the screen nicely"""
    os.system('cls' if os.system == 'nt' else 'clear')
    return

def cor():
    if correct == 1:
        print("Hmm... did you have any help? \U0001f914")
    elif correct == 2:
        print("Hmm... I don't believe you. Surley you had help \U0001f914")
    elif correct == 3:
        print("You not telling the truth. Nobody is that good \U0001f914")
    elif correct == 5:
        print("Either you are a genius or you are cheating  \U0001f914" )
    elif correct == 7:
        print("I think I re-write the game  \U0001f914")
    return



time.sleep(2)
clear()
print("""In this part you will be tested to your limit.

Not only do you need to be fast you also have to have some knowledge of the night sky.

You have 5 seconds to answer each question and 15 seconds overall to accumulate 20 points or more.

The game will end if you answer a question wrong or if you don't accumulate 20 points or more.

Each question will yield 5 points.""")
print()
time.sleep(4)
print()
player_name = input("Enter your name please >>>  ").lower()
print(f"Good luck {player_name.title()} \U0001f600")
print()
print()
input('press enter to continue >>>')
url = "https://raw.githubusercontent.com/BenMacdui/Grinchy-and-Wolfie-s-Python-Code/main/astronomyquiz.txt"



# get my text file from Github as specified above in the URL variable
astroquiz = requests.get(url)


# set the score variable to zero
score = 0
correct = 0

# we now split the text fill into seperate list items.
a = astroquiz.text
x = a.split('--')

# the next line will take 2 items of the list x, and put them
# into a seperate list of lists.
# for a detailed explanation of the code see my adventure game

subList = [x[n:n+2] for n in range(0, len(x), 2)]


# set the total elapsed time variable to zero
total_elapsed_time = 0

# Here we run the major while loop to determine when the total time is up.
# Total time is set to 15 seconds

while total_elapsed_time <= 15:
# use random modul to make a random choic of the questions
    quiz = random.choice(subList)
    prompt = "enter a or b or c >>>  "
    print("Question coming up...")
    time.sleep(1)
    print()
    question = quiz[0]
    print()
    print()
# we split question  where we have 2 or more spaces, so that
# we can print them on two lines.
    quest = re.split(r'\s{2,}', question)
    print()
    print(quest[0],'\n\n')
    time.sleep(2)
    print(quest[1])
    print()
    print()
    time.sleep(2)
# we start the timer.It measures the difference between the start of the input and users
# actual input. If this time is over 5 seconds the user gets and appropriate response
    start_time = time.time()
    answer = input(prompt).lower().split()
    elapsed_time = time.time() - start_time
    if elapsed_time > 5 and score < 20:
        elapsed_time = round(elapsed_time, 0)
        total_elapsed_time = elapsed_time + total_elapsed_time
        print()
        print(f"""You took {elapsed_time} seconds and your score is {score}. You are too slow and have not enough points to continue \U0001f608""")
        print()
        input("Would you like to appeal against the decision? Press enter")
        print()
        print("I bet you would...\n\n \U0001f608 hmm let me think about it...")
        print()

# we put in some fun stuff. the player might get the decision to end
# overturned by an appeal decision made by random.choice

        print("decision is been discussed behing closed doors between \U0001f608 and \U0001f607" )
        time.sleep(4)
        print()
        print("still waiting...")
        time.sleep(3)
        decision = ["Sorry... no can do \U0001f608... the decision has been made. You a gonna...\U0001f608","Today is your lucky day. I will let you have it, cause you so nice \U0001f607", "Sorry no decision could be reached ..."]
        print()
        judge = random.choice(decision)
        time.sleep(2)
        print()
        print(judge)
        if judge == decision[0]:
            print("The end for you my friend")
            print(f"Try again soon {player_name.title()}")
            sys.exit()
            time.sleep(2)
            sys.exit()
        elif judge == decision[-1]:
            print()
            print(f"Please try again. Good luck next time {player_name.title()} \U0001f600")
            print()
            time.sleep(2)
            sys.exit()
        else:
            print()
            if score > 0 and score < 20:
                r = 20 - score

                print(f"I will give you {r} points and you will live forever, cause you so nice \U0001f607")
                print()
                print("bye bye")
                print("thanks for playing")
                print("\U0001f607")
                time.sleep(2)
                sys.exit()
            else:
                input("Enter to continue >>>")
                print()
                print("Oh no! I just see that you have scored zero points so far. Sorry I would like to help and I could have, had you scored some points. Unfortunatly now you have to go. It breaks my heart. Sorry \U0001f61e")
                print()
                time.sleep(2)
                print("\U0001f608")
                time.sleep(1)
                clear()
                sys.exit()
    else:
        print()
        x = quiz[1]
        y = x.split()
        print(y[-1])
        print()
        if answer[-1]== y[-1]:
            correct += 1
            print()
            print("correct")
            print()
            time.sleep(2)
            cor()
            print()
            input("press enter to continue >>>")
            total_elapsed_time = elapsed_time + total_elapsed_time
            total = round(total_elapsed_time, 0)
            print()
            print(f"Total seconds so far...{total}")
            print()
            score = score + 5
        else:
            print("Wrong answer")
            print()
            print("Try again soon \U0001f600")
            print()
            print()

            print("The end for you my friend")
            print("thanks for playing")
            time.sleep(3)
            input('enter to continue>>>')
            print()
            print(f"\U0001f608. See you around {player_name.title()}")
            print()
            time.sleep(2)
            clear()
            sys.exit()
time.sleep(2)
print('goodbye')
print()
time.sleep(2)
print(f'You have used up a total of {total} seconds, which is over your allowed time allowance. \U0001f608')
print()
print(f'Your score is: {score} points')
print()
if score >= 20:
    print("Well done you live forever")
    print()
    print(f"Your total is {score} points")
    print()
    print("We think you are a genius \U0001f600")
    print()
    time.sleep(4)
else:
    print("You will be turned to stone \U0001f608")
print()
print("the story goes on")
input('enter to continue')
time.sleep(4)
print("\U0001f600")
time.sleep(2)
clear()


# The next part

print("""the two lovely ladies are on there way and the come to a cross road.

To the right of the cross roads across the field was a cave that looked warm and

welcoming.

In the centre of the cross road stood an old, old oak. It was more than 1000 years old.

On one of its branches sat a crow. The oak spoke in a deep voice to the two lovely ladies

'You did not score enough points and are lucky to still be alive.

You will not be able to choose on your own which path to go. The crow will choose.

One path will lead to the gates of hell and the other through the tunnel of fire.

Or you can go to the nice cave but Obirah is watching the entrance to the cave and he

will challenge you to a duell.

The crow will determing your fate. """)
print()
print()

input("entert to continue >>>")

ch = ["Gates of Hell", "Tunnel of Fire", "Cave"]

fate = random.choice(ch)

if fate == "Gates of Hell":
    print("You will be banished to hell where you sweat in the kitchen for eternity")
    print("\U0001f608 but I have a big heart and give you one more chance to escape...")
    print("...tho I am not sure you deserve it...\U0001f914")
    print()
    print("you need to answer a tough riddle: ")
    input("enter to continue")
    ri = "the more you take the more you leave behind"
    ans = ['finger print', 'fingerprint', 'fingerprints']
    print()
    print(ri)
    time.sleep(2)
    start_time = time.time()
    answ = input(f"what's your answer, {player_name}? >>>  " )
    elapsed_time = time.time() - start_time
    if elapsed_time > 5:
        print()
        print("The end my friend. You were too slow \U0001f608")
        print()
        time.sleep(2)
        sys.exit()
    elif answ in ans:
        print("you were lucky this time and escape from the Gates of Hell")
        time.sleep(2)
        sys.exit()

# Tunnel of fire
if fate == "Tunnel of Fire":
    print("You will vanish in the tunnel of fire. There is no way out unless you can answer the next question")
    print()
    time.sleep(2)
    print("There is a time limit on the answer. So you have to be quick \U0001f608")
    print()
    time.sleep(2)
    input('When ready press enter')
    print()
    print("A mobile phone and a case for it cost £110 in total. \nThe mobile phone costs £100 more than the phone case. How much was the mobile phone?")
    print()
    print()
    print('a)£100 b)£105 c)£102')
    print()
    time.sleep(2)
    start_time = time.time()
    answ = input(f"what's your answer, {player_name}? >>>  " )
    elapsed_time = time.time() - start_time
    if elapsed_time > 3:
          print()
          print("Too slow. You will vanish in the Tunnel of Fire")
    else:
          print("you got away with it. I will get you next time \U0001f608")
          print()
          print("The story will continue")
          print()
          time.sleep(2)
          sys.exit()
# Cave
if fate == "Cave":
    print("""The ground shook as Obirah landed right in front of the cave.

    I am guarding the cave and won't

    let you in unless you draw faster than me.

    Watch out on the screen for the word draw when it appears both you and I will draw

    and whoever is faster wins.

    You press the enter key to draw once the word draw appears on the screen.

    But do not press enter before or you loose.

    Are you ready?

    You better be. """)
    print()
    print()
    time.sleep(2)
    input("when you ready press enter to start the draw")
    print()
    time.sleep(2)
    clear()
    time.sleep(2)
    print()
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()  # This function call doesn't return until Enter is pressed.
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # If the player pressed Enter before DRAW! appeared, the input()
        # call returns almost instantly.
         print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > 0.3:
         timeElapsed = round(timeElapsed, 4)
         print('You took', timeElapsed, 'seconds to draw. Too slow!')
         print("You have to move on")
         time.sleep(3)
         print()
         print("The end my friend")
         time.sleep(1)
         clear()
         sys.exit()
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw.')
        print('You are faster than me! You win!')
        print("I will get you next time")
        print("The story continues")
        time.sleep(3)
        clear()
        sys.exit()
