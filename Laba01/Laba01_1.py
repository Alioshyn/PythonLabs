# 2. Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

print("Введите первое число")
a=input()
print("Введите второе число")
b=input()
print("Введите третье число")
c=input()

if a==b:
    print("Первое число равно второму")
if a==c:
    print("Первое число равно третьему")
if c==b:
    print("Второе число равно третьему")
if (a!=b and b!=c and c!=a):
    print("Все три числа разные")

print()