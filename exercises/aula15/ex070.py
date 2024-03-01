print('~'*30)
print('    shopping in store!    ')
print('~'*30)

totalAmount = 0
expensiveProduct = 0
cheaperProduct = 5000
cheaperProductName = ''
choice = 'a'

while True:
    print('='*20)
    product = input('enter the product: ').strip()
    price = float(input('enter the price: '))
    totalAmount += price
    print('='*20)
    if price > 1000:
        expensiveProduct += 1
    if price < cheaperProduct:
        cheaperProduct = price
        cheaperProductName = product
    while choice not in 'yn':
        choice = input('Do you want to order more? (y/n): ').strip().lower()
    if choice == 'n':
        break
    choice = 'a'
print('='*20)
print(f'The total amount: R${totalAmount}!')
print(f'There were {expensiveProduct} above R$1000!')
print(f'The cheaper product was {cheaperProductName} and it costs R${cheaperProduct}!')
