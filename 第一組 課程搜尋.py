
# coding: utf-8

# In[14]:

ntust={'經濟學':'TR-412-2','計概':'MA-303','國文':'tr-309','微積分':'IB-306','英文字彙':'tr-609','英文口語':'IB-611',
       '管理學':'IB-502','法律與生活':'tr-310-1'}
print("課程列表: 經濟學 計概 國文 微積分 英文字彙 英文口語 管理學 法律與生活")
a=input("請輸入課程名稱：")
b=ntust.get(a,'沒有此課程')
print(b)
while True:
    c=input("是否繼續查詢:")
    if c=="是":
        a=input("請輸入課程名稱：")
        b=ntust.get(a,'沒有此課程')
        print(b)
    else :
        break
    


# In[13]:




# In[ ]:



