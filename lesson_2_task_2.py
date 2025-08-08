def is_year_leap(year):
  return year % 4 == 0
  year_to_check = [2024, 2023, 2000, 1900, 2020]
  for year in years_to_check:
    result = is_year_leap(year)

print(f"год {year}: {result}")
