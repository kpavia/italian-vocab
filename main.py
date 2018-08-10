words = {"floor": "pavimento", "ceiling": "soffitto", "shelf": "scaffale", "wall": "parete", "window": "finestra",
         "door": "porta", "chair": "sedia", "armchair": "poltrona", "couch": "divano", "carpet": "moquette",
         "cushions": "cuscini", "coffee table": "tavolino", "rug": "tappeto", "bed": "letto", "room": "stanza"}


def quiz():
    correct = 0
    wrong = 0
    print("Translate the word into Italian.")
    for item in words:
        question = input(f'{item} in Italian is:\n').lower()
        if words[item] == question:
            print("Correct!")
            correct += 1
        else:
            print(f'Wrong. Answer is {words[item]}')
            wrong += 1
            i = 0
            while i < 10:
                i += 1
                review = input(f'{item} in Italian is:\n').lower()
                if words[item] == review:
                    print("Correct!")
                else:
                    print(f'Wrong. Answer is {words[item]}')
    else:
        print(f'Results\n'
              f'Correct: {correct}\n'
              f'Wrong: {wrong}\n'
              f'Total: {len(words)}')


quiz()

