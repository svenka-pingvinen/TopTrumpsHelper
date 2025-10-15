print("welcome to the toptrumps helper!")
card = input("what card do you have? ")
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
card29 = {"Name": "Chihuahua", "Size": 1, "Rarity" 4, "Good Temper" :2, "Cuteness" :29, "Top Trumps Rating" :85}
card30 = {"Name": "Scooby Doo", "Size": 6, "Rarity" :10, "Good Temper" :5, "Cuteness" :25, "Top Trumps Rating" :85}

cardlist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12]

for dog in cardlist:
    if dog["Name"] == card:
        print(dog)
        sizewin = 0
        raritywin = 0
        temperwin = 0
        cutenesswin = 0
        ttrwin = 0
        for opponent in cardlist:
            if opponent["Name"] != card:
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
        elif highestvalue == raritywin:
            print("you should choose Rarity")
        elif highestvalue == temperwin:
            print("you should choose Good Temper")
        elif highestvalue == cutenesswin:
            print("you should choose Cuteness")
        elif highestvalue == ttrwin:
            print("you should choose Top Trumps Rating")