my_file = open('text.txt', 'w', encoding='utf-8')
text = []
while True:
    line = input('Введите текст: ')
    if line == '':
        print(line)
        break
    else:
        text.append(line + '\n')
my_file.writelines(text)
my_file.close()

with open('text.txt', 'r', encoding='utf-8') as my_text:
    content = my_text.readlines()
    print(content)

with open('text.txt', 'r', encoding='utf-8') as my_text:
    for line in my_text:
        print(line)

