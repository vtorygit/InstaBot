#!/usr/bin/env python
# coding: utf-8


from jupyter_notebook.Bot_src import Igbot

print("Specify language: 'ru' or 'eng'")
l = input()

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
    my_followers = bot.getUserFollowers(user, m_followers, mode = "followers")
    my_followings = bot.getUserFollowers(user, m_followings, mode = "followings")
    bot.unfollow_unmut(my_followers, my_followings)
else:
    print("Insert login:")
    user = input()
    print("Insert password:")
    pswrd = input()
    bot = Igbot(user, pswrd)
    print("Insert the number of your followers to account for:")
    m_followers = int(input())
    print("Insert the number of your followings to account for:")
    m_followings = int(input())
    my_followers = bot.getUserFollowers(user, m_followers, mode = "followers")
    my_followings = bot.getUserFollowers(user, m_followings, mode = "followings")
    bot.unfollow_unmut(my_followers, my_followings)




