from core import Coffee


def make_coffee_order():
    coffee_options = ["Капучино", "Латте", "Эспрессо"]
    syrup_options = ["Шоколадный", "Ванильный", "Карамельный", "Без сиропа"]

    print("Выберите тип кофе:")
    for i, coffee in enumerate(coffee_options, 1):
        print(f"{i}. {coffee}")
    coffee_choice = int(input("Введите номер выбранного кофе: ")) - 1

    sugar_choice = input("Добавить сахар? (да/нет): ").lower() == "да"

    print("Выберите сироп:")
    for i, syrup in enumerate(syrup_options, 1):
        print(f"{i}. {syrup}")
    syrup_choice = int(input("Введите номер выбранного сиропа: ")) - 1

    syrup_selected = syrup_options[syrup_choice] if syrup_choice < len(syrup_options) - 1 else None

    coffee = Coffee(coffee_options[coffee_choice], sugar_choice, syrup_selected)
    return coffee


def main():
    coffee_order = make_coffee_order()
    print(coffee_order.get_order_info())


if __name__ == '__main__':
    main()
