try:
    with open('F1.txt', 'w') as f1:
        print("Введите данные для файла F1. Для завершения введите пустую строку:")
        while True:
            line = input()
            if not line:
                break
            f1.write(line + '\n')
except IOError as e:
    print(f"Ошибка при открытии файла F1.txt: {e}")

try:
    with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
        first_line = f1.readline().strip().split()
        if not first_line:
            print("Файл F1.txt пуст. Нет данных для обработки.")
        else:
            f1.seek(0)
            for line in f1:
                words = line.strip().split()
                if not any(word in first_line for word in words):
                    f2.write(line)
except IOError as e:
    print(f"Ошибка при открытии/записи файлов: {e}")

try:
    with open('F2.txt', 'r') as f2:
        first_line_f2 = f2.readline().strip()
        if not first_line_f2:
            print("Файл F2.txt пуст. Нет данных для обработки.")
        else:
            consonants_count = sum(1 for char in first_line_f2 if char.isalpha() and char.lower() not in 'aeiou')
            print(f"Количество согласных в первой строке файла F2: {consonants_count}")
except IOError as e:
    print(f"Ошибка при открытии файла F2.txt: {e}")
