# Задача 1
def perimetr(a, b):
    perimetr = (a + b) * 2
    print("Периметр прямоугольника: ", perimetr)

# Задача 2    
def square(a, b):
    square = a * b
    print("Площадь прямоугольника: ", square)

# Задача 3    
def revs():
    lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
    lst.reverse()
    print(lst) 

# Задача 4
def menu():    
    menu = {
        "beefstrogonoff": 350,
        "burger": 200,
        "meatloaf": 500,
        "chicken pot pie": 400,
        "beefshteks": 650
    }
    new_menu = {k:v + 50 for k, v in menu.items()}  
    print(new_menu) 

# Задача 5    
def time():
    time = input("Введите время: ")
    hour = int(time[0:2])
    minute = int(time[3:5])
    second = int(time[6:8])
    res = (hour * 3600) + (minute * 60) + second
    print(res, "секунда")

# Задача 6        
def chat_bot():
    while True:
        a = input()
        if a == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        elif a.upper() == a:
            print("Успокойся!") 
        elif "?" in a:
            print("Конечно!")  
        else:
            print("Ну и что")  
            
# Задача 7
def upp(word):
    word_split = word.split()
    new_lst = []
    for i in word_split:
        new_lst.append(i.title()[0])
    res = "".join(new_lst)
    print(res)    
    
        
    