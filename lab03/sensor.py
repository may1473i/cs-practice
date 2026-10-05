P_deg = float(input('Введите порог в градусах Цельсия '))
n = int(input('Введите количество записей '))

err = 0
mx = 0
sr = 0

for i in range(n):
    C_deg = input('Значение:')

    if C_deg == 'error':
        err += 1
    else:
        C_deg = int(C_deg)
        sr += C_deg
        if C_deg > P_deg:
             mx = C_deg

print(err, mx, sr / (n - err))
    