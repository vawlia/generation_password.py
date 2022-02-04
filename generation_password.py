import random
def generate_password(length_password, chars):
    password = ''
    for i in range(length_password):
        password += random.choice(chars)
    return password


numbers_passwords = int(input('Введите количество паролей'))  #спрашиваем пользователя про количесво паролей
length_password = int(input('Введите длину пароля'))  #спрашиваем пользователя про длину пароля
digits = '0123456789' #список символов
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
numbers_symbol = input('Нужны в пароле числа? (y/n)')  #спрашиваем пользователя про числовые значения в пароле
low_symbol = input('Нужны в пароле строчные буквы? (y/n)')  #спрашиваем пользователя про строчные значения в пароле
up_symbol = input('Нужны в пароле заглавные буквы?(y/n)')  #спрашиваем пользователя про заглавные значения в пароле
punctuation_symbol = input('Нужны в пароле спец знаки(y/n)')  #спрашиваем пользователя про символьные значения в пароле

if numbers_symbol == 'y':
    chars += digits
if low_symbol == 'y':
    chars += lowercase_letters
if up_symbol == 'y':
    chars += uppercase_letters
if punctuation_symbol == 'y':
    chars += punctuation

for _ in range(numbers_passwords):
    print(generate_password(length_password, chars))
