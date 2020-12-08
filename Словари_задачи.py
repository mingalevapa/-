#!/usr/bin/env python
# coding: utf-8

# 1) На основе переданной строки (не содержащей повторяющихся символов) создать словарь, в котром каждому символу строки будет соответствовать номер символа в строке. Пример: строка 'abcdef'

# In[1]:


l1 = list('abcd')
l1


# In[2]:


d1 = {'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10}
d1


# 2) Определить сколько элементов заданного списка содержится в словаре. Пример: определить сколько элементов списка l1 содержится в словаре d1 (ответ: 2)

# In[3]:


evgene_o = """My uncle -- high ideals inspire him;
     but when past joking he fell sick,
     he really forced one to admire him --
     and never played a shrewder trick.
     Let others learn from his example!
     But God, how deadly dull to sample
     sickroom attendance night and day
     and never stir a foot away!
     And the sly baseness, fit to throttle,
     of entertaining the half-dead:
     one smoothes the pillows down in bed,
     and glumly serves the medicine bottle,
     and sighs, and asks oneself all through:
     When will the devil come for you?
     
     Such were a young rake's meditations --
     by will of Zeus, the high and just,
     the legatee of his relations --
     as horses whirled him through the dust.
     Friends of my Ruslan and Lyudmila,
     without preliminary feeler
     let me acquaint you on the nail
     with this the hero of my tale:
     Onegin, my good friend, was littered
     and bred upon the Neva's brink,
     where you were born as well, I think,
     reader, or where you've shone and glittered!
     There once I too strolled back and forth:
     but I'm allergic to the North..."""


# 3) Для строки evgene_o создать словарь где для всех символов, встречающихся в строке хранится число: сколько раз символ встретился в строке evgene_o. 

# 4) Используя словарь, полученный в задаче 3 подсчитать количество строчных букв в строке evgene_o. 

# In[4]:


dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60} 


# 5) Написать код, который создает новый словарь с именем dic4, содержащий все пары ключ-значение из словарей dic1, dic2, dic3.

# In[11]:


dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}
dic4 = dic1
dic4.update(dic2)
dic4.update(dic3)


# In[12]:


dic4


# 6) Просуммировать все значения из словаря dic4

# In[14]:


dic4[1]+dic4[2]+dic4[3]+dic4[4]+dic4[5]+dic4[6]


# 7) Перемножить все значения из словаря dic4

# In[15]:


dic4[1]*dic4[2]*dic4[3]*dic4[4]*dic4[5]*dic4[6]


# 8) Просуммировать произведения ключей на словаря dic4 на соответствующие им значения

# In[ ]:





# In[5]:


dic5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
dic6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}


# 9) На базе словаря dic6 создать словарь dic7 в котором нет пар ключ-значение с ключами, встречающимися в словаре dic5

# 10) Создать словарь dic8 в котором есть все пары ключ-значения из dic5, а для ключей, которые есть в dic6, но отсутствуют в dic5 добавить соответствующие пары ключ-значения в dic8.

# In[6]:


import random
ri1 = [random.randint(1, 15) for _ in range(30)]
print(ri1)


# 11) Из списка ri1 получить упорядоченный по возрастанию список не имеющий повторяющихся значений.

# 12) Используя распаковку из списка списков сделать список, содержащий последовательность первых и последних значений вложенных списков и сохраняющий порядок их следования.
# 
# Пример: [[1, 2, 3], [4, 5, 6, 7], [9, 2]] -> [1, 3, 4, 7, 9, 2]

# 13)  В словаре, полученном в задаче 3 удалить все пары ключ/значение для символов, встречающихся менее 5 раз.

# 14) Составить программу "мешок". Программа раз за разом запрашивает у пользователя новые значения и "кладет их в мешок". Если полученное значение уже есть в мешке, то оно не помещается в мешок, а пользователю сообщается о том, что такое значение уже есть в мешке. Максимальное количество значений в мешке - 5 штук. Если помещение в мешок очередного значения приводит к превышению допустимого количества значений, то из него извлекается одно из хранившихся в нем ранее значений и предъявляется пользователю. Для того чтобы выйти из программы пользователь вводит пустое значение. При выходе из программы пользователю демонстрируется содержимое мешка.
# 
# \*) Дополнительная опция: пользователь может вводить сразу несколько значений, разделенных запятой.

# In[ ]:


bag=[]
while True:
    inp_val=input()
    if inp_val=='':
        print(bag)
        break
    elif inp_val in bag:
        print("Данное значение уже есть в мешке")
        continue
    else:
        if len(bag)==5:
            print(f'Удаленное значение: {bag.pop(0)}')
            bag.append(inp_val)
            print(f'Добавленное значение: {bag[-1]}')
        else:
            bag.append(inp_val)
            print(f'Добавленное значение: {bag[-1]}')


# 
