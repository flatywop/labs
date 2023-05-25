x = input('введите слово: ')
with open('synonyms.txt') as f:
    lines = [i.rstrip('\n') for i in f]
    n = [i.split(' - ') for i in lines]
    n = sum(n, [])
    myn = {n[i]: n[i + 1] for i in range(0, len(n)-1, 2)}
    if x in n:
        print(myn[x])
        q = input( 'вас устраивает подбор синонима?(да / нет): ')
        if q == 'нет':
            s = input('введите новое слово: ')
            f = open('synonyms.txt', 'a+')
            f.write(s)
        else:
            print('ok')
    else:
        print('такого слова нет')


