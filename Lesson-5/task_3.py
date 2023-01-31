translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('input_text.txt', encoding='utf-8') as text_eng:
    for line in text_eng:
        for key in translate.keys():
            line = line.replace(key, translate[key])
        print(line)
        with open('output_file.txt', 'a') as text_rus:
            text_rus.write(f'\n{line}\n')
