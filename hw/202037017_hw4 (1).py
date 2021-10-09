#!/usr/bin/env python
# coding: utf-8

# In[8]:


month = ['쌍', '쇠', '복', '돌', '팽', '육', '쌍', '개', '칠', '갑', '삼', '방']
day = ['봉', '구', '욕', '포', '똥', '삼', '식', '석', '놈', '님', '년', '돌', '단', '득', '방', '질', '장', '걸', '래', '룡', '동', '순', '자', '박', '창', '언', '것', '포', '만', '단', '국']
def get_my_chosun_name(first_name, my_month, my_day):
    print("당신의 조선 이름은 ", first_name, month[my_month-1], day[my_day-1]+ " 입니다")

get_my_chosun_name('김', 12, 26)


# In[1]:




