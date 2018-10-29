room_items = {"floor": "pavimento", "ceiling": "soffitto", "shelf": "scaffale", "wall": "parete", "window": "finestra",
              "door": "porta", "chair": "sedia", "armchair": "poltrona", "couch": "divano", "carpet": "moquette",
              "cushions": "cuscini", "coffee table": "tavolino", "rug": "tappeto", "bed": "letto", "room": "stanza",
              "bathroom sink": "lavabo", "vacuum": "aspirapolvere"}

kitchen_items = {"kitchen": "cucina", "kitchen sink": "lavello", "fork": "forchetta", "spoon": "cuchiaio",
                 "knife": "coltello", "cup": "tazza", "plate": "piatto", "oven": "forno", "stove": "fornelli",
                 "refrigerator": "frigorifero", "microwave": "microonde", "sauce pan": "padella", "pot": "pentola",
                 "bowl": "ciotola"}

food_items = {"garlic": "aglio", "oil": "olio", "basil": "basilico", "cheese": "formaggio",
              "mozzarella": "mozzarella", "parmesan": "parmigiano", "tomato": "pomodoro", "sauce": "salsa",
              "vegetables": "verdura", "fruit": "frutta", "bread": "pane", "grain": "cereali", "liquid": "liquido",
              "powder": "polvere", "cream": "crema"}

ordinal_numbers = {"first": "primo", "second": "secondo", "third": "terzo", "fourth": "quarto", "fifth": "quinto",
                   "sixth": "sesto", "seventh": "septimo", "eighth": "ottavo", "ninth": "nono", "tenth": "decimo",
                   "eleventh": "undicesimo", "twelfth": "dodicesimo", "thirteenth": "tredicesimo",
                   "fourteenth": "quattordicesimo", "fifteenth": "quindicesimo", "sixteenth": "sedicesimo",
                   "seventeenth": "diciasettesimo", "eighteenth": "diciottesimo", "ninteenth": "diciannovesimo",
                   "twentieth": "ventesimo", "twenty-first": "ventunesimo", "twenty-second": "ventiduesimo",
                   "twenty-third": "ventitresimo", "twenty-fourth": "ventiquattresimo",
                   "twenty-fifth": "venticinquesimo", "twenty-sixth": "ventiseiesimo",
                   "twenty-seventh": "ventisettesimo", "twenty-eighth": "ventiottesimo",
                   "twenty-ninth": "ventinovesimo", "thirtieth": "trentesimo", "fourtieth": "quarantesimo",
                   "fiftieth": "cinquantesimo", "sixtieth": "sessantesimo", "seventieth": "settantesimo",
                   "eightieth": "ottantesimo", "nintieth": "novantesimo", "hundredth": "centesimo"}

direct_object_pronouns = {"1st person singular": "mi", "2nd person singular": "ti", "3rd person singular masc.": "lo",
                          "3rd person singular fem.": "la", "1st person plural": "ci", "2nd person plural": "vi",
                          "3rd person plural masc.": "li", "3rd person plural fem.": "le"}

indirect_object_pronouns = {"1st person singular": "mi", "2nd person singular": "ti",
                            "3rd person singular masc.": "gli", "3rd person singular fem.": "le",
                            "1st person plural": "ci", "2nd person plural": "vi", "3rd person plural": "loro"}


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


def kitchen_quiz():
    correct = 0
    wrong = 0
    print("Translate the word into Italian.")
    for item in kitchen_items:
        question = input(f'{item} in Italian is:\n').lower()
        if kitchen_items[item] == question:
            print("Correct!")
            correct += 1
        else:
            print(f'Wrong. Answer is {kitchen_items[item]}')
            wrong += 1
            i = 0
            while i < 10:
                i += 1
                review = input(f'{item} in Italian is:\n').lower()
                if kitchen_items[item] == review:
                    print("Correct!")
                else:
                    print(f'Wrong. Answer is {kitchen_items[item]}')
    else:
        print(f'Results\n'
              f'Correct: {correct}\n'
              f'Wrong: {wrong}\n'
              f'Total: {len(kitchen_items)}')


kitchen_quiz()

