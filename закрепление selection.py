#!/usr/bin/env python
# coding: utf-8

# In[3]:




print('Python', 'is the best', '!!')



print("раз", "два, "три")


# In[4]:


print("Honey, what's your hurry", end='?')


# In[5]:


print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')


# In[6]:


print("Told you not to worry", "But maybe that's a lie", sep=' :) ')


# In[7]:


print("Remember not to get too close to stars", "They're never gonna give you love like ours", sepp=" ")


# In[8]:


a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)


# In[31]:


print('*' * 17, sep = '')
print('*', '*', sep = " " * 15)
print('*', '*', sep = " " * 15)
print('*' * 17, sep = '')


# In[33]:


a = int(input())
b = int(input())
c = (a + b) ** 2
d = (a ** 2) + (b ** 2)
print(('Квадрат суммы', a, 'и', b, 'равен', c), ('Сумма сумма квадратов', a, 'и', b, 'равен', d), sep='\n'


# In[35]:


a = int(input())
b = int(input())
c = (a + b) ** 2
d = (a ** 2) + (b ** 2)
print('Квадрат суммы', a, 'и', b, 'равен', c)
print('Сумма сумма квадратов', a, 'и', b, 'равен', d)


# In[45]:


a, b, c, d = int(input()), int(input()), int(input()), int(input())
s =  (a ** b) + (c ** d)                                                      
print(s)


# In[1]:


a = str(input())
b = a + a
c = a + a + a
print(int(a) + int(b) + int(c))


# In[8]:


n = int(input())
a = n % 10000 // 1000
b = n % 1000 // 100
c = n % 100 // 10
d = (n % 10)
if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')


# In[1]:


a, b = int(input()), int(input())
print (min(a,b))


# In[3]:


print(min(int(input()), int(input())))


# In[7]:


a ,b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    san = b
else:
    san = a
if c > d:
    san1 = d
else:
    san1 = c
if san > san1:
    print(san1)
else:
    print(san)


# In[8]:


a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)


# In[9]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = 0
m = 0
if a < b:
    n = a
else:
    n = b
if c < d:
    m = c
else:
    m = d
if n < m:
    print(n)
else:
    print(m)


# In[10]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and a < c and a < d:
    print(a)
if b <= a and b < c and b < d:
    print(b)
if c <= a and c <= b and c < d:    
    print(c)
if d < a and d <= c and d < b:
    print(d)


# In[11]:


a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b <= a: a = b
if c <= a: a = c
if d <= a: a = d
print(a)


# In[12]:


n = int(input())
if n <= 13:
    print('детство')
if 14 < n < 24:
    print('молодость')
if 25 < n < 59:
    print('зрелость')
if n >= 60:
    print('старость')


# In[13]:


x = int(input())
if x <= 13:
    print('детство')
else:
    if 14 <= x <= 24:
        print('молодость')
    else:
        if 25 <= x <= 59:
            print('зрелость')
        else: 
            if x >= 60:
                print('старость')


# In[14]:


a = int(input())

if a < 14:
  print('детство')
else:
  if a < 25:
    print('молодость')
  else:
    if a < 60:
      print('зрелость')
    else:
      if a > 59:
        print('старость')


# In[15]:


a=int(input())
if a>=60:
    print('старость')
elif a>=25:
    print('зрелость')
elif a>=14:
    print('молодость')
else:
    print('детство')


# In[18]:


x = int(input())
if x <= 24:
    print('детство' if x <= 13 else 'молодость')
else:
    print('старость' if x >=60 else 'зрелость' )


# In[19]:


age = int(input())
print(("детство","молодость","зрелость","старость")[(14<=age<=24) + 2*(25<=age<=59) + 3*(age>=60)])


# In[37]:


a ,b, c, = int(input()), int(input()), int(input())
f = 0
if a >= 0:
    f = f + a
else:
    a == 0
if b >= 0:
    f = f + b
else: 
    b == 0
if c >= 0:
    f = f + c
else:  
    c == 0
print(f)


# In[38]:


a, b, c, s = int(input()), int(input()), int(input()), 0
if a > 0:
    s += a
if b > 0:
    s += b
if c > 0:
    s += c
print(s)


# In[39]:


a, b, c=int(input()), int(input()), int(input())
if a>0:
    a=a
else:
    a=0
if b>0:
    b=b
else:
    b=0
if c>0:
    c=c
else:
    c=0
print(a+b+c)


# In[40]:


a = int(input())
b = int(input())
c = int(input())
if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
print(a + b + c + 0)


# In[ ]:




