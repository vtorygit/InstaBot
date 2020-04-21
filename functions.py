#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import openpyxl
import pandas as pd


# In[2]:


def getID(api):
    uID = api.username_id #get username id as an attribute of api object created by package InstagramAPI
    return uID


# In[6]:


def getTotalFollowers(api, user_id, is_pop = True,output = "usernames"):
    """
    api = Instagram api object with login()
    user_id = pk number or api.username_id value. To get your id, run getUserID() on api
    is_pop = True (default) means that account has more than 10000 followers. If True,
    the number of followers list is limited to 10000. To avoid it specify is_pop=False
    output = "usernames" (default), "pk", "full"
    -----------
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    
    To get followers of self account, do not specify user_id. Otherwise enter 'pk' entity.
    Output can be usernames, ID's or full (json)
    """

    # it's an upgraded version of getUserFollowers function from InstagramAPI package
    # that solves problems with extraction of limited number of followers
    
    import time
    followers = []
    next_max_id = True
    if is_pop == True:
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = api.getUserFollowers(user_id, maxid=next_max_id) #"_" keeps the last value
            # this solution was provided in github issue comments to the package used
            followers.extend(api.LastJson.get('users', []))
            next_max_id = api.LastJson.get('next_max_id', '')
            if len(followers) >= 10000:
                next_max_id = False
            time.sleep(3) #to avoid blocking, was added by me after being blocked for 24h
    else:
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = api.getUserFollowers(user_id, maxid=next_max_id) #"_" keeps the last value
            # this solution was provided in github issue comments to the package used
            followers.extend(api.LastJson.get('users', []))
            next_max_id = api.LastJson.get('next_max_id', '')
            time.sleep(3)
        
    if output != "full": #full output means returning all the possible information
        follows_list = []
        for user in followers:
            if output == "usernames": # to return the list of usernames
                follows_list.append(user['username'])
            else:
                follows_list.append(user['pk']) #to return the list of IDs
        return follows_list
    else: #return full informations as JSON
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

        _ = api.getUserFollowings(user_id, maxid=next_max_id) #works the same way but with different function from package
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
    #this website is a JSON with needed information about any account
    get_page = requests.get(url)
    id_ = get_page.json()['graphql']['user']['id']
    return id_


# In[ ]:


def get_history(filename = "History.xlsx"):
    """filename = name of excel file with 'followed_hist' as first column header """
    try:
        file = pd.read_excel(filename) #read file if it is in the directory and provided by user
        return file
    except FileNotFoundError: #if the file is not found, create
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "History"
        sheet_h = wb["History"]
        sheet_h['A1'] = "followed_hist"
        sheet_h['B1'] = "datetime"
        wb.save(filename)
        file_ = pd.read_excel(filename)
        return file_
    


# In[ ]:


def follow_user_list(api, userlist):
    for user in userlist:
        ID = get_usr_id(user)
        api.follow(ID)
        time.sleep(5)


# In[ ]:




