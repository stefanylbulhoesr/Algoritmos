num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(3, 4)
print(num)
num.remove(7) #procura do início da lista o primeiro elemento para remover
print(num)
print(f'Essa lista tem {len(num)} elementos')