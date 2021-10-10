#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
Lists
"""

primes=[2,3,5,7,11,2]
print(primes)

empty_list=[]
print(empty_list)


# In[9]:


"""
Multiple different data types
"""
mixed =['Jenny',1,14,True]
print(mixed)
list_of_lists=[['a',1],['b',2]]


# In[11]:


"""
Zero-indexing
"""

names=['Roger','Rafeal','Andy','Novak']

print(names[0]) #first data
print(names[1]) #second data
print(names[2]) #third data
print(names[3]) #last data


# In[13]:


"""
Negative indexing
"""
print(names[-1]) #last data
print(names[-2]) #second to last data
print(names[-3]) #third to last data
print(names[-4]) 


# In[18]:


"""
List slicing
"""
hsu_buildings=['만우관','장공관','필헌관','소통관','송암관','늦봄관','장준하통일관']
building_slice = hsu_buildings[1:4]  #독립적인 객체  
building_slice[0] = '생활관'

print(building_slice)
print(hsu_buildings)#building_slice에 리스트 아이템수정했다고 hsu_buildings원본 리스트에 변화 있는건 아님(슬라이스는 별도의 객체)
print(hsu_buildings[:])#hsu_buildings를 전체 출력 한다는 의미


# In[22]:


#테이블=표=2차원(행,열)

"""
Multi-dimensional List
"""
restaurants=[['해우리','한식','고s'],['짜장명가','중식','중화비빔밥'],['찌개동아리','한식','제육전골'],['맘스터치','양식','싸이버거']] #2차원리스트
print(restaurants)

restaurants[0][2] ='해우라면'
print(restaurants[0])


# In[26]:


"""
Adding Lists Together
"""

items_one = ['cake','cookie', 'bread']
items_two = ['biscuit','tart']

total_items = items_one + items_two #리스트 추가하기(리스트 개별 아이템 추가 : append()또는 insert()사용)

print(total_items)


# In[1]:


"""
Useful Methods for Lists
"""

#Len() : 리스트 크기를 리턴 / 사용법 : len(list)
knapsack = [2,4,3,7,10]
size = len(knapsack) #개수 출력
print(size)

#count() : 특정 아이템의 개수를 리턴 / 사용법 : list.count(item) > 중복허용
backpack = ['pencil','pen','notebook','textbook','pen','highlighter','pen']
numPen = backpack.count('pen') #특정리스트 개수 출력
print(numPen)

#append() > 끝에 추가
orders =['daisies','perwinkle']
orders.append('tulips')
print(orders)

#insert() > 특정위치에 추가
store_line = ['Karla','Maxium','Martin','Isabella']
store_line.insert(2,'Vikor') #2번째에 끼어들기 하는 셈
print(store_line)

#pop() > 특정위치의 아이템을 삭제
sw_subject = ['C Programing','Calculus','Data Engineering','Data Structures','Machine Learning']
sw_subject.pop(2)
print(sw_subject)
sw_subject.pop()
print(sw_subject)

#remove() > 특정 아이템을 삭제
sw_subject.remove('Calculus')
print(sw_subject)

#sort() > 아이템들을 정렬(숫자는 숫자 순서대로, 문자열은 문자대로 정렬 : 오름차순으로 정렬)

numbers=[4,2,1,3]
numbers.sort()
print(numbers)

hsu_buildings=['만우관','장공관','필헌관','소통관','송암관','늦봄관','장준하통일관']
hsu_buildings.sort()
print(hsu_buildings)

#sorted() > 정렬된 리스트를 리턴
numbers = [4,2,1,3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# In[4]:




