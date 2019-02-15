import random
from pprint import pprint

months_seasons = {"gennaio": "January", "febbraio": "February", "marzo": "March", "aprile": "April", "maggio": "May",
                  "giugno": "June", "luglio": "July", "agosto": "August", "settembre": "September", "ottobre":
                  "October", "novembre": "November", "dicembre": "December", "l'inverno": "winter", "l'estate":
                  "summer", "primavera": "spring", "lo autunno": "fall"}


def quiz(choice):
    correct = 0
    wrong = 0
    print("Translate the word into Italian.")
    for item in choice:
        question = input(f'{item} in Italian is:\n')
        if choice[item] == question:
            print("Correct!")
            correct += 1
        else:
            print(f'Wrong. Answer is {choice[item]}')
            wrong += 1
            i = 0
            while i <= 5:
                i += 1
                review = input(f'{item} in Italian is:\n').lower()
                if choice[item] == review:
                    print("Correct!")
                else:
                    print(f'Wrong. Answer is {choice[item]}')
    else:
        print(f'Results\n'
              f'Correct: {correct}\n'
              f'Wrong: {wrong}\n'
              f'Total: {len(choice)}')


print(len(months_seasons))
randomized = {}
while len(months_seasons) != len(randomized):
    for keys in months_seasons:
        add = random.choice(list(months_seasons))
        if months_seasons[add] not in randomized:
            randomized[add] = months_seasons[add]
pprint(randomized)
print(len(randomized))

