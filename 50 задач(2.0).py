#1
# phrases = input('Напишите слова через запятую, каждое слово с большой буквы: ')
# phrases = phrases.split(', ')
# words = []
# wonderful = ["Канделябр","Пантограф","Хьюмидор","Пудромантель","Пендельтюр","Скареда","Пипидастр","Пертурбация","Зряшный"]
# for word in phrases:
#     for wond_w in wonderful:
#         if word == wond_w:
#             words.append(wond_w)
# words.sort()
# print(words)

#2
# how1 = input("Введите первое число предела: ")
# how2 = input('Введите последнее число предела:')
# num1 = int(how1)
# num2 = int(how2)
# nums = []
# while num1 <= num2:
#     if num1 % 2!=0 and num1 % 3 != 0 and num1 % 5!= 0 and num1 %7 !=0:
#         nums.append(num1)
#     elif num1 == 2 or num1 == 3 or num1 ==5 or num1 == 7:
#         nums.append(num1)
#     num1 += 1
# print(nums)
# sum_nums = sum(nums)
# print(sum_nums)

#3
# phrase = input('Введите текст: ')
# phrase.lower()
# alths = list(phrase)
# for alth in alths:
#     if alth == ' ' or alth == ',' or alth == '.' or alth == '?' or alth == '!':
#          alths.pop(alths.index(alth))
    
# alths_ver = list(reversed(alths))
# print(alths_ver)
# print(alths)
# if alths_ver == alths:
#     print("Текст является палиндромом")
# else:
#     print("Текст не является палиндромом")

#4
# import random
# player = input("Введите свой выбор: ")
# choices = ["ножницы", "камень", "бумага"]
# computer_choice = random.choice(choices)
# print("Компьютер выбрал: ",computer_choice)
# if player== 'ножницы' and computer_choice == 'бумага' or player== 'бумага' and computer_choice =='камень'or player== 'камень' and computer_choice =='ножницы':
#     print("Ты победил!!!")
# elif player== computer_choice:
#     print("Компьютер выбрал тоже самое!")
# else:
#     print("Ты проиграл(")\

#5
# import csv
# nums = []
# with open('C:\програм\csv.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
#         nums = nums + row
# print(nums)
# f_nums = []
# for num in nums:
#     f_num = float(num)
#     f_nums.append(f_num)
# print(sum(f_nums)/2)

#1
# class Book:
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
# tolstoy = Book("Лев Толстой","Война и мир")
# print(tolstoy.name)
# print(tolstoy.author)
        

#2
# class Soda:
#     def __init__(self, adds=None):
#         if no(adds, str):
#             self.adds = adds
#         else:
#             self.adds = None

#     def show_my_drink(self):
#         if self.adds:
#             print('Газировка и', self.adds)
#         else:
#             print('Обычная газировка')

#3
# class Canorno:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c 
#     def is_triangle(self):
#         if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (int, float)):
#             print("Нужно вводит только числа")
#         elif self.a < 0 or self.b < 0 or self.c < 0:
#             print("С отрицательными числами ничего не выйдет")
#         elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
#             print("Жаль, но из этого треугольника ничего не выйдет")
#         else:
#             print("Ура, можно посторить треугольник")
# first = Canorno(-5 , 8, 9)
# first.is_triangle()

#4
# class Nikolay:
# 	var = ['name', 'age']
 
# 	def __init__(self, name, age):
#             if name == "Николай":
#                 self.name = name
#             else:
#                 self.name = "Я не", name, "а Николай"
#             self.age = age
# per = Nikolay("Максим", "20")
# print(per.name)
# print(per.age)

#5
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, name):
#         self.books.append(name)
#     def remove_book(self, name):
#         try:
#             self.books.remove(name)
#             print("Книга удалена из библиотеки.")
#         except ValueError:
#             print("Книга не найдена в библиотеке.")
#     def search_book(self, name):
#         if name in self.books:
#             print("Книга найдена в библиотеке.")
#             return True
#         else:
#             print("Книга не найдена в библиотеке.")
#             return False
# first_lib = Library()
# first_lib.add_book("Гроза")
# first_lib.add_book('Буратино')
# first_lib.add_book("Война и Мир")
# first_lib.add_book("Судьба человека")
# first_lib.remove_book("Буратино")
# first_lib.search_book("Буратино")
# first_lib.search_book("Гроза")
# print(first_lib.books)

#6
# class AirCompany:
#     def __init__(self):
#         self.planes = []  
#         self.ways = []     

#     def add_plane(self, model):
#         self.planes.append(model)
#         print(f"Самолет {model} добавлен.")

#     def remove_plane(self, model):
#         if model in self.planes:
#             self.planes.remove(model)
#             print(f"Самолет {model} удален.")
#         else:
#             print(f"Самолет {model} не найден.")

#     def add_way(self, way):
#         self.ways.append(way)
#         print(f"Маршрут {way} добавлен.")

#     def remove_way(self, way):
#         if way in self.ways:
#             self.ways.remove(way)
#             print(f"Маршрут {way} удален.")
#         else:
#             print(f"Маршрут {way} не найден.")

#     def find_plane(self, model):
#         if model in self.planes:
#             return f"Самолет {model} найден."
#         else:
#             return f"Самолет {model} не найден."

#     def find_way(self, city):
#         available_routes = [route for route in self.ways if city in route]
#         return available_routes if available_routes else f"Нет доступных маршрутов для города {city}."


# pobeda = AirCompany()
# pobeda.add_plane("Boeing 737")
# pobeda.add_plane("Boeing 777")
# print(pobeda.find_plane("Airbus A320"))
# pobeda.remove_plane("Boeing 737")
# print(pobeda.find_plane("Boeing 737"))
# pobeda.add_way("Екатеринбург - Москва")
# pobeda.add_way("Москва - Los Angeles")
# print(pobeda.find_way("Los Angeles"))

#7
# class BankAccount:
#     def __init__(self, account, owner, balance=0.0):
#         self.account = account
#         self.owner = owner                    
#         self.balance = balance                
#     def moneyplus(self, pay):
#         commission = pay * 0.01            
#         self.balance += pay - commission
#         print(f"Счет пополнен на {pay}. Текущий баланс: {self.balance}")
#     def moneymimus(self, pay):
#         if pay > self.balance:
#             print("Недостаточно средств на счете.")
#             return
#         commission = pay * 0.01   
#         self.balance -= (pay + commission)
#         print(f"Со счета снято {pay}. Комиссия: {commission}. Текущий баланс: {self.balance}")
#     def check_balance(self):
#         print(f"Текущий баланс счета: {self.balance}")
# first_per = BankAccount("0001", "Sava")
# first_per.check_balance()      
# first_per.moneyplus(5000)         
# first_per.moneymimus(1500)        
# first_per.check_balance()

#8
# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y 

#     def distance_btw(self, other_point):
#         dx = self.x - other_point.x
#         dy = self.y - other_point.y
#         return math.sqrt(dx**2 + dy**2)

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#         print(f"Новые координаты: ({self.x}, {self.y})")

#     def where(self):
#         if self.x == 0 and self.y == 0:
#             return "Точка имеет координаты (0, 0)"
#         elif self.x == 0:
#             return "Точка лежит на оси y"
#         elif self.y == 0:
#             return "Точка лежит на оси x"
#         else:
#             return "Точка не лежит ни на одной из осей"
# Sava_point = Point(20, -4)
# Your_point = Point(0, 12)
# print(Sava_point.distance_btw(Your_point))
# Sava_point.move(-3, 3)
# print(Sava_point.where())

#9
# class Product:
#     def __init__(self, name, price, how):
#         self.name = name 
#         self.price = price     
#         self.how = how 

#     def up(self, qountity):
#         if qountity > 0:
#             self.how += qountity
#             print(f"Количество товара: {self.how}")
#         else:
#             print("Количество для увеличения должно быть положительным.")

#     def less(self, qountity):
#         if qountity > 0:
#             if self.how >= qountity:
#                 self.how -= qountity
#                 print(f"Количество товара: {self.how}")
#             else:
#                 print("Недостаточно товара.")
#         else:
#             print("Количество для уменьшения должно быть положительным.")

#     def cost(self):
#         return self.price * self.how

#     def information(self):
#         print(f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.how}, Общая стоимость: {self.cost()} руб.")
# milkeway = Product("Chocolate_Milkeway", 21, 12)
# cola = Product("Cola", 90, 10)
# candy = Product("Красная цена: Конфета", 50, 100)
# milkeway.less(9)
# cola.up(5)
# milkeway.information()
# cola.information()

#10
# class Student:
#     def __init__(self, name, age):
#         self.name = name            
#         self.age = age               
#         self.subjects = {}            

#     def add_subject(self, subject, grade=None):
#         if subject not in self.subjects:
#             self.subjects[subject] = grade
#         else:
#             print(f"Предмет '{subject}' уже есть")
#     def del_subject(self, subject):
#         if subject in self.subjects:
#             del self.subjects[subject]
#         else:
#             print(f"Предмет '{subject}' не найден у студента")
#     def add_grade(self, subject, grade):
#         if subject in self.subjects:
#             self.subjects[subject] = grade
#         else:
#             print(f"Предмет '{subject}' не найден у студента")

#     def middle_grade(self):
#         valid_grades = [grade for grade in self.subjects.values() if grade is not None]
#         if valid_grades:
#             average = sum(valid_grades) / len(valid_grades)
#             return average
#         else:
#             return None

#     def infomartion(self):
#         print(f"Студент: {self.name}, Возраст: {self.age}")
#         print("Предметы и оценки:")
#         for subject, grade in self.subjects.items():
#             print(f" {subject}: {grade if grade is not None else 'нет оценки'}")
#         mid = self.middle_grade()
#         if mid is not None:
#             print(f"Средний балл: {mid}")
#         else:
#             print("Нет оценок")
# Ivan_U =Student("Ульянов Иван", 17)
# Koz_K = Student("Козлов Кирилл", 17)
# Ivan_U.add_subject("Физика")
# Koz_K.add_subject("Русский язык")
# Ivan_U.add_grade("Физика", 4)
# Koz_K.add_grade("Русский язык", 2)
# Ivan_U.infomartion()
# Koz_K.infomartion()

#1
# try:
#     file = open("C:/програм/example.txt", "r")
#     data = file.read()
#     print(data)
    
# except FileNotFoundError:
#     print("Файл не найден")
# except PermissionError:
#     print("Нет прав доступа к файлу")

#2
# import csv

# with open("C:/програм/data.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#3
# import csv
# nums = []
# with open("C:/програм/weather.csv", 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:  
#         value = float(row[3])
#         nums.append(value)
# print(max(nums))

#4
# import csv
# data = []
# data1 = []
# with open("C:/програм/data1.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         data.append(row)
# with open("C:\програм\data.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row1 in reader:
#         data1.append(row1)
# combined_data = data1 + data
# with open("C:\програм\data.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(combined_data)

#5
# import xml.etree.ElementTree as ET   
# try:
#     tree = ET.parse('C:/програм/products.xml')
#     root = tree.getroot()
# except Exception as e:
#     print(f"Ошибка: {e}")
#     products = []
# for product in root.findall('C:/програм/products/product'):
#     products.append({
#             'название': product.find('название').text,
#             'цена': int(product.find('цена').text),
#             'категория': product.find('категория').text,
#             'количество': int(product.find('количество').text)
#         })
#     if not products:
#         print("Нет продуктов")

#     def print_products(product_list):
#         print("\n{:<20} {:<10} {:<15} {}".format(
#             "название", "цена", "категория", "количество"))
#         print("-" * 60)
#         for p in product_list:
#             print("{:<20} {:<10} {:<15} {}".format(
#                 p['название'], p['цена'], p['категория'], p['количество']))
    

#     print("Сортировка по цене(от высокой):")
#     sorted_by_price = sorted(products, key=lambda x: x['цена'], reverse=True)
#     print_products(sorted_by_price)

#     category = input("Выберите категорию для фильтра: ")
#     filtered = [p for p in products if p['категория'].lower() == category.lower()]
    
#     if filtered:
#         print(f"Продукты в категории '{category}':")
#         print_products(filtered)
#     else:
#         print(f"Нет продуктов в '{category}'")
    
#     print("Заказ:")
#     order = {}
#     for p in products:
#         qty = input(f"Сколько '{p['название']}'вы хотите взять (максимально {p['количество']})?: ")
#         try:
#             qty = int(qty)
#             if 0 < qty <= p['количество']:
#                 order[p['название']] = qty
#         except ValueError:
#             pass
    
#     if order:
#         total_cost = sum(p['цена'] * order[p['название']] for p in products if p['название'] in order)
#         print("Заказ:")
#         for name, qty in order.items():
#             print(f"{name}: {qty} pcs.")
#         print(f"Полная цена: {total_cost} рублей.")
#     else:
#         print("Вы ничего не заказали")

#6
# import os
# import csv

# def main():
#     # Собираем все CSV файлы
#     files = [f for f in os.listdir('C:/data') if f.endswith('.csv')]
#     if not files:
#         print("В папке 'data' нет CSV файлов.")
#         return
#     print(f"Найдено {len(files)} файлов в папке")
    
#     users = []
#     for file in files:
#         with open(f'C:/data/{file}', 'r') as f:
#             users.extend(list(csv.DictReader(f)))
    

#     print("\nCтатистика:")
#     ages = [int(u['возраст']) for u in users if 'возраст' in u and u['возраст'].isdigit()]
#     if ages:
#         print(f"Возраст: от {min(ages)} до {max(ages)} лет, средний {sum(ages)//len(ages)}")
#     if 'пол' in users[0]:
#         genders = [u['пол'] for u in users if u['пол']]
#         print(f"Мужчин: {genders.count('муж')}, Женщин: {genders.count('жен')}")
#     if 'местоположение' in users[0]:
#         locations = [u['местоположение'] for u in users if u['местоположение']]
#         print("Топ 3 города:", ', '.join(sorted(set(locations))[:3]))
    
#     filter_by = input("\nФильтровать по возрасту (введите число) или городу (введите название): ")
#     if filter_by:
#         if filter_by.isdigit():
#             filtered = [u for u in users if 'Возраст' in u and u['Возраст'] == filter_by]
#             print(f"\nНайдено {len(filtered)} пользователей с возрастом {filter_by}:")
#         else:
#             filtered = [u for u in users if 'Местоположение' in u and filter_by.lower() in u['Местоположение'].lower()]
#             print(f"\nНайдено {len(filtered)} пользователей из {filter_by}:")
        
#         for user in filtered[:3]:
#             print(user)


#main()
    
#7
# import string

# def main():
#     try:
#         with open("C:/програм/example.txt", 'r') as f:
#             text = f.read()
#     except Exception as e:
#         print(f"Ошибка при чтении файла: {e}")
#         return
#     print("\nCтатистика:")
#     print(f"Файл прочитан. Всего символов: {len(text)}")
#     sents = [s.strip() for s in text.split('.') if s.strip()]
#     sents += [s.strip() for s in text.split('!') if s.strip()]
#     sents += [s.strip() for s in text.split('?') if s.strip()]
#     print(f"Предложений: {len(sents)}")
#     mid_len = sum(len(s) for s in sents) / len(sents)
#     print(f"Средняя длина предложения: {mid_len:.1f} символов")
#     words = []
#     for word in text.split():
#         del_word = word.strip(string.punctuation + '—»«...')
#         if del_word:
#             words.append(del_word.lower())
    
#     print(f"Всего слов: {len(words)}")
#     print(f"Уникальных слов: {len(set(words))}")
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#     sort = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
#     print("\nТоп-5 самых частых слов:")
#     for word, count in sort[:5]:
#         print(f"{word}: {count} раз")
# main()
    
#8
# def choice():
#     words = ["яблоко", "банан", "апельсин", "виноград"]
#     for i in range(len(words)):
#         other = i
#         for u in range(i+1, len(words)):
#             if words[u] < words[other]:
#                 other = u
#         words[i], words[other] = words[other], words[i]
#     print("После сортировки:", words)

# choice()

    
#1
# from itertools import permutations
# word = input("Введите слово: ")
# letters = list(word)  
# for alth in range(1, len(letters) + 1):
#     for tog in permutations(letters, alth):
#         print(''.join(tog))

#2
# with open("C:/програм/example.txt", "r") as file:
#     text = file.read()
#     text = text.lower()
#     words = text.split()
# word_count = {}
# for word in words:
#     word = word.strip(".,!?;:-()\"'")
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#         print(word_count)
#         print(word)
# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
# for i, (word, count) in enumerate(sorted_words[:10], 1):
#     print(f"{i}. '{word}' - {count} раз")

#3
# num = input("Введите число: ")
# step = input("В какой степеннь возвести: ")
# if step == 0:
#     print(1)
# elif step % 2 == 0:  # если степень четная
#     print(num * num, step // 2)
# else:  # если степень нечетная
#     print(num * (num, step - 1) )

#4
# def find(nums):
#     if not nums:
#         return []
    
#     max_len = 1
#     len_now = 1
#     start_index = 0
#     start = 0
    
#     for i in range(1, len(nums)):
#         if nums[i] <= nums[i-1]:
#             len_now += 1
#         else:
#             if len_now > max_len:
#                 max_len = len_now
#                 start = start_index
#             len_now = 1
#             start_index = i
    
#     if len_now > max_len:
#         max_len = len_now
#         start = start_index
    
#     return nums[start:start + max_len]

# ex = [10, 8, 9, 5, 3, 4, 0]
# final = find(ex)
# print( final)

#5
# import csv
# nums = []
# with open("C:/програм/nums.csv", 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:  
#         value = float(row[0])
#         nums.append(value)
# print(sum(nums))

#6
# class Matrix_Solut:
#     def matrix(self, A, B):
#         self.A = A  
#         self.B = B  
#         self.how = len(A)  
    
#     def solve(self):
#         AB = [row[:] for row in self.A]
#         for i in range(self.how):
#             AB[i].append(self.B[i])
        
#         for i in range(self.how):
#             div = AB[i][i]
#             for j in range(i, self.how+1):
#                 AB[i][j] /= div
            
#             for k in range(i+1, self.how):
#                 mult = AB[k][i]
#                 for j in range(i, self.how+1):
#                     AB[k][j] -= mult * AB[i][j]
        
#         X = [0] * self.how
#         for i in range(self.how-1, -1, -1):
#             X[i] = AB[i][self.how]
#             for k in range(i-1, -1, -1):
#                 AB[k][self.how] -= AB[k][i] * X[i]
        
#         return X

# solver = Matrix_Solut()
# A = [[1, -1],
#      [1, 1]]
# B = [1, 3]
# solver.matrix(A, B)
# solution = solver.solve()
# print("Ответы:")
# print(f"x = {solution[0]:.1f}")
# print(f"y = {solution[1]:.1f}")


#7
# import csv

# def read():
#     data = []
#     with open("c:/програм/weather.csv", newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             data.append(row)
#     return data

# def stat(column):
#     numbers = [float(x) for x in column if x.replace('.', '').isdigit()]
#     if not numbers:
#         return "Нет чисел"
        
#     stats = {
#             "Сумма чисел": sum(numbers),
#             "Среднее арифметическое": sum(numbers)/len(numbers),
#             "Минимальное число": min(numbers),
#             "Максимальное число": max(numbers)
#         }
#     return stats

# def main():
#     data = read()  
#     headers = data[0]
#     columns = list(zip(*data[1:]))
    
#     print("Характеристика:")
#     for i, column in enumerate(columns):
#         print(f"Колонка '{headers[i]}':")
#         stats = stat(column)
        
#         if isinstance(stats, dict):
#             for key, value in stats.items():
#                 print(f"{key}: {value:.2f}")
#         else:
#             print(stats)

#main()

#8
# import random

# SIZE = 10

# def grids():
#     return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

# def print_grid(grid):
#     print("   " + " ".join(str(i) for i in range(SIZE)))
#     for i, row in enumerate(grid):
#         print(f"{i} |" + "|".join(cell if cell != ' ' else ' ' for cell in row) + "|")

# def horizontal(grid, word, row, col):
#     if col + len(word) > SIZE:
#         return False
#     for i in range(len(word)):
#         if grid[row][col + i] != ' ' and grid[row][col + i] != word[i]:
#             return False
#     for i in range(len(word)):
#         grid[row][col + i] = word[i]
#     return True

# def vertical(grid, word, row, col):
#     if row + len(word) > SIZE:
#         return False
#     for i in range(len(word)):
#         if grid[row + i][col] != ' ' and grid[row + i][col] != word[i]:
#             return False
#     for i in range(len(word)):
#         grid[row + i][col] = word[i]
#     return True


# def generate_crossword(words):
#     grid = grids()
#     used_words = []
#     words.sort(key=len, reverse=True)
#     for word in words:
#         word = word.upper()
#         placed = False
#         attempts = 0
#         while not placed and attempts < 100:
#             direction = random.choice(['horizontal', 'vertical'])
#             row = random.randint(0, SIZE - 1)
#             col = random.randint(0, SIZE - 1)
#             if direction == 'horizontal':
#                 placed = horizontal(grid, word, row, col)
#             else:
#                 placed = vertical(grid, word, row, col)
#             attempts += 1
#         if placed:
#             used_words.append(word)
#     return grid, used_words

# def check(grid, solution):
#     for i in range(SIZE):
#         for j in range(SIZE):
#             if grid[i][j] != ' ' and grid[i][j] != solution[i][j]:
#                 return False
#     return True


#words = ['Программа', 'Сервер', 'Браузер', 'Память', 'Клавиша', 'Монитор', 'Скрипт', 'Студент', 'Учебник', 'Формула']
#grid, used_words = generate_crossword(words)
#print("Kроссворд:")
#print_grid(grid)
#print("Использованные слова:", ", ".join(used_words))
#solution = [row.copy() for row in grid]
#if check(grid, solution):
#   print("Решение правильное!")
#else:
#   print("Решение неправильное.")

#9
# class Matrix:
#     def __init__(self, data):
#         self.data = data
#         self.rows = len(data)  
#         self.cols = len(data[0]) if data else 0 

#     def __str__(self):
#         s = ""
#         for row in self.data:
#             s += str(row) + "\n"
#         return s
    
#     def plus(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             return "Матрицы разного размера!"
#         result = []
#         for i in range(self.rows):
#             row = []
#             for j in range(self.cols):
#                 row.append(self.data[i][j] + other.data[i][j])
#             result.append(row)
#         return Matrix(result)  

#     def minus(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             return "Ошибка: Матрицы разного размера!"
#         result = []
#         for i in range(self.rows):
#             row = []
#             for j in range(self.cols):
#                 row.append(self.data[i][j] - other.data[i][j])
#             result.append(row)
#         return Matrix(result)  
    
#     def mul(self, other):
#         if self.cols != other.rows:
#             return "Нельзя умножить эти матрицы!"
#         result = []
#         for i in range(self.rows):
#             row = []
#             for j in range(other.cols):
#                 summa = 0
#                 for k in range(self.cols):
#                     summa += self.data[i][k] * other.data[k][j]
#                 row.append(summa)
#             result.append(row)
#         return Matrix(result)

#     def transport(self):
#         result = []
#         for j in range(self.cols):
#             row = []
#             for i in range(self.rows):
#                 row.append(self.data[i][j])
#             result.append(row)
#         return Matrix(result)

#     def get2know(self):
#         if self.rows != 2 or self.cols != 2:
#             return "Определитель только для матриц 2x2"
#         return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

#matrix1 = Matrix([[3, 2], [4, 4]])
#matrix2 = Matrix([[7, 6], [7, 10]])
#print("Матрица 1:\n", matrix1)
#print("Матрица 2:\n", matrix2)
#print("Сумма:\n", matrix1.plus(matrix2))
#print("Разность:\n", matrix1.minus(matrix2))
#print("Произведение:\n", matrix1.mul(matrix2))
#print("Транспонированная матрица 1:\n", matrix1.transport())
#print("Определитель матрицы 1:\n", matrix1.get2know())
