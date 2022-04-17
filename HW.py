s =  input('Введите несколько чисел через пробел:')

List_ = s.split() # преобразуем введенные числа в список
# print(List_)

# отсортируем список List_ по возрастанию методом пузырька

for i in range(len(List_)):
    for j in range(len(List_) - i - 1):
        if List_[j] > List_[j + 1]:
            List_[j], List_[j + 1] = List_[j + 1], List_[j]

print(List_)

# определим индекс введенного числа в списке List_
g = input('Теперь введите еще одно число:')
low = 0 # нижняя граница списка
high = len(List_) - 1 # верхняя граница
mid = (low + high) // 2 # середина

while g != List_[mid] and low <= high:
    if g > List_[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if g == List_[mid]:
    print('ID:', mid)
else:
    print('Такого значения нет')


