result = []
m = ()
print('Добро пожаловать в игру!')
n = int(input('Какое число (от 3 до 20) на первом столбе?: '))
for i in range(1, n):
    for j in range(i+1, n):
        k = i + j
        if n % k == 0:
            m = (f'{i}{j}')
            result.append(m)
            continue

result= ''.join(result)
print('Ваш пароль: ', result)