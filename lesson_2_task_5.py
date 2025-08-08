def month_to_season(month):
  if month in [12, 1, 2]:
    return "Зима"
  elif month in [3, 4, 5]:
    return "Весна"
  elif month in [6, 7, 8]:
    return "Лето"
  elif month in [9, 10, 11]:
    return "Осень"
  else:
    raise ValueError("Некорректный номер месяца. Введите число от 1 до 12.")
 if __name__ == "__main__":
   test_cases = [1, 3, 6, 9, 12, 15]

   for month in test_cases:
       try:
           print(f"Месяц {month}: {month_to_season(month)}")
except ValueError as e:
   print(f"Месяц {month}: {e}")
