#!/usr/bin/env python
# coding: utf-8

# In[1]:


from InstaBot_selenium_version_cleanup_comments import Igbot


# In[ ]:


print("Specify language: 'ru' or 'eng')
l = input()


# In[ ]:


if l == 'ru':
    print("Введите, пожалуйста, логин:")
    user = input()
    print("Введите, пожалуйста, пароль:")
    pswrd = input()
    bot = Igbot(user, pswrd)
    print("Введите, пожалуйста, сколько Ваших подписчиков учитывать при отборе аккаунтов для подписки:")
    m_followers = int(input())
    print("Введите, пожалуйста, сколько Ваших подписок учитывать при отборе аккаунтов для подписки:")
    m_followings = int(input())
    print("Введите, пожалуйста, наименование аккаунта, на подписчиков которых Вы хотите подписаться:")
    target_user = input()
    print("Введите, пожалуйста, сколько последних подписчиков целевого аккаунта нужно сохранить:")
    n_target = int(input())
    my_followers = bot.getUserFollowers(user, m_followers, mode = "followers")
    my_followings = bot.getUserFollowers(user, m_followings, mode = "followings")
    user_f = bot.getUserFollowers(target_user, n_target)
    print("Сколько аккаунтов Вы хотите выбрать для подписки? Введите число не более 10:")
    N = int(input())
    bot.promote(N, user_f, my_followers, my_followings)
else:
    print("Введите, пожалуйста, логин:")
    user = input()
    print("Введите, пожалуйста, пароль:")
    pswrd = input()
    bot = Igbot(user, pswrd)
    print("Введите, пожалуйста, сколько Ваших подписчиков учитывать при отборе аккаунтов для подписки:")
    m_followers = int(input())
    print("Введите, пожалуйста, сколько Ваших подписок учитывать при отборе аккаунтов для подписки:")
    m_followings = int(input())
    print("Введите, пожалуйста, наименование аккаунта, на подписчиков которых Вы хотите подписаться:")
    target_user = input()
    print("Введите, пожалуйста, сколько последних подписчиков целевого аккаунта нужно сохранить:")
    n_target = int(input())
    my_followers = bot.getUserFollowers(user, m_followers, mode = "followers")
    my_followings = bot.getUserFollowers(user, m_followings, mode = "followings")
    user_f = bot.getUserFollowers(target_user, n_target)
    print("Сколько аккаунтов Вы хотите выбрать для подписки? Введите число не более 10:")
    N = int(input())
    bot.promote(N, user_f, my_followers, my_followings)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



