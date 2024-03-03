print('Программа поиска текста в файле')
import subprocess

def search_word(command, string):
    result = subprocess.run('cat ' + command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(True if string in result.stdout else False)

def returncode_texts(command):
    result = subprocess.run('cat ' + command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.returncode

print('Введите строку текста')
string = input('---> ')

print('Введите путь к файлу')
command = input('---> ')

if string != '' and command != '' and returncode_texts(command) == 0:
    search_word(command, string)
else:
    print('Проверьте введенные данные!')
    
    