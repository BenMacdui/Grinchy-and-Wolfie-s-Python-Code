def German_word():
    g_list = {'Eier': 'eggs',
              'Brot': 'bread',
              'Marmelade': 'jam',
              'Morgen': 'morning',
              'Guten Tag': 'hello',
              'Blumenkohl': 'cauliflower',
              'Blume' : 'flower',
              'Klassenzimmer' : 'class room',
              'Haribo' :  'haribo',
              'Haus': 'house',
              'spielen' : 'play',
              'Spinne' : 'spider',
              'Nachmittag' : 'afternoon'}
    import random
    correct = 0
    wrong = 0
    tries = 3
    while tries > 0:
        tries -= 1
        keywlist = list(g_list.keys())
        random.shuffle(keywlist)

        for keyword in keywlist:
            display ="{}"
        print("")
        #print(display.format(keyword))

        userinput_answer = input(f"Tell me the English word for: {keyword}: ").lower()
        #print(g_list[keyword])
        print("")

        if userinput_answer == (g_list[keyword]):
            print("Correct \U0001f601")
            correct += 1
        else:
            print("Wrong \U0001F612")
            wrong += 1
            print("*" * 25)
    print()
    print('*'*25)
    display = "Score: {} correct and {} wrong"
    print(display.format(correct,wrong))
    print('*'*25)

    print()
    if correct > 2:
        print('The ladies got it right and were allowed into the house')
    else:
        print('The ladies were turned into stone')
    return

