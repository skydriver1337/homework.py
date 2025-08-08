import math
def square(side):
area = side ** 2
return math.ceil(area) if not isinstance(side,int) else area
print(square(5))
print(square(5.3))
print(square(4.1))
