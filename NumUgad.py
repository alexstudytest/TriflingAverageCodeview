
import random

word_list = ['математика', 'геометрия', 'информатика', 'программирование', 'питон', 'образование', 'телефон']


    # функция получения случайного слова из списка слов
def get_word():
        word = random.choice(word_list)
        return word.upper()


    # функция получения текущего состояния
def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
        return stages[tries]
def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(word_completion)
        print()

        while not guessed and tries > 0:
            guess = input('Введите букву или слово целиком: ').upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print('Вы уже называли букву', guess)
                elif guess not in word:
                    print('Буквы', guess, 'нет в слове.')
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print('Отличная работа, буква', guess, 'присутствует в слове!')
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i in range(len(word)) if word[i] == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = ''.join(word_as_list)
                    if '_' not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print('Вы уже называли слово', guess)
                elif guess != word:
                    print('Слово', guess, 'не является верным.')
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print('Введите букву или слово.')
            print(display_hangman(tries))
            print(word_completion)
            print()
        if guessed:
            print('Поздравляем, вы угадали слово! Вы победили!')
        else:
            print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')
again = 'д'

while again.lower() == 'д':
        word = get_word()
        play(word)
        again = input('Играем еще раз? (д = да, н = нет):')


"""

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''


n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()


if add_digit.lower() == 'д':
    chars += digits
if add_lowercase.lower() == 'д':
    chars += lowercase_letters
if add_uppercase.lower() == 'д':
    chars += uppercase_letters
if add_punctuation.lower() == 'д':
    chars += punctuation
if remove_badsymbols.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    generate_password(length, chars)
"""


