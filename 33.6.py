A=int(input())
B=int(input())
H=int(input())
while A>B:
    A=int(input())
    B=int(input())
    H=int(input())
if H<A:
    print('Недосып')
elif H>B:
    print('Пересып')
else:
    print('Это нормально')
#6.10.8,4.8.5,2.5.3-это нормально
#7.9.10,10.12.14-пересыр
#7.9.2.,10.12.4-недосып
