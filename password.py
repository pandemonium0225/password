password = 'a123456'
limit = 3
while limit <= 3:
    limit -= 1
    password2 = input("please guess the password, you can try 3 times")
    if password2 == password:
        print("welldone 登入成功")
        break
    elif password2 == 'Q':
        print("you are leaving this password-guessing game")
        break
    elif password2 != password:
        if limit == 0:
            break
        else:
            print("密碼錯誤 還有" + str(limit) + "次機會!")