from string import ascii_letters as let, digits as dig
from random import choice
from clipboard import copy
from datetime import date
s = ''
for i in range(15):
    s += choice(let + dig)
print('Ваш новый пароль:', s)
out = open('Почта.txt', 'a')
print(str(date.today()), s, file=out)
out.close()
copy(s)

