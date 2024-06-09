def main():
    menu = {
        "кофе": 20.00,
        "чай": 10.00,
        "булочка": 5.00,
        "салат": 30.40,
        "пирожное": 45.50
    }

    total_cost = 0.0
    print()

    try:
        while True:
            dish = input("Блюдо: ")

            if dish in menu:
                total_cost += menu[dish]
            else:
                print("Блюдо не найдено в меню, попробуйте снова.")
    except EOFError:
        pass

    print(f"Сумма:{total_cost:.2f}")

main()
