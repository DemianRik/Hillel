a = float(input("Перше число: "))
b = float(input("Друге число: "))
c = input("Що робимо? (+, -, *, /) ")

if c == '+':
    print("Результат:", a + b)
elif c == '-':
    print("Результат:", a - b)
elif c == '*':
    print("Результат:", a * b)
elif c == '/':
    if b == 0:
        print("Помилка: ділення на нуль!")
    else:
        print("Результат:", a / b)