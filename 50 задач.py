#screen 1

#1
# list = [60, 'haha',93 ]
# list.reverse()
# print(list)

#2
# list = [60, 'haha', 93]
# list[0], list[len(list)-1] = list[len(list)-1], list[0]
# print(list)

#3
# par = 50, 'haha', 9
# def to_list(par):
#     return list(par)
# print(to_list(par))

#4
# nums = [50, 90, 12, -8, 6.5, 10]
# def useless(nums):
#     maxnum = max(nums)
#     fin = maxnum / len(nums)
#     return fin
# print(useless(nums))

#5
# abs_list = []
# list = [0, -50, 10, 7, -160]
# def list_sort(list):
#     for change in list:
#         if change < 0:
#             change *= -1
#             abs_list.append(change)
#         else:
#             abs_list.append(change)
#     fin_list = sorted(abs_list, reverse=True) #если False, то по возрастанию
#     return fin_list
# print(list_sort(list))

#6
# words = ['joker', 'cash', 'details']
# new_words = []
# def all_eq(words):
#     biggest_len = len(max(words, key=len)) # находим самое длинное слово из списка
#     for change in words:
#         if len(change) < biggest_len:
#             while len(change) != biggest_len:
#                 change = change + '_'
#                 if len(change) == biggest_len:
#                     new_words.append(change)
#         else:
#             new_words.append(change)
#     return new_words
# print(all_eq(words))
#screen 2

#1
# num = input('Введите число: ')
# def to_float(num):
#     if num.isdigit():
#         num = float(num)
#     else:
#         num = 'Невозможно преобразовать'
#     return num
# print(to_float(num))

#2
a = 13
b = 14.768568
c = 8.76
d = 56
def avg_5(a, b, c, d):
    num = a * b * c * d
    return round(num, 5)
print(avg_5(a, b, c, d))

#3
# num1 = 6.6
# num2 = 2
# mor = num1 * num2
# def mul_to_int(mor):
#     if (mor * 10) % 10 ==0:
#         mor = int(mor)
#     else:
#         mor = mor
#     return mor
# print(mul_to_int(mor))

#4
# import math
# how = 60
# r_r = (how / (4/3 * math.pi)) ** (1/3)
# print(r_r, "- радиус шара")

#screen 3

#1
# choose = 6.0
# def dislike_6(choose):
#     if choose == 6:
#         answ = 'Только не 6!'
#     else:
#         answ = 'True'
#     return answ
# print(dislike_6(choose))

#2
# letter = input('Введите с чем нужна помощь: ')
# def help_boll(letter):
#     if letter == 'а':
#         answ = ' (а + b) + c = a + (b + c) или (a*b)*c = a*(b*c)'
#     elif letter == 'к':
#         answ = 'a+b=b+a или a*b=b*a'
#     elif letter == 'д':
#         answ = 'a*(b + c) = a*b + a*c'
#     elif letter == 'м':
#         answ = 'не(a*b) = не(a) + не(b) или не(a+b) = не(a) * не(b)'
#     else:
#         answ = '"a" - ассоциативность, "к" - коммутативность, "д" - дистрибутивность, "м" - правило де Моргана'
#     return answ
# print(help_boll(letter)) 

#screen 4

#1
# list = [60, 'haha',93 ]
# list.reverse()
# print(list)

#2
# list = [60, 'haha', 93]
# list[0], list[len(list)-1] = list[len(list)-1], list[0]
# print(list)

#3
# par = 50, 'haha', 9
# def to_list(par):
#     return list(par)
# print(to_list(par))

#4
# nums = [50, 90, 12, -8, 6.5, 10]
# def useless(nums):
#     maxnum = max(nums)
#     fin = maxnum / len(nums)
#     return fin
# print(useless(nums))

#screen 5

#5
# abs_list = []
# list = [0, -50, 10, 7, -160]
# def list_sort(list):
#     for change in list:
#         if change < 0:
#             change *= -1
#             abs_list.append(change)
#         else:
#             abs_list.append(change)
#     fin_list = sorted(abs_list, reverse=True) #если False, то по возрастанию
#     return fin_list
# print(list_sort(list))

#6
# words = ['joker', 'cash', 'details']
# new_words = []
# def all_eq(words):
#     biggest_len = len(max(words, key=len)) # находим самое длинное слово из списка
#     for change in words:
#         if len(change) < biggest_len:
#             while len(change) != biggest_len:
#                 change = change + '_'
#                 if len(change) == biggest_len:
#                     new_words.append(change)
#         else:
#             new_words.append(change)
#     return new_words
# print(all_eq(words))

#screen 6

#1
# list = ['ahhahaah', 60, 12]
# def to_dict(list):
#     slov = {items: items for items in list}
#     return slov
# print(to_dict(list))

#2
# my_dict = {"first_one": "we can do it"}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
# biggest_dict(pet = 'dog',lesson = 'English' )
# print(my_dict)

#3
# nums = [0, 9, 5, 8, 1, 0, 8, 4, 7, 3, 8, 0, 9, 9, 2]
# def count_it(nums):
#     dicts = {num: nums.count(num) for num in nums}
#     chan_dict = sorted(dicts.items(), key = lambda x: x[1])
#     return dict(chan_dict[-3:]) #возвращение последних трех элементов
# print(count_it(nums))

#4
# from collections import OrderedDict
# my_dict = OrderedDict({'pet': 'dog',
#            'toy': 'car',
#            'name':'Sava',
#            'lesson': 'English',
#            'apartment' : 'window'})
# my_dict.move_to_end('pet', last=True)
# my_dict.move_to_end('apartment', last = False)
# my_dict['new_key'] = 'new_value'
# del my_dict['toy']
# print(my_dict)

#строки_1

#1
# low_subst = []
# low_st = []
# subst = ['hhaha', 'car', 'warm', 'PlaySTAtion']
# st = ['joke', 'frog', 'playstation']
# def search_substr(subst, st):
#     for low_substs in subst:
#         low_subst.append(str.lower(low_substs))
#     for low_sts in st:
#         low_st.append(str.lower(low_sts))
#     for same in low_subst:
#         if same in low_st:
#             answ = ('Есть контакт')
#         else:
#             answ = ('Мимо')
#     return answ
# print(search_substr(subst, st))

#2
# letter = 'p'
# st = 'piper'
# def first_last(letter, st):
#     if st.find(letter) < 0:
#         answ = 'None, None'
#     else:
#         answ = st.find(letter) , st.rfind(letter)
#     return answ
# print(first_last(letter, st))

#3
# text = 'Александр Пушкин начал писать свои первые произведения уже в семь лет. В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. Пушкин первым из русских писателей начал зарабатывать литературным трудом. Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения в поддержку революционеров — за вольнодумство поэта даже отправляли в ссылки.'
# from collections import Counter
# def top3(text):
#     counter_top3 = Counter(text.replace(' ', '')).most_common(3)
#     return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])
# print(top3(text))

#4
# st = 'Привет, как твои дела?'
# fin_text = ''
# upper = True
# for alth in st:
#     if  alth.isalpha():
#         if upper == True:
#             upper = not upper
#             fin_text = fin_text + alth.lower()
#             print('low')
#         else:
#             fin_text= fin_text + alth.upper()
#             upper = not upper
#             print('up')
#     else:
#         fin_text += alth
# print(fin_text)

#строки 2

#5
# st = "С реки повеяло ночной прохладой (солнце ещё не взошло) и какой-то промозглой сыростью и запахом."
# scob1 = ")"
# scob2 = "("
# while scob1 in st or scob2 in st:
#     place2 = st.find(')')
#     place1 = st.find('(')
#     st = st.replace(st[place1:place2+1], '')
# print(st)

#6
# word = 'гр@оо@лк@оц@ва'
# fin_text = []
# def cleaned_str(word):
#     for alth in word:
#         if alth == '@':
#             fin_text.pop()
#         else:
#             fin_text.append(alth)
#     return ''.join(fin_text)
# print(cleaned_str(word))

#задача 2
#10
# x = [10]
# y = [0]
# def coor(x, y):
#     return (x[0],y[0])
# print(coor(x,y))

#11
# goests = ['Андрей', "Максим", "Иван"]
# def hello(goests):
#     for hi in goests:
#         answ = hi + ', здравствуйте'
#         print(answ)
# hello(goests)

#12
# word = 'хоккей'
# def check(word):
#     words = list(word)
#     for check in range(0, len(list(word))):
#         if words[check-1] == words[check]:
#             print('True')
# check(word)

#13
# sen = 'Привет,  как твои  дела?'
# def right_sen(sen):
#     new_sen = sen.replace('  ', ' ')
#     return new_sen
# print(right_sen(sen))

#14
# import math
# rad = 14
# long = 10
# q = 1000
# def mass(rad, long, q):
#     V = math.pi * rad**2 * long
#     return round(V, 2)
# print(mass(rad, long, q))

#15
# import math
# nums = '10, 1, -5'
# def more(nums):
#     int_num = []
#     list_num = nums.split(", ")
#     for how in range(0, len(list_num)):
#         new_num = int(list_num[how])
#         int_num.append(new_num)
#     answ = math.prod(int_num)
#     print(answ)
# more(nums)

#16
# import math
# box1 = [6, 8, 1]
# box2 = [3, 15, 24]
# box3 = [7, 20, 3]
# boxes  = [box1, box2, box3]
# sum_boxes = []
# def gen(boxes):
#     for box in boxes:
#         sum_boxes.append(math.prod(box))
#     answ = sum(sum_boxes)
#     return answ
# print(gen(boxes))

#17
# import math 
# pointsa = {"x" : -2,
#           "y" : 1}
# pointsb = {'x': 4,
#            'y': 3}
# def long(pointsa, pointsb):
#     x = pointsb.get('x') - pointsa.get('x')
#     y = pointsb.get('y') - pointsa.get('y')
#     long = math.sqrt(x**2 + y**2)
#     return round(long, 3)
# print(long(pointsa, pointsb))

#18
# sent = 'спасибо, но нет'
# def x4k3p4(sent):
#     sent = sent.lower()
#     sent = sent.replace('а', '4')
#     sent =sent.replace('е', '3')
#     sent =sent.replace('и', '1')
#     sent =sent.replace('о', '0')
#     sent =sent.replace('с', '5')
#     return sent
# print(x4k3p4(sent))

#19
# nums = [5, 9, 0]
# def sum(nums):
#     new_num = 0
#     while new_num < 100:
#         for how in range(0, len(nums)-1):
#             new_num = new_num + nums[how]
#         nums.append(new_num)
#     return nums
# print(sum(nums))

#20
# nums = [0, -1, -10]
# def choose(nums):
#     for how in range(0, len(nums)):
#         if nums[how-1] < nums[how]:
#             answ = 'Возрастает'
#         else:
#             answ = 'Убывает'
#     return answ
# print(choose(nums))

#21
# nums = [0, 5, 10, 15, 23, 25]
# def mid(nums):
#     if len(nums) % 2 != 0:
#         return nums[int((len(nums)/2))]
#     else:
#         middels = (nums[int(len(nums) / 2) -1] + nums[int(len(nums) / 2)]) / 2
#         return middels
# print(mid(nums))

#7
# text = []
# def one():
#     message = ' '
#     while message != '   ':
#         message = input('Нажмите на кнопкку(space). Чтобы вывести сообщение нажмите на кнопку 3 раза: ')
#         if message == ' ':
#             message = message.replace(' ', 'A')
#             text.append(message)
#         elif message == '     ':
#             message = message.replace('     ', 'E')
#             text.append(message)
#         elif message == '       ':
#             message = message.replace('       ', 'G')
#             text.append(message)
#     if message == '   ':
#         return ''.join(text)
# print(one())

#8
# text = ['a', 'C', 'V', 'e', 'r']
# new_text = []
# def rev(text):
#     for alth in text:
#         if alth.islower():
#             alth = alth.upper()
#             new_text.append(alth)
#         else:
#             alth = alth.lower()
#             new_text.append(alth)
#     new_text.reverse()
#     return new_text
# print(rev(text))

#9
# friends = ['Mark', 'Mary', 'Nick', 'John']
# enemies = ['Peter', 'Bob', 'John']
# def hate(friends, enemies):
#     for names in friends:
#         for stu in enemies:
#             if names == stu:
#                 friends.remove(names)
#     return friends
# print(hate(friends, enemies))

# задачи 3

#1
# def game():
#    choose1 = input("Выбор первого игрока: ")
#    choose2 = input('Выбор второго игрока:')
#    if choose1 == 'камень' and choose2 == 'ножницы':
#         answ = 'первый победил'
#    elif choose1 == 'камень' and choose2 == 'бумага':
#         answ = 'второй победил'
#    elif choose1 == 'бумага' and choose2 == 'камень':
#         answ = 'первый победил'
#    elif choose1 == 'ножницы' and choose2 == 'камень':
#         answ = 'второй победил'
#    elif choose1 == 'бумага' and choose2 == 'ножницы':
#          answ = 'второй победил'
#    elif choose1 == 'ножницы' and choose2 == 'бумага':
#         answ = 'первый победил'
#    return answ
# print(game())

#2
# text = 'Как дела? Пошли гулять??????'
# placeask1 = text.find('!')
# placeask2 = text.rfind('!')
# placequen1 = text.find('?')
# placequen2 = text.rfind('?')
# def no_noisy(placeask1, placeask2, placequen1, placequen2):
#     if text[placeask1] == text[placeask1+1]:
#         new_text = text.replace(text[placeask1:placeask2],'' )
#     elif text[placeask1] != text[placeask1+1]:
#         placeaskend = text.find('!', text.find('!')+1)# так будет искаться второе вхождение символа !
#         new_text = text.replace(text[placeaskend:placeask2],'' )
#     if text[placequen1] == text[placequen1+1]:
#         new_text = text.replace(text[placequen1:placequen2],'' )
#     elif text[placequen1] != text[placequen1+1]:
#         placequenend = text.find('?', text.find('?')+1)# так будет искаться второе вхождение символа ?
#         new_text= text.replace(text[placequenend:placequen2],'' )
#     return new_text
# print(no_noisy(placeask1, placeask2, placequen1, placequen2))

#3
# V = 10
# D = 10
# K = 10
# T = 1
# cards = [10, V, 2]
# def check(cards):
#     if sum(cards) < 21:
#         return False
#     else: 
#         return True
# print(check(cards))

#5
# text =' y+o+u+'
# def check(text):
#     for alth in text:   
#         if alth.isalpha():
#             if text[text.index(alth) -1] == '+' and text[text.index(alth) +1] == '+':
#                 return True
#             else: return False
# print(check(text))

#6
# text = '12:00 pm'
# def change(text):
#     if 'am'in text or 'pm' in text:
#         if 'am' in text:
#             list_text = text.split(':')
#             list_text[0] = int(list_text[0]) 
#             list_text[0] = str(list_text[0])
#             if list_text[0] == '12':
#                 list_text[0] = '00'
#             else:
#                 list_text[0] = list_text[0]
#             text24 = ':'.join(list_text)
#             new_text24 = text24.replace('am', '')
#             return new_text24
#         else:
#             list_text = text.split(':')
#             if list_text[0] == '12':
#                 text24 = ':'.join(list_text)
#                 new_text24 = text24.replace('pm', '')
#                 return new_text24
#             else:
#                 list_text[0] = int(list_text[0]) + 12
#                 list_text[0] = str(list_text[0])
#                 text24 = ':'.join(list_text)
#                 new_text24 = text24.replace('pm', '')
#                 return new_text24
#     elif not 'am'in text or not 'pm' in text:
#         list_text = text.split(':')
#         if list_text[0] >= '12':
#             list_text[0] = int(list_text[0]) - 12
#             list_text[0] = str(list_text[0])
#             text12 = ':'.join(list_text) + ' pm'
#             return text12
#         else:
#             if list_text[0] == '00':
#                 text12 = ':'.join(list_text) + ' am'
#             else:
#                 text12 = ':'.join(list_text) + ' am'
#             return text12
# print(change(text))


#7
# password = 'HUFubgnripjhi9038903275%'
# def check(password):
#     grade = 0
#     if "!" in password or "@" in password or "%" in password:
#             grade += 1
#     if password.islower() == False:
#         grade += 1
#     if password.isupper() == False:
#         grade += 1
#     if len(password) >= 8:
#         grade += 1
#     if any(num.isdigit() for num in password) == True: #проверка на число
#         grade += 1
#     print('Оценка сложности вашего пароля - ', grade,'/ 5') 
# check(password)
        
#8
# nums = input('Введите число: ')
# def nums_in_rus(nums):
#     if nums == '0':
#         answ = 'ноль'
#     units = ['',"один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
#     teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
#              "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
#     tens = ['', "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
#             "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
#     hundreds = ["", "сто", "двести", "триста", "четыреста", 
#                 "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
#     if len(nums) == 3:
#         if  int(nums) % 100 == int(nums) % 10:
#             answ = hundreds[int(int(nums) / 100)] + units[int(nums)%10]
#         else:
#             answ = hundreds[int(int(nums) / 100)] + tens[int((int(nums) %100) / 10)]+ units[int(nums)%10]
#     elif len(nums) == 2:
#         if int(int(nums) / 10) != 1:
#             answ = tens[int(int(nums) /10)]+ teens[int(nums)%10]
#         else:
#             answ = teens[int(nums)%10]
#     elif len(nums) == 1:
#         answ = units[int(nums) % 10]
#     return answ
# print(nums_in_rus(nums))

#9
# long = (input('Какую длину чисел выбираете: '))
# def lucky_ticket(long):
#     grade = 0
#     for num in range(0, int(long)):
#         nums = []
#         if len(str(num)) % 2:
#             mid = int(len(str(num)) / 2)
#             for alth in str(num):
#                 alth = int(alth)
#                 nums.append(alth)
#                 if len(nums) > 2:
#                     if sum(nums[0:mid+1]) == sum(nums[mid+2:len(str(num))+1]):
#                         grade += 1
#                         print('3 значное')
#                 elif len(nums)==2:
#                     if nums[0] == nums[1]:
#                         grade+= 1
#                 elif len(nums) == 1:
#                     continue
#     return grade 
# print(lucky_ticket(long))
