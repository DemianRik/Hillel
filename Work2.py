user_name = input("Введіть ваше ім'я: ")
print("Привіт, ", user_name)

user_num = int(input("Введіть 5-ти значне число: "))

num_1 = user_num % 10
num_2 = user_num // 10 % 10
num_3 = user_num // 100 % 10
num_4 = user_num // 1000 % 10
num_5 = user_num // 10000

print(f"{num_1}{num_2}{num_3}{num_4}{num_5}")
