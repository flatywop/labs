from random import randint

def z1():
    m = []
    while (n:=str(input()))!= "stop":
        m.append(n)
    print(" ".join(m))

def z2():
    m = []
    while (n:=str(input()))!= "stop":
        if "ф" in n or "Ф" in n:
            print("ого! это редкое слово")
        else:
            print("это не очень редкое слово")

def z3():
    print ("для завершения игры введите слово stop")
    f = 0
    s = 0
    while f<3:
        while True:
            a = randint(1,100)
            b = randint(1,100)
            print (f"{a} + {b} = ", end = " ")
            res = input()
            while not res.isdigit() and res != "stop":
                print ("вы ввели что-то не то, повторите ввод:", end=" ")
                res = input()
            if res == "stop":
                break
            if a + b == res:
                print("ответ правильный")
                s +=1
            else:
                print("ответ неправильный")
                f +=1
            if f == 3:
                print("игра окончена, правильных ответов: ", s)

z1()
z2()
z3()
