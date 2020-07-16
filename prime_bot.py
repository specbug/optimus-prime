#!/usr/bin/env python
# coding: utf-8

# In[47]:


import tweepy
import os
import numpy as np
import datetime


# In[48]:


consumer_key = 'idRM2Gd434GELnVIJxtk8F3Ly' 
consumer_secret = '8iLvHK7U80nxp4JAynNx96MEh2UixfddALebiShZAj7JHYH5UA' 
access_token = '1283305452269260803-0iddWDQ0gc828LjvDbc5iPoEs6qpEh'
access_token_secret = 'CZkh3ZmEnzB0iGYjy6BbGsTeITtu050y5QSgiV5SmgQla'


# In[49]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# In[50]:


l_tweets = [str(t.text) for t in tweepy.Cursor(api.user_timeline, id='primes_bot').items()]
len(l_tweets)


# In[51]:


with open('primes.txt', mode='r') as f:
    for line in f:
        words = line.split(',')
        start_n = int(words[-1])
        break
    
yr = int(datetime.datetime.now().year)
mn = int(datetime.datetime.now().month)
dy = int(datetime.datetime.now().day)
hr = int(max(1, datetime.datetime.now().hour))

end_n = yr*mn*dy*hr

print(start_n, end_n)


# In[52]:


def sieve_of_eratosthenes(n, primes=[]): 
    prime_flag = [False]*(n+1) 
      
    for i in range(2, n+1): 
        if not prime_flag[i]: 
            primes.append(i) 
            for j in range(i, n+1, i): 
                prime_flag[j] = True
                
    return primes

def prime_range(s, e):
    
    n = int(np.floor(np.sqrt(e))) + 1
    primes = sieve_of_eratosthenes(n) 
        
    r = e-s+1
    
    mark = [False]*(r+1)
    
    for i in range(len(primes)): 
        
        low_lim = int(np.floor(s/primes[i])) * primes[i]
        
        if low_lim < s: 
            low_lim += primes[i] 
        if low_lim == primes[i]: 
            low_lim += primes[i] 
            
        for j in range(low_lim, e+1, primes[i]): 
            mark[j-s] = True
            
    return [i for i in range(s, e+1) if not mark[i-s]]


# In[53]:


if start_n != end_n: 
    l_primes = prime_range(start_n, end_n)
    if len(l_primes) > 0:
        with open('primes.txt', 'a') as f:
            f.write(', '+', '.join([str(i) for i in l_primes]))
        
with open('primes.txt', mode='r') as f:
    for line in f:
        words = line.split(',')
        api.update_status(np.random.choice(list(set(words) - set(l_tweets))))

