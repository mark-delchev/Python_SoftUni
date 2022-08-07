Sofia = ['Sofia', 0.05, 0.07, 0.08, 0.12]
Varna = ['Varna', 0.045, 0.075, 0.10, 0.13]
Plovdiv = ['Plovdiv', 0.055, 0.08, 0.12, 0.145]

city = str(input())
sales = float(input())

if city in Sofia:
    if 0 <= sales <= 500:
        commission = sales * Sofia[1]
        print(f'{commission:.2f}')
    elif 500 < sales <= 1000:
        commission = sales * Sofia[2]
        print(f'{commission:.2f}')
    elif 1000 < sales <= 10000:
        commission = sales * Sofia[3]
        print(f'{commission:.2f}')
    elif sales > 10000:
        commission = sales * Sofia[4]
        print(f'{commission:.2f}')
    else:
        print('error')

elif city in Varna:
    if 0 <= sales <= 500:
        commission = sales * Varna[1]
        print(f'{commission:.2f}')
    elif 500 < sales <= 1000:
        commission = sales * Varna[2]
        print(f'{commission:.2f}')
    elif 1000 < sales <= 10000:
        commission = sales * Varna[3]
        print(f'{commission:.2f}')
    elif sales > 10000:
        commission = sales * Varna[4]
        print(f'{commission:.2f}')
    else:
        print('error')

elif city in Plovdiv:
    if 0 <= sales <= 500:
        commission = sales * Plovdiv[1]
        print(f'{commission:.2f}')
    elif 500 < sales <= 1000:
        commission = sales * Plovdiv[2]
        print(f'{commission:.2f}')
    elif 1000 < sales <= 10000:
        commission = sales * Plovdiv[3]
        print(f'{commission:.2f}')
    elif sales > 10000:
        commission = sales * Plovdiv[4]
        print(f'{commission:.2f}')
    else:
        print('error')

else:
    print('error')