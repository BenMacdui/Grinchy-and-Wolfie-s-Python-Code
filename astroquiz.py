import random, sys, time, requests, os, re

def clear():
    """This function checks whether we are in windows 'nt' or
    and if so uses cls command to clear the sreen all other
    systems, incl. Mac are based on unix and use clear.
    It will clear the screen nicely"""
    os.system('cls' if os.system == 'nt' else 'clear')
    return

time.sleep(2)
clear()
print("""In this part you will be tested to your limit. Not only do you need to be fast you also have to have some knowledge of the night sky.

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


# prints question and answer


astroquiz = requests.get(url)



score = 0
a = astroquiz.text
x = a.split('--')
subList = [x[n:n+2] for n in range(0, len(x), 2)]
total_elapsed_time = 0
while total_elapsed_time <= 15:
    quiz = random.choice(subList)
    prompt = "enter a or b or c >>>  "
    print("Question coming up...")
    time.sleep(1)
    print()
    question = quiz[0]
    print()
    print()
    quest = re.split(r'\s{2,}', question)
    print()
    print(quest[0],'\n\n')
    time.sleep(2)
    print(quest[1])
    print()
    print()
    time.sleep(2)
    start_time = time.time()
    answer = input(prompt).lower().split()
    elapsed_time = time.time() - start_time
    if elapsed_time > 5 and score < 20:
        elapsed_time = round(elapsed_time, 0)
        total_elapsed_time = elapsed_time + total_elapsed_time
        print()
        print(f"You took {elapsed_time} seconds and your score is {score}. You are too slow and have not enough points to continue \U0001f608")
        print()
        input("Would you like to appeal against the decision? Press enter")
        print()
        print("I bet you would...\n\n \U0001f608 hmm let me think about it...")
        print()
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
            print(f"Pease try again. Good luck next time {player_name.title()} \U0001f600")
        else:
            print()
            r = 20 - score
            if r != 0:

                print(f"I will give you {r} points and you will live forever, cause you so nice \U0001f607")
                print()
                print("bye bye")
                print("thanks for playing")
                print("\U0001f607")
                time.sleep(2)
                sys.exit()
            else:
                print()
                print("You have scored zero points so far. Sorry I would like to help and I could have had you scored some points. Now you have to go. Sorry \U0001f61e")
                print()
                time.sleep(2)
                sys.exit()
    else:
        print()
        x = quiz[1]
        y = x.split()
        print(y[-1])
        print()
        if answer[-1]== y[-1]:
            print()
            print("correct")
            print()
            time.sleep(2)
            print("hmm you seem too good! Have you had any help? \U0001f914")
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
time.sleep(4)
print("\U0001f600")
time.sleep(2)
clear()

