#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.webdriver.common.keys import Keys
from numpy import random


# In[15]:


class Igbot:
    def __init__(self, username, password, mode = "UI"):
        """
        (username, password, mode = "UI")
        ---------
        username - enter username for account to perform actions 
        password - enter the one coreespondign to username
        mode = 'UI' to have a Chrome window opened or 'headless' just to get results returned
        
        This function initialises the selenium browser with login.
        """
        self.username = username
        options = ChromeOptions()
        options.add_argument("--start-maximized") #make full screen size
        if mode == 'headless':
            options.add_argument('headless') #to avoid chrome window open and speed up 
        self.driver = webdriver.Chrome(options = options) #to make full screen
        self.driver.get("https://www.instagram.com/") #connect to start page
        sleep(3) #wait
        self.driver.find_element_by_xpath("//input[@name = 'username']").send_keys(username) #type in username
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password) #type in password
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type = 'submit']/div[contains(text(),'Log In')]").click() # click login
        
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div/div[3]/form/div[2]/span/button").click() #confirm the enter if needed
        except:
            pass
        
        if mode == "UI":
            try:
                sleep(5)
                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() #close pop-up window with "Not now"
            except:
                print("""Не удалось войти в аккаунт. Пожалуйста, проверьте правильность введенных логина и пароля. Если все верно, попробуйте осуществить вход вручную через браузер и подтвердить почту либо номер телефона, к которому привязан аккаунт""")

    
    def getUserFollowers(self, username, N, mode = "followers"):
        """
        (self, username, N, mode = "followers")
        ---------
        username - the user to collect following or followers of
        N - how many people names to collect
        mode - one of 'followers' or 'followings'. Which information to collect: followers or followings
        
        This function collects the followers or following list by the username provided
        """
        self.driver.get('https://www.instagram.com/' + username)
        #find and click followers or following button
        try:
            if mode == "followings":
                followersLink = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a') #followings
            else:
                followersLink = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a') #followers
            followersLink.click()
            sleep(2) #wait a bit
            followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            scrollbox = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]') # capture pop-up window to scroll down
            # scrolling down
            while numberOfFollowersInList < N: #scrolling down with script to load the list of needed number of usermanes
                numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbox)
                sleep(random.randint(500,1000)/1000) #wait for some time before continuing scrolling   
        except:
            followersList = []
        #collecting usernames
        followers = []
        try:
            for user in followersList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                followers.append(userLink)
                if (len(followers) == N): #limit with the N instances
                    break
        except:
            pass
        return followers # return last N followers
    
    def promote(self, N, target_u_followers, current_followers, current_followings):
        """
        (self, N, target_u_followers, current_followers)
        --------
        N - number of randomly chosen accounts among followers of target user
        target_u_followers - the result of getUserFollowers(), a list of names collected
        current_followers - the followers you already have as a list
        
        This function chooses N accounts for you to follow and conducts following
        """
        to_follow = []
        indices = []
        iter_ = 0
        # get numbet of accounts to choose for following
        if type(N) != int:
            print("Введите, пожалуйста, целое число:")
            N = int(input())
        if N >= 10: #check for not being out of range
            print(f"Число слишком большое. Введите число менее 10, поскольку одновременная подписка на большее число аккаунтов блокируется") #исходя из лимита подписок в час без блокировки действия
            N = int(input())
        #  choose unique N indicies for accounts to follow
        while len(to_follow)<N:
            if iter_ < N*2:
                i = random.randint(0, N)
                if i not in indices:
                    indices.append(i)
                    to_follow.append(target_u_followers[i])
                    iter_ += 1
            else:
                break
        
        to_follow_clear = []
        for name in to_follow:
            #check for presense in history
            if (name not in current_followers) and (name not in current_followings):
                to_follow_clear.append(name)
        self.to_follow_clear = to_follow_clear
        print(f"Введите 'Да', чтобы подписаться на {len(to_follow_clear)} аккаунтов:")
        for u in to_follow_clear:
            print(u) #to see the accounts chosen
        action = input()
        if action == 'Да':
            for user in to_follow_clear:
                url = user
                self.driver.get(url)
                sleep(3)
                self.driver.find_element_by_css_selector('button').click() #click follow
                sleep(10)

            print("Готово!")
        
        return to_follow_clear
    
    def unfollow_unmut(self, current_followers, current_followings):
        to_unfollow = []
        for user in current_followings:
            if user not in current_followers:
                to_unfollow.append(user)
        iter_ = 0
        for u in to_unfollow:
            if iter_ < 10:
                url = user
                self.driver.get(url)
                sleep(3)
                #self.driver.find_elements_by_css_selector('button')[2].click() #click unfollow
                self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button').click()
                self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_').click()
                sleep(10)
            else:
                break
        


