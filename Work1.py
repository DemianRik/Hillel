user_name = input("Введіть ваше ім'я: ")
print("Привіт, ", user_name)

user_num = int(input("Введіть 4-х значне число: "))

num_1 = user_num % 10
num_2 = user_num // 10 % 10
num_3 = user_num // 100 % 10
num_4 = user_num // 1000

print(num_4)
print(num_3)
print(num_2)
print(num_1)
