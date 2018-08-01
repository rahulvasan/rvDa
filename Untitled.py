
# coding: utf-8

# In[10]:


import urllib.request
import pandas as pd
import os
df=pd.read_csv("MovieGenre.csv",encoding="latin1")
posters=df.Poster
genre=df.Genre
title=df.Title
for i in range(1000):
    print (i)
    a=genre[i].split('|')
    b=a[0]
    newpath = "c:/rv/exp/" + b
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if "https://" in str(posters[i]):
        try:
            urllib.request.urlretrieve(posters[i],"c:/rv/exp/"+b+"/"+title[i]+".jpg")
        except IOError:
            print("Invalid Poster")
            continue
            

