#!/usr/bin/env python
# coding: utf-8

# In[1]:


from InstaBot_selenium_version_cleanup_comments import Igbot


# In[ ]:


print("Введите, пожалуйста, логин:")
user = input()
print("Введите, пожалуйста, пароль:")
pswrd = input()


# In[ ]:


bot = Igbot(user, pswrd)


# In[ ]:


print("Введите, пожалуйста, сколько Ваших подписчиков учитывать при отборе аккаунтов для подписки:")
m_followers = int(input())
print("Введите, пожалуйста, сколько Ваших подписок учитывать при отборе аккаунтов для подписки:")
m_followings = int(input())
print("Введите, пожалуйста, наименование аккаунта, на подписчиков которых Вы хотите подписаться:")
target_user = input()
print("Введите, пожалуйста, сколько последних подписчиков целевого аккаунта нужно сохранить:")
n_target = int(input())


# In[ ]:


my_followers = bot.getUserFollowers(user, m_followers, mode = "followers")
my_followings = bot.getUserFollowers(user, m_followings, mode = "followings")
user_f = bot.getUserFollowers(target_user, n_target)


# In[ ]:


print("Сколько аккаунтов Вы хотите выбрать для подписки? Введите число не более 10:")
N = int(input())


# In[ ]:


bot.promote(N, user_f, my_followers, my_followings)

