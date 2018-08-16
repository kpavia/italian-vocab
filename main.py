room_items = {"floor": "pavimento", "ceiling": "soffitto", "shelf": "scaffale", "wall": "parete", "window": "finestra",
              "door": "porta", "chair": "sedia", "armchair": "poltrona", "couch": "divano", "carpet": "moquette",
              "cushions": "cuscini", "coffee table": "tavolino", "rug": "tappeto", "bed": "letto", "room": "stanza",
              "bathroom sink": "lavabo", "vacuum": "aspirapolvere"}

kitchen_items = {"kitchen": "cucina", "kitchen sink": "lavello", "fork": "forchetta", "spoon": "cuchiaio",
                 "knife": "coltello", "cup": "tazza", "plate": "piatto", "oven": "forno", "stove": "fornelli",
                 "refrigerator": "frigorifero", "microwave": "microonde", "sauce pan": "padella", "pot": "pentola"}

food_items = {"garlic": "aglio", "oil": "olio", "basil": "basilico", "cheese": "formaggio",
              "mozzarella": "mozzarella", "parmesan": "parmigiano", "tomato": "pomodoro", "sauce": "salsa",
              "vegetables": "verdura", "fruit": "frutta", "bread": "pane", "grain": "cereali",
              "liquid": "liquido", "powder": "polvere", "cream": "crema"}


def room_quiz():
    correct = 0
    wrong = 0
    print("Translate the word into Italian.")
    for item in room_items:
        question = input(f'{item} in Italian is:\n').lower()
        if room_items[item] == question:
            print("Correct!")
            correct += 1
        else:
            print(f'Wrong. Answer is {room_items[item]}')
            wrong += 1
            i = 0
            while i < 10:
                i += 1
                review = input(f'{item} in Italian is:\n').lower()
                if room_items[item] == review:
                    print("Correct!")
                else:
                    print(f'Wrong. Answer is {room_items[item]}')
    else:
        print(f'Results\n'
              f'Correct: {correct}\n'
              f'Wrong: {wrong}\n'
              f'Total: {len(room_items)}')




