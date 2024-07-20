import random

def is_valid_user_right_border(right_border):
    if right_border.isdigit() and int(right_border) > 0:
        return True
    else:
        return False
    
def is_valid_user_number(user_input, right_border):
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) <= right_border:
        return True
    else:
        return False


def guessing_the_number():

    
    count = 0

    print("Добро пожаловать в числовую угадайку")

    while True:
        print("Введите максимум диапазона загаданного числа. Любое неотрицательное число. ")
    
        right_border = input()
        if not is_valid_user_right_border(right_border):
            print("А может быть все-таки введем целое число?")
            continue
        right_border = int(right_border)
        guessed_number = random.randint(1, right_border)
        break
    
    while True:
        print(f"Введите целое число от 1 до {right_border}")
        user_input = input()
        
        if not is_valid_user_number(user_input, right_border):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
            
        user_input = int(user_input)
        
        if user_input > guessed_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count += 1
        elif user_input < guessed_number:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count += 1
        else:
            print(f"Вы угадали число за {count} попыток, поздравляем!")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            print(f"Хотите сыграть еще раз? (д - да, н - нет)")
            user_answer = input()
            if user_answer.lower() == "д":
                guessing_the_number()
            else:
                break
            
guessing_the_number()