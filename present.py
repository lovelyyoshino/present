# -*- coding: utf-8 -*-
import requests
import datetime
import time
import operator
def CurrentTime():
    current=str(int(time.mktime(datetime.datetime.now().timetuple())))
    #print(current)
    return  current
#CurrentTime()
print(datetime.datetime.now().timetuple())
print ("1为抢年兽，2为抢台历，3为(坷垃，喵娘，灯笼)，4免费舰长，5贤者石头，6专抢灯笼")
str1 = input("Enter your number: ");
cookies=input("Enter your cookies: ");
cookies1='LIVE_BUVID=e256b91db3db0d82041af54e59e3c3d0; LIVE_BUVID__ckMd5=f529ac9b536218f1; bili_jct=e0306b8ccd64a81098f135db2df7f089; DedeUserID=27793897; DedeUserID__ckMd5=28b0477391e7646b; SESSDATA=9722d437%2C1518254483%2C059f4a4e; JSESSIONID=30565BC9010BA05D8E47F463E3EE2AC7; sid=m4iwoihz'
while 1:
    current_TIME=time.strftime('%M',time.localtime(time.time()))
    #print(current_TIME)
    #https://api.live.bilibili.com/activity/v1/NewSpring/redBagPool?_=1516334716372 api
    url="https://api.live.bilibili.com/activity/v1/NewSpring/redBagPool?_="+str(CurrentTime())#获取url
    headers = {'Cookie': cookies}
    respone = requests.get(url, headers=headers)
    #print (respone.json())
    my_num=respone.json()['data']['red_bag_num']
    if int(my_num)==0:
        print ("请输入正确的cookies")
    #print (my_num)
    for i in range (0,8):#获取8个数0-7
        leave=respone.json()['data']['pool_list'][i]['stock_num']
        name = respone.json()['data']['pool_list'][i]['award_name']
        #print (str(name)+"剩余数量"+str(leave))
        if(int(str1)==1):
            if name=="年兽头衔" and my_num>999 and leave!=0:
                if int(current_TIME)<30 or int(current_TIME)>50:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload={"award_id":"title-92","exchange_num":"1"}
                    respone1=requests.post(url1,headers=headers,data=payload)
                    print (respone1.json())
                '''else:
                    print("error")'''
            '''else:
                url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                payload={"award_id":"title-92","exchange_num":"1"}
                respone1=requests.post(url1,headers=headers,data=payload)
                print (respone1.json())'''
        elif(int(str1)==2):
            if my_num>8888 and leave!=0:
                if int(current_TIME)<30 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "award-calendar", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
        elif(int(str1)==3):
            if  my_num>450 and leave>0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "gift-3", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
            elif  my_num>233 and leave>0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "gift-4", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
            elif my_num>15 and leave>0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "gift-109", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
        elif (int(str1) == 4):
            if name=="舰长体验券（一个月）" and my_num > 6699 and leave > 0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "guard-3", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
        elif (int(str1) == 5):
            if name=="贤者之石"and my_num > 1888 and leave > 0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "stuff-3", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
        elif (int(str1) == 6):
            if name=="红灯笼" and my_num>15 and leave>0:
                if int(current_TIME)<2 or int(current_TIME)>58:
                    url1='https://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'
                    payload = {"award_id": "gift-109", "exchange_num": "1"}
                    respone1 = requests.post(url1, headers=headers, data=payload)
                    print (respone1.json())
