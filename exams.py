#1
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in a:
#    if i < 5:
#        print(i)

#2
#import random
#a = [random.randint(0, 15) for i in range(10)]
#print(a)
#print(f"Первое: {a[0]} Последнее: {a[-1]}")
#s=1
#for i in a:
#    s*=i
#print(f"Произведение: {s}")

#3
#a = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
#for i in a:
#    if i == 237:
#        break
#    elif i%2 == 0:
#        print(i)

#4
#a = int(input('age: '))
#if a < 2:
#    print('mladenechik')
#elif a>=2 and a<4:
#    print('malish')
#elif a>=4 and a<13:
#    print('rebenok')
#elif a>=13 and a<20:
#    print('podrostok')
#elif a>=20 and a<65:
#    print('vzrosliy')
#else:
#    print('pozhiloy')

#5
#unverificated = ['user1', 'user2', 'user3', 'user4', 'user5']
#verificated=[]
#i=0
#print(f"Unverificated: {unverificated}")
#print(f"Verificated: {verificated}\n\n")
#while unverificated:
#    transfer=unverificated.pop()
#    verificated.append(transfer)
#    i+=1
#print(f"Unverificated: {unverificated}")
#print(f"Verificated: {verificated}")

#6
#a=['pizza', 'falafel', 'carrot cake']
#cream = str(input('What your favorite ice-cream? '))
#b=a.copy()
#b.append(cream)
#print(f"I like {a}")
#print(f"What is my friend likes: {b}")

#7
#listik = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#a = []
#l=0
#s=0
#for i in listik:
#    if i<30 and i>2 and i%3==0:
#        a.append(i)
#        del(lst[l])
#        l+=1
#    else:
#        s+=i
#        l+=1
#print(f"Gotovo: {a}\nSuma = {s}")

#8
#list={'a': 2, 'b': 4, 'c': 6, 'd': 8}
#for i in list.values():
#    if i>2:
#        print(i)

#9
#import random
#x=int(input('Stepen: '))
#a=[random.randint(1, 10) for i in range(6)]
#b=[random.randint(1, 10)**x for i in range(6)]
#for i in a:
#    for j in b:
#        print(f"i know your key – {i}, his value is - {j}")
#        break
