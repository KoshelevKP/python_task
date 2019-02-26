
# coding: utf-8

# In[2]:

# задание 1
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(long_phrase) > len(short_phrase):
    print("long_phrase длиннее чем short_phrase")
else:
    print("short_phrase длиннее чем long_phrase")


# In[5]:

# задание 2
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'

i_count = 0
a_count = 0

for char in text:
    if char == 'а':
        a_count += 1
    if char == 'и':
        i_count += 1

if i_count > a_count:
    print('"и" втречается чаще')
else:
    if i_count == a_count:
        print('"и" и "а" втречаются одиноковое количество раз')
    else:
        print('"а" втречается чаще')


# In[11]:

# задание 3
byte_file_size = 231000

mb_file_size = byte_file_size/1024/1024

result = 'Объем файла равен {:.2} Mb'.format(mb_file_size)
print (result)


# In[20]:

# задание 4 и 5
import math

x = math.sin(math.pi/6)

print(x)
print(0.1+0.2)


# In[27]:

# задание 6
a = 3
b = 2

[a, b] = [b, a]

print('a = ' + str(a) + ', b = ' + str(b))


# In[51]:

# задание 7
import math

num_2 = 10011

length_num = math.trunc(math.log(num_2, 10)) + 1 #определяем колечесвто разрядов

num10 = 0

for n in range (1,length_num+1):
    num10 += num_2 % 10 * (2**(n-1))
    num_2 = math.trunc(num_2/10)
    
print(num10)

