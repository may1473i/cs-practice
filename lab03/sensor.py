P_deg = float(input('Введите порог в градусах Цельсия '))
n = int(input('Введите количество записей '))

err = 0
mx = P_deg
sr = 0
p = 0

for i in range(n):
    C_deg = input('Значение:')
    
    if C_deg == 'error':
        err += 1
    else:
        C_deg = float(C_deg)
        sr += C_deg
        if C_deg > mx:
             mx = C_deg
        if C_deg > P_deg:
            p += 1

print('Всего значений: ', n)
print('Ошибок: ', err)
print('Превышений порога: ', p)
print(f'Максимальное показание: {mx:.1f}')
print(f'Среднее показание: {sr / (n - err):.1f}')
    