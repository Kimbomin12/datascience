#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
for loops
"""

nums={1,2,3,4,5}
for num in nums:
    print(num)   #들여쓰기 안하면 indentationError가 발생한다.
    #code1
    #code2
    
#range()
print()

nums=range(10) #create (0,1,2,3,4,....,10)
for num in nums: 
    print(num)


# In[2]:


"""
continue Keyword
"""

nums = [1,2,-1,4,-5,5,2,-9]
for num in nums:
    #If num is negative, we skip it(음수 생략하고 양수만 출력)
    if num<0:
        continue
    print(num)
    


# In[6]:


"""
break Keywor
"""

game_plays = ['stage1','stage2','stage3', 'gameover','stage4','stage5']

for play in game_plays:
    if play=='gameover':
        print("Game is over...")
        break
    print(play+"is complete.")


# In[11]:


"""
List Comprehension
"""
one_to_ten = [i+1 for i in range(10)]   #현실에서는 1번부터 숫자세니까
print(one_to_ten)


for i in range(10): #0부터 숫자 10개 나열
    print(i)
    


# In[16]:


"""
List Comprehension including conditions
"""

hotspurs=[['손흥민','A+'],['해리 케인','F'],['탕기 은돔벨레','F',],['델리 알리','B'],['로카스 모우라','B+'],['이메르송','D']]
poors = [player[0] for player in hotspurs if player[1]=='F']   
print("감독님한테 혼날 사람:")
print(poors)

                                                                                                                 


# In[17]:


"""
while loops
"""

hungry = True
foods_on_table = ['참치김밥','순대','로제떡볶이','김말이','오뎅','단무지','고로케']
foods_num=7 #음식 수
ate_num=0 #먹은 음식 수
while ate_num<4:
    print(foods_on_table[ate_num]+"냠냠")
    ate_num+=1
print("배부르다..여기까지")


# In[ ]:


"""
Infinite Loop
"""
x=1
y=1
while x<5:
    print("Do something")
    y+=1
    if y>5:
        print("Why doen't it end?")

