try:
    with open('Кинотеатр.txt', 'r') as file:
        lines = file.readlines()
except IOError as e:
        print(f"Ошибка при открытии файла Кинотеатр.txt: {e}")
        lines = []

if not lines:
    print("Файл 'Кинотеатр.txt' пуст. Нет данных для обработки.")
else:
    try:
        day = int(input("Введите день проведения сеанса: "))
        month = int(input("Введите месяц проведения сеанса: "))
        year = int(input("Введите год проведения сеанса: "))
    except ValueError:
        print("Ошибка: Некорректный ввод. Введите целые числа для дня, месяца и года.")
    else:
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900 or year > 2100:
            print("Ошибка: Некорректная дата. Пожалуйста, введите корректные значения для дня, месяца и года.")
        else:
            target_date = f"{day:02d}.{month:02d}.{year:04d}"
            cheap_movies = []
            movies_by_date = []

            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    movie_name = parts[0]
                    date = parts[1]
                    ticket_price_str = parts[2]
                    try:
                        ticket_price = float(ticket_price_str)
                    except ValueError:
                        print(f"Ошибка при обработке строки: {line}. Некорректный формат цены.")
                        continue

                    if ticket_price < 15:
                        cheap_movies.append(movie_name)

                    if date == target_date:
                        movies_by_date.append(movie_name)
                else:
                    print(f"Ошибка при обработке строки: {line}. Некорректное количество элементов.")

            print("\nФильмы с билетами меньше 15 рублей:")
            for movie in cheap_movies:
                print(movie)

            print("\nФильмы на определенную дату:")
            for movie in movies_by_date:
                print(movie)
