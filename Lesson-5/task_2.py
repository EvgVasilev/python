with open("example.txt", 'r', encoding='utf-8') as example:
    content = example.readlines()
    #print(content)
with open("example.txt", 'r', encoding='utf-8') as file_obj:
    print(f'Количество строк в файле - {len(content)}\n')
    count_words = 1
    for word in content:
        print(word.replace('\n', ''))
        for i in word:
            if i == ' ':
                count_words += 1
        print(f'Количество слов в строке = {count_words}')
        count_words = 1
