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

Each question will yield 5 points.

Good luck \U0001f600""")
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
    if elapsed_time > 5:
        elapsed_time = round(elapsed_time, 0)
        total_elapsed_time = elapsed_time + total_elapsed_time
        print(total_elapsed_time)
        print(f"You took {elapsed_time} seconds. Too slow")
        print("The end for you my friend")
        print()
        print("Try again soon")
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
            time.sleep(2)
            clear()
            sys.exit()
time.sleep(2)
print('goodbye')
print()
time.sleep(2)
print(f'You have used up a total of {total} seconds, which over your allowed time allowance.')
print()
print(f'Your score is: {score}')
if score >= 20:
    print("Well done you live forever")
else:
    print("You will be turned to stone")
print()
print("the story goes on")
time.sleep(4)
print("\U0001f600")
time.sleep(2)
clear()

