import logging

# Настройка логирования
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def add(a, b):
    result = a + b
    logging.info(f"ADD: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"SUBTRACT: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"MULTIPLY: {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logging.error(f"DIVIDE_BY_ZERO: attempted {a} / {b}")
        raise ZeroDivisionError("Ошибка: деление на ноль запрещено!")
    result = a / b
    logging.info(f"DIVIDE: {a} / {b} = {result}")
    return result

def get_number(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Ошибка: нужно вводить числа.")
            logging.warning(f"Invalid input: {s}")

def main():
    print("=== Калькулятор ===")
    a = get_number("Введите первое число: ")
    b = get_number("Введите второе число: ")
    op = input("Введите операцию (+, -, *, /): ")

    try:
        if op == "+":
            res = add(a, b)
        elif op == "-":
            res = subtract(a, b)
        elif op == "*":
            res = multiply(a, b)
        elif op == "/":
            res = divide(a, b)
        else:
            print("Неизвестная операция")
            return
        print("Результат:", res)

    except ZeroDivisionError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
