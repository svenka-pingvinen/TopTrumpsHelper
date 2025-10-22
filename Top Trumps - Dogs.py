print("welcome to the toptrumps helper!")
gamefinished = False
while gamefinished == False:
    cardsize = input("what size is your dog card? ")
    card1 = {"Name": "Staffordshire Bull Terrier", "Size": 3, "Rarity" :4, "Good Temper" :5, "Cuteness" :14, "Top Trumps Rating" :60}
    card2 = {"Name": "Husky", "Size": 4, "Rarity" :6, "Good Temper" :5, "Cuteness" :22, "Top Trumps Rating" :88}
    card3 = {"Name": "Beagle", "Size": 2, "Rarity" :2, "Good Temper" :3, "Cuteness" :20, "Top Trumps Rating" :49}
    card4 = {"Name": "Border Collie", "Size": 3, "Rarity" :8, "Good Temper" :5, "Cuteness" :19, "Top Trumps Rating" :86}
    card5 = {"Name": "German Shepherd", "Size": 4, "Rarity": 1, "Good Temper" :4, "Cuteness" :15, "Top Trumps Rating" :51}
    card6 = {"Name": "Shih Tzu", "Size": 2, "Rarity" :7, "Good Temper" :5, "Cuteness" :25, "Top Trumps Rating" :35}
    card7 = {"Name": "Maltese", "Size": 1, "Rarity" :7, "Good Temper" :2, "Cuteness" :22, "Top Trumps Rating" :66}
    card8 = {"Name": "Pug", "Size": 1, "Rarity" :2, "Good Temper" :4, "Cuteness" :27, "Top Trumps Rating" :40}
    card9 = {"Name": "Alaskan Malamute", "Size": 5, "Rarity" :7, "Good Temper" :2, "Cuteness" :15, "Top Trumps Rating" :80}
    card10 = {"Name": "Labrador", "Size": 4, "Rarity" :2, "Good Temper" :5, "Cuteness" :27, "Top Trumps Rating" :95}
    card11 = {"Name": "Pembroke Welsh Corgi", "Size":1, "Rarity" :4, "Good Temper" :3, "Cuteness" :18, "Top Trumps Rating" :65}
    card12 = {"Name": "Poodle", "Size": 3, "Rarity" :6, "Good Temper" :2, "Cuteness" :27, "Top Trumps Rating" :60}
    card13 = {"Name": "Border Terrier", "Size": 2, "Rarity" :6, "Good Temper" :3, "Cuteness" :10, "Top Trumps Rating" :40}
    card14 = {"Name": "Dalmatian", "Size": 4, "Rarity" :6, "Good Temper" :3, "Cuteness" :16, "Top Trumps Rating" :80}
    card15 = {"Name": "Cocker Spaniel", "Size": 3, "Rarity" :2, "Good Temper" :5, "Cuteness" :21, "Top Trumps Rating" :49}
    card16 = {"Name": "Stray Dog", "Size": 3, "Rarity" :5, "Good Temper" :2, "Cuteness" :15, "Top Trumps Rating" :100}
    card17 = {"Name": "Saint Bernard", "Size": 6, "Rarity" :8, "Good Temper" :4, "Cuteness" :25, "Top Trumps Rating" :94}
    card18 = {"Name": "Great Dane", "Size": 6, "Rarity" :8, "Good Temper" :3, "Cuteness" :20, "Top Trumps Rating" :50}
    card19 = {"Name": "Bulldog", "Size": 3, "Rarity" :4, "Good Temper" :4, "Cuteness" :25, "Top Trumps Rating" :10}
    card20 = {"Name": "Dachshund", "Size": 2, "Rarity" :5, "Good Temper" :2, "Cuteness" :29, "Top Trumps Rating" :67}
    card21 = {"Name": "Labrador Retriever", "Size": 4, "Rarity" :1, "Good Temper" :5, "Cuteness" :28, "Top Trumps Rating" :90}
    card22 = {"Name": "Basset Hound", "Size": 3, "Rarity" :4, "Good Temper" :3, "Cuteness" :27, "Top Trumps Rating" :55}
    card23 = {"Name": "Rough Collie", "Size": 4, "Rarity" :7, "Good Temper" :5, "Cuteness" :27, "Top Trumps Rating" :45}
    card24 = {"Name": "Golden Retriever", "Size": 4, "Rarity" :2, "Good Temper" :5, "Cuteness" :27, "Top Trumps Rating" :75}
    card25 = {"Name": "Boxer", "Size": 4, "Rarity" :5, "Good Temper" :5, "Cuteness" :26, "Top Trumps Rating" :19}
    card26 = {"Name": "Afghan Hound", "Size": 4, "Rarity" :9, "Good Temper" :3, "Cuteness" :29, "Top Trumps Rating" :25}
    card27 = {"Name": "Dobermann Pinscher", "Size": 4, "Rarity" :4, "Good Temper" :3, "Cuteness" :18, "Top Trumps Rating" :50}
    card28 = {"Name": "Greyhound", "Size": 4, "Rarity" :6, "Good Temper" :5, "Cuteness" :27, "Top Trumps Rating" :25}
    card29 = {"Name": "Chihuahua", "Size": 1, "Rarity": 4, "Good Temper" :2, "Cuteness" :29, "Top Trumps Rating" :85}
    card30 = {"Name": "Scooby Doo", "Size": 6, "Rarity" :10, "Good Temper" :5, "Cuteness" :25, "Top Trumps Rating" :85}

    cardlist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30]

    doglist = []
    for dog in cardlist:
        if dog["Size"] == int(cardsize):
            print(dog)
            doglist.append(dog)

    print (doglist)
    print ()
    index = 1
    for dog in doglist:
        print(str(index) + ". " + dog["Name"])
        index += 1
    cardchoice = input("which card do you have? (type the number) ")
    cardchoice = int(cardchoice)
    dog = doglist[cardchoice - 1]
    sizewin = 0
    raritywin = 0
    temperwin = 0
    cutenesswin = 0
    ttrwin = 0
    for opponent in cardlist:
        if opponent["Name"] != dog["Name"]:
            if dog["Size"] > opponent["Size"]:
                sizewin += 1
            if dog["Rarity"] > opponent["Rarity"]:
                raritywin += 1
            if dog["Good Temper"] > opponent["Good Temper"]:
                temperwin += 1
            if dog["Cuteness"] > opponent["Cuteness"]:
                cutenesswin += 1
            if dog["Top Trumps Rating"] > opponent["Top Trumps Rating"]:
                ttrwin += 1
    highestvalue = max(sizewin, raritywin, temperwin, cutenesswin, ttrwin)
    if highestvalue == 0:
        print("you can't win with this card")
    elif highestvalue == sizewin:
        print("you should choose Size")
        print("your chance of winning is " +str(int(round((sizewin/29)*100,0))) + "%")
    elif highestvalue == raritywin:
        print("you should choose Rarity")
        print("your chance of winning is " +str(int(round((raritywin/29)*100,0))) + "%")
    elif highestvalue == temperwin:
        print("you should choose Good Temper")
        print("your chance of winning is " +str(int(round((temperwin/29)*100,0))) + "%")
    elif highestvalue == cutenesswin:
        print("you should choose Cuteness")
        print("your chance of winning is " +str(int(round((cutenesswin/29)*100,0))) + "%")
    elif highestvalue == ttrwin:
        print("you should choose Top Trumps Rating")
        print("your chance of winning is " +str(int(round((ttrwin/29)*100,0))) + "%")
    playagain = input("do you want to play again? (yes/no) ")
    if playagain == "no":
        gamefinished = True
        print("thanks for playing!")

    