import random

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


# quiz(months_seasons)

# print(len(months_seasons))
# print(random.choice(list(months_seasons)))

new_dict = {}
add = random.choice(list(months_seasons))
new_dict = new_dict[months_seasons.items()]
print(new_dict)

# for k, v in months_seasons.items():
#     print(k, v)


# TODO: figure out how to randomize the quiz (maybe create a random dict from the original dict?)
