
def menu():
  print("Выбери действие:", "1 - перевод из двоичной в десятиричную", "2 - перевод из десятиричной в двоичную", "3 - перевод из десятиричной в шестнаднацитиричную", "4 - перевод из шестнадцатиричной в десятиричную", sep="\n")
  a = int(input())
  if a == 1:
    convertToDecimal(input("Введи число: "))
  elif a == 2:
    convertToBinary(int(input('Введи число: ')))
  elif a == 3:
    convertToHexadecimal(int(input('Введи число: ')))
  elif a == 4:
    ToDecimal(input("Введи число: "))

#Перевод из двоичной в десятиричную
def convertToDecimal(num: str):
  #num = input()
  convert = 0
  for i in range(0, len(num)):
    convert += int(num[i]) * 2 ** int(i)
  print(convert)

#Перевод из десятиричной в двоичную
def convertToBinary(num: int):
  #num = int(input())
  convert = ""
  while num > 0:
    convert += str(num % 2)
    num = num // 2
  print(convert[::-1])

#Перевод из десятиричной в шестнадцатиричную
def convertToHexadecimal(decimal_number: int):
  #decimal_number = int(input("Введите десятичное число: "))
  hexadecimal_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
  hexadecimal_number = ""
  while decimal_number > 0:
    remainder = decimal_number % 16  # Получаем остаток от деления на 16
    hexadecimal_digit = hexadecimal_digits[remainder]  # Получаем шестнадцатеричную цифру
    hexadecimal_number = hexadecimal_digit + hexadecimal_number  # Добавляем цифру в начало шестнадцатеричного числа
    decimal_number //= 16  # Выполняем целочисленное деление на 16
  print("Шестнадцатеричное число:", hexadecimal_number)


#Перевод из шестнадцатиричной в десятирич
def ToDecimal(num: str):
  #num = input()
  convert = 0
  for i in range(0, len(num)):
    convert += int(num[i]) * 16 ** int(i)
  print(convert)


menu()