def camel_to_snake(name):
    snake_case = []

    for char in name:
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        else:
            snake_case.append(char)

    return ''.join(snake_case).lstrip('_')

def main():
    camel_case = input("Верблюжий стиль: ")

    snake_case = camel_to_snake(camel_case)

    print(f"{snake_case}")


main()
