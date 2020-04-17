#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import openpyxl
import pandas as pd


# In[2]:


def getID(api):
    uID = api.username_id
    return uID


# In[6]:


def getTotalFollowers(api, user_id, output = "usernames"):
    """
    api = Instagram api object with login()
    user_id = pk number or api.username_id value. To get your id, run getUserID() on api
    output = "usernames" (default), "pk", "full"
    
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    
    To get followers of self account, do not specify user_id. Otherwise enter 'pk' entity.
    Output can be usernames, ID's or full (json)
    """

    import time
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        time.sleep(3) #to avoid blocking
    if output != "full":
        follows_list = []
        for user in followers:
            if output == "usernames":
                follows_list.append(user['username'])
            else:
                follows_list.append(user['pk'])
        return follows_list
    else:
        return followers


# In[8]:


def getTotalFollows(api, user_id, output = "usernames"):
    """
    api = Instagram api object with login()
    user_id = pk number or api.username_id value. To get your id, run getUserID() on api
    output = "usernames" (default), "pk", "full"
    
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    
    To get followers of self account, do not specify user_id. Otherwise enter 'pk' entity.
    Output can be usernames, ID's or full (json)
    """

    import time
    follows = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        follows.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        time.sleep(1) #to avoid blocking
    if output != "full":
        followings_list = []
        for user in follows:
            if output == "usernames":
                followings_list.append(user['username'])
            else:
                followings_list.append(user['pk'])
        return followings_list
    else:
        return follows


# In[8]:


def get_usr_id(username):
    "username (str) - enter the name of Istagram user to get ID"
#     print("Введите имя пользователя:")
#     username = str(input())
    url = f"https://www.instagram.com/{username}/?__a=1"
    get_page = requests.get(url)
    id_ = get_page.json()['graphql']['user']['id']
    return id_


# In[ ]:


def get_history(filename = "History.xlsx"):
    try:
        file = pd.read_excel(filename)
        return file
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "History"
        sheet_h = wb["History"]
        sheet_h['A1'] = "followed_hist"
        wb.save(filename)
        file_ = pd.read_excel(filename)
        return file_
    


# In[ ]:





# In[ ]:




