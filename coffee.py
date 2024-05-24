def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Нужная сумма: {amount_due}")
        coin = int(input("Вставьте монету: "))
        if coin == 5 or coin == 10 or coin == 20 or coin == 50:
            amount_due -= coin
    print(f"Ваша сдача: {-amount_due}")

main()
