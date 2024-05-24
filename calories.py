def main():
    fruits = {"Apple": 130, "Avocado": 50,
        "Banana": 110, "Grapes": 90,
            "Kiwifruit": 90, "Lemon": 15,
                "Lime": 20, "Orange": 80,
                    "Peach": 60, "Pear": 100,
                        "Pineapple": 50, "Plums": 70,
                            "Honeydew Melon": 50, "Cantaloupe": 50,
                                "Grapefruit": 60, "Nectarine": 60,
                                    "Strawberries": 50, "Sweet Cherries": 100,
                                        "Tangerine": 50, "Watermelon": 80}
    f = input("Фрукт: ")
    if f in fruits:
        print("Калории:",fruits[f])

main()
