def convert_date(old_date):
    month_dict = {
        "январь": "01", "февраль": "02", "март": "03", "апрель": "04",
        "май": "05", "июнь": "06", "июль": "07", "август": "08",
        "сентябрь": "09", "октябрь": "10", "ноябрь": "11", "декабрь": "12"
    }

    parts = old_date.split()

    if len(parts) == 1 and '.' in old_date:
        day, month, year = old_date.split('.')
        try:
            day = int(day)
            month = int(month)
            year = int(year)

            return f"{year:04}-{month:02}-{day:02}"
        except ValueError:
            return None

    elif len(parts) == 3:
        day, month_str, year = parts
        try:
            day = int(day)
            year = int(year)

            if month_str.lower() in month_dict:
                month = month_dict[month_str.lower()]
                return f"{year:04}-{month}-{day:02}"
            else:
                return None
        except ValueError:
            return None
    else:
        return None

def main():
    while True:
        old_date = input("Дата: ")
        new_date = convert_date(old_date)
        if new_date:
            print(new_date)
            break
        else:
            print()

main()
