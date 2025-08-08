def filter_list(lst):
  return [x for x in lst if x < 30 and x % 3 == 0]
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
filtered = filter_list(lst)
print("Исходный список:", lst)
print("Отфильтрованный список (числа <30, кратные 3):", filtered)
