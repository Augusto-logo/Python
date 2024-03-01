print('~' * 25)
print('      Cash Machine')
print('~' * 25)

one = ten = twenty = fifty = 0

withdraw = int(input('Enter the amount to withdraw: '))
rest = withdraw
#valor 1524
while rest > 0:
    if rest > 50:
        fifty = rest // 50
        rest = rest % 50
    elif rest > 20:
        twenty = rest // 20
        rest = rest % 20
    elif rest > 10:
        ten = rest // 10
        rest = rest % 10
    elif rest > 1:
        one = rest// 1
        rest = rest % 1
print('=' * 35)
if fifty > 0:
    print(f'You received {fifty} $50 dollar bills!\n')
if twenty > 0:
    print(f'You received {twenty} $20 dollar bills!\n')
if ten > 0:
    print(f'You received {ten} $10 dollar bills!\n')
if one > 0:
    print(f'You received {one} $1 dollar bills!\n')
print('=' * 35)