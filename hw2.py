'''Определите количество четных элементов в последовательности, завершающейся числом 0.'''
i=0
while True:
    i=int(input())
    if i==0:
        break
    if i%2==0:
        i+=1
print(i)
