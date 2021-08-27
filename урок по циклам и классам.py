#!/usr/bin/env python
# coding: utf-8

# In[34]:


a = 5
while  a > 0:
    print(a, end=" ")
    a -= 1


# In[35]:


a = 5
while a <= 55:
    print(a, end=' ')
    a += 2


# In[36]:


a = 5
while a <= 55:
    if a % 2 == 1:
        print(a, end=' ')
    a += 1


# In[41]:


i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
    print(i)


# In[43]:


n = int(input())
c = 1
while c <= n:
    print('*' * c)
    c += 1


# In[44]:


n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'


# In[45]:


i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1


# In[2]:


c = int (input())
s = 0
while c != 0:
    s = s + c
    c = int (input())
print (s)


# In[16]:


s = 0


while s < 5:
    s = s + 1
    print(s)
    
    
print("buttu")


# In[12]:


a = int(input())
b = int(input())
d = 1
while d % a != 0 or  d % b != 0:
    d += 1
else:
    print(d)


# In[24]:


i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break # досрочно завершаем цикл
    print(a * b)
    i += 1


# In[7]:


# put your python code here
a = int(input())
b = int(input())
d = 1
while d % a != 0 or  d % b != 0:
    d += 1
else:
    print(d)




# In[6]:


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
    print(s)


# In[8]:


while True:
  n = int(input())
  if n > 100: break
  elif n >= 10: print(n)



# In[8]:


while True:
    a = int(input('Введите целое число: '))
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(a)


# In[9]:


a = 0
while a<=100:
  a = int (input())
  if a > 100:
    break
  if a<10:
    continue
print(a)


# In[16]:


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(s)
print(i)


# In[7]:


i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break # досрочно завершаем цикл
    if (a == 0) or (b == 0):
        continue # переходим к следующей итерации
    print(a * b)
    i += 1


# In[10]:


a = int(input())
while a < 101:
    if a > 9:
        print(a)
    a = int(input())


# In[36]:


n = int(input())
for i in range(n):
    print("*" * n)


# In[86]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d+1):
    print('\t', i, end='')
print()
for j in range(a, b+1):
    print(j, end='')
    for g in range(c, d+1):
        print('\t', g*j, end='')
    print()


# In[57]:


n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()


# In[84]:


n = int(input())
for i in range(n):
        print("dos")


# In[88]:


a = int(input())
b = int(input())
s = 0
c = 0
for j in range (a,b+1):
    if j%3 == 0:
        s = s+j #42
        c = c+1
    j+=1
print(s/c)


# In[14]:


genome = input()
cnt = 0
for nucl in genome:
    if nucl == "A":
       cnt += 1
print(cnt)    


# In[15]:


genome = input()
print(genome.count('C'))


# In[17]:


a =  input() # input auto use type str
s1 = a.upper().count('c'.upper())
s2 = a.upper().count('g'.upper())
S=s1+s2
print(S/len(a)*100)


# In[19]:


s = 'abcdefghijk'
s[3:6]
s[:6]
s[3:]
s[::-1]
s[-3:]
s[:-6]
s[-1:-10:-2]


# In[20]:


s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)


# In[22]:


students = ['Амина', 'Али', 'Мыктыбек']
for student in students:
    print("Hello, " + student + "!")


# In[23]:


len(students)


# In[24]:


students[::-1]  # индексация и срезы на списках работают также, как и со строками


# In[26]:


students = ['Ivan', 'Masha', 'Sasha']

teachers = ['Oleg', 'Alex']


# In[27]:


students + teachers


# In[28]:


[0, 1] * 4


# In[29]:


students = ['Ivan', 'Masha', 'Sasha']
students[1] = 'Oleg'
print(students)


# In[34]:


students = ['Ivan', 'Masha', 'Sasha']
students.append('Olga')
print(students)


# In[35]:


students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)


# In[36]:


a = [0] * 5
print(a)


# In[37]:


a = [0 for i in range(5)]
print(a)


# In[38]:


a = [i * i for i in range(5)]
print(a)


# In[46]:


a = [int(i) for i in input().split()]
print(a)


# In[53]:


s = [ int(i) for i in input().split()]
summ = 0 
l = len(s)-1
for i in range(0.1+1):
    summ = summ + s[i]
print(summ)


# In[52]:


s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1


# In[65]:


# n, m, k = (int(i) for i in input(). split())
# a = [[0 for j in range(m)] for i in range(n)]


# In[66]:


# a


# In[78]:


n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1  # расставляем мины
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()


# In[77]:


a


# In[80]:


def f(n):
    return n * 10 + 5
print(f(f(f(10))))


# In[81]:


def f(n):
    return n * 10 + 5

m = f(f(f(10)))
print(m, '-> f(f(f(10)))')

a = f(10) # n * 10 + 5, где n = 10, т.е. 105
b = f(a)  # n * 10 + 5, где n = 105, т.е. 1055
c = f(b)  # n * 10 + 5, где n = 1055, т.е. 10555

print(c, '-> c = f(b), b = f(a), a = f(10)')


# In[2]:


a = input().split()
s = 0
for i in a:
    s += int(i)
    print(s)


# In[3]:


some_numbers = input()
sum = 0
list_of_numbers = some_numbers.split()
 
for num in list_of_numbers:
    sum += int(num)
 
print(sum)


# In[4]:


for i in range(0,8):
  for f in range(0,8):
    print ("*" * f)
  break


# In[5]:


n='*'
for i in range(1,8):
  print(n)
  n+='*'


# In[6]:


print('''*
**
***
****
*****
******
*******''')


# In[7]:


i = 1
while i != 8:
    print('*' * i)
    i += 1


# In[9]:


python ver


# In[11]:


name = input('Как тебя зоиут?')
print('Привет', name)


# In[12]:


print('Kak teby zovut')
name = input()
print('privet', name)


# In[15]:


name = input()
print('Привет,', name)


# In[17]:


name = input()
print('Привет, ',  name)


# In[18]:


print("Привет,", input())


# In[ ]:


'a', str(a)

