print('Программа поиска текста в файле')
import subprocess

def search_word(command, string):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(True if string in result.stdout else False)

print('Введите строку текста')
string = input('---> ')

print('Введите команду и путь к файлу')
command = input('---> ')

if string != '' and command != '':
    search_word(command, string)
else:
    print('Одна или обе из введенных строк оказались пустыми!')