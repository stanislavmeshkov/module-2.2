first = int(input())
second = int(input())
third = int(input())
if first == second or first == third or second == third:
    print(2)
elif first == second == third:
    print(3)
elif first != second != third:
    print(0)