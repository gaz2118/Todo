#!/usr/bin/env python
# coding: utf-8

# In[18]:


s = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=s)


# In[23]:


name = input()
print('Привет, -', name, end='')


# In[1]:


a = int(input())
print(a, 9, 10, sep="\n")


# In[14]:


a = int(input()
print(a, a+1, a+2, sep="\n", end='')


# In[17]:


a = int(input())
print(a, a+1, a+2, sep="\n", end='')


# In[19]:


a = int(input())
c = int(input())
d = int(input())
print(a+c+d)


# In[22]:


a = int(input())
print('Объем =', a*a*a)
print('Площадь полной поверхности =', 6*a*a) 


# In[27]:


a = int(input())
b = int(input())
print(3*((a+b)*(a+b)*(a+b))+275*(b*b)-127*a-41)


# In[26]:


a = int(input())
b = int(input())
print(3*(a+b)**3+275*b**2-127*a-41)


# In[32]:


a = int(input())
v = a ** 3
s = 6 * (a ** 2)
print("Объем = ", v, "\nПлощадь полной поверхности = ", s)


# In[34]:


a = int(input())
print('Следующее за числом',a , 'число:', a+1)
print('Для числа', a ,'предыдущее число:', a-1)


# In[35]:


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(3*(a+b+c+d))


# In[36]:


a = int(input())  # Стоимость монитора
b = int(input())  # Стоимость системного блока
c = int(input())  # Стоимость клавиатуры
d = int(input())  # Стоимость мыши
print((a + b + c + d) * 3)


# In[14]:


a, b = int(input()), int(input())
c = a + b
k = a - b
s = a * b
print(str(a), "+", str(b), "=", c, sep=" ",end="    ")
print(str(a), "-", str(b), "=", k)
print(str(a), "*", str(b), "=", s)


# In[15]:


a = int(input()) 
b = int(input()) 
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)


# In[31]:


print(2// 7)


# In[33]:


23//7


# In[34]:


123//10


# In[35]:


20//5


# In[36]:


2//5


# In[37]:


15//2


# In[38]:


29%5


# In[39]:


a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)


# In[41]:


-2**5


# In[42]:


b1, q, n = int(input()), int(input()), int(input())
print(b1 * q ** (n-1))


# In[43]:


a = int(input())
print(a // 100)


# In[45]:


n, k = int(input()), int(input())
print(k // n)
print(k % n)


# In[48]:


99//2


# In[51]:


124234413532/2


# In[59]:


a = int(input())
print(a - a // 2)


# In[57]:


1132//2


# In[58]:


1133//2


# In[60]:


# m - число мест в купе
# n - номер места в вагоне
# k - номер купе

n = int(input())
m = 4
k = (n + m - 1) // m
print(k)


# In[63]:


n = int(input())
print((n + 3)//4)


# In[71]:


a = int(input())
print((a-1) // 4 + 1)



# In[73]:


a = int(input())
b = a // 60
c = a % 60
print(a, 'мин - это', b, 'час', c, 'минут.')


# In[1]:


num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Искомое число =', last_digit * 10 + first_digit)


# In[2]:


num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')


# In[12]:


num = int(input())
digit3 = num % 10
print(digit3)


# In[13]:


num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
sum = digit1 + digit2 + digit3
umn = digit1 * digit2 * digit3
print("Сумма цифр =", sum)
print("Произведение цифр =", umn)


# In[34]:


num = int(input())
a = num % 10
c = (num % 100) // 10
d = num // 100
s = 
print(d, c, a)
print(d, a, c)
print(c, d, a)
print(c, a, d)
print(a, d, c)
print(a, c, d)


# In[36]:


num =int(input())
c = num % 10
b = (num % 100) // 10
a = num // 100
print(a * 100 + b * 10 + c) 
print(a*100+c*10+b)
print(b*100+a*10+c)
print(b*100+c*10+a)
print(c*100+a*10+b)
print(c*100+b*10+a)


# In[45]:


123//100


# In[47]:


num = int(input())
a = num % 10
c = (num % 100) // 10
d = num // 100


print(a, c, d)


# In[50]:


3281%10000


# In[52]:


num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)


# In[56]:


i = int(input())
    
            if i / 2:
            print(i, 'чётное')
                else:
                    print(i, 'нечётное')
                if i // 2:
                    print(i, 'чётное')
                else:
                    print(i, 'нечётное')
                if i % 2 == 0:
                    print(i, 'чётное')
                else:
                    print(i, 'нечётное')
                if i // 2 == 0:
                    print(i, 'чётное')
                else:
                    print(i, 'нечётное')
                if i % 2 != 0:
                    print(i, 'нечётное')
                else:
                    print(i, 'чётное')
                if i // 2 != 0:
                    print(i, 'нечётное')
                else:
                    print(i, 'чётное')


# In[ ]:




