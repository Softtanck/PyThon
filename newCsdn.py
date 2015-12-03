#By:Tanck
import urllib2
import urllib
import math
import json
    

def startThread(times): 
    for i in range(times):
        addComment("http://blog.csdn.net/u010316858/comment/submit?id=50112725") # this need comment id.

#delte score for csdn
def deleteComment(url):
    req = urllib2.Request(url, headers = {
            'Connection': 'Keep-Alive',# this cookie is other account.
            'Cookie':'bdshare_firstime=1447232219913; uuid_tt_dd=5986093432674467892_20151111; __gads=ID=4e8b7d524daec6c7:T=1447232220:S=ALNI_MbkH7ng0cPlgfNH4unhI1XZo10nKQ; __qca=P0-1401388616-1447232222242; CloudGuest=OqgGkygABYOorxIx2iye8yIvso49BNlLEzS8Luy4zhJn4tThXsiT7GIHKfZMbXteC7CdVvlcclaHdFt8PhS/Y6S6kCSaQ9Sa9El27IeS2Q4Ch3e3Ig+drLvwO075Jl/zXYbVfWTLxHdFC424bb3s5SFzhDoCLYb1TJXYOb/Im0IKxvmRW3MOVXGRzliXruYu; _JQCMT_ifcookie=1; _JQCMT_browser=3c08e6f1e91182dc617a39007cd0b88d; __message_district_code=510000; FullCookie=1; cache_cart_num=0; _ga=GA1.2.761241429.1447730839; lzstat_uv=883228072758227966|3497199@3573258@3603851@3596993@3434703@3593393@3311294@3525517@3311322@3590372@3606012@20071207@3602465@2981463; scvh=2014-10-22+17%3a54%3a46+008; uuid=d7f796a5-3188-4180-b77b-99a869587603; UserName=u014024936; UserInfo=mACNdeE1g1tSUbRU0qSRPTzjOXb4BFjotua5jwGYBS6G88mzsMf7v5h71WW5EyUseJ7U%2Bgw%2F4yXcm%2BRchkMUqL0EbC2r2c9rwmKNFMbUJWHZh5Eoy4TD4OANLJ42gTBH; UserNick=%E6%88%91%E7%88%B1%E5%90%83%E6%B3%A1%E9%9D%A2; AU=8C0; UN=u014024936; UE="5088541@qq.com"; access-token=f81b8e9f-0e31-4a02-93a7-622e7ab4ade7; ViewMode=list; avh=50125917%2c49408103%2c6294292%2c50053097; dc_tos=nyrf41; dc_session_id=1449108208300; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Host':'blog.csdn.net',
            'Referer':'http://blog.csdn.net/u010316858/article/details/50112725',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
    oper = urllib2.urlopen(req)
    temp = oper.read()
    print 'success delete' + temp
    
#add score for csdn
def addComment(url):
    datas = {'commentid':'','content':'test','replyId':''}
    data = urllib.urlencode(datas)
    req = urllib2.Request(url,data, headers = {
            'Connection': 'Keep-Alive',# this cookie is other account.
            'Cookie':'bdshare_firstime=1447232219913; uuid_tt_dd=5986093432674467892_20151111; __gads=ID=4e8b7d524daec6c7:T=1447232220:S=ALNI_MbkH7ng0cPlgfNH4unhI1XZo10nKQ; __qca=P0-1401388616-1447232222242; CloudGuest=OqgGkygABYOorxIx2iye8yIvso49BNlLEzS8Luy4zhJn4tThXsiT7GIHKfZMbXteC7CdVvlcclaHdFt8PhS/Y6S6kCSaQ9Sa9El27IeS2Q4Ch3e3Ig+drLvwO075Jl/zXYbVfWTLxHdFC424bb3s5SFzhDoCLYb1TJXYOb/Im0IKxvmRW3MOVXGRzliXruYu; _JQCMT_ifcookie=1; _JQCMT_browser=3c08e6f1e91182dc617a39007cd0b88d; __message_district_code=510000; FullCookie=1; cache_cart_num=0; _ga=GA1.2.761241429.1447730839; lzstat_uv=883228072758227966|3497199@3573258@3603851@3596993@3434703@3593393@3311294@3525517@3311322@3590372@3606012@20071207@3602465@2981463; scvh=2014-10-22+17%3a54%3a46+008; uuid=d7f796a5-3188-4180-b77b-99a869587603; UserName=u014024936; UserInfo=mACNdeE1g1tSUbRU0qSRPTzjOXb4BFjotua5jwGYBS6G88mzsMf7v5h71WW5EyUseJ7U%2Bgw%2F4yXcm%2BRchkMUqL0EbC2r2c9rwmKNFMbUJWHZh5Eoy4TD4OANLJ42gTBH; UserNick=%E6%88%91%E7%88%B1%E5%90%83%E6%B3%A1%E9%9D%A2; AU=8C0; UN=u014024936; UE="5088541@qq.com"; access-token=f81b8e9f-0e31-4a02-93a7-622e7ab4ade7; ViewMode=list; avh=50125917%2c49408103%2c6294292%2c50053097; dc_tos=nyrf41; dc_session_id=1449108208300; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Host':'blog.csdn.net',
            'Referer':'http://blog.csdn.net/u010316858/article/details/50112725',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
    oper = urllib2.urlopen(req)
    temp = oper.read()
    print temp
    s = json.loads(temp)
    commentTemp = ''
    commentTemp = s['data']
    print commentTemp
    if commentTemp == None or commentTemp.strip() == '': # is comment fail.?
        print 'comment fail,data is null'
    else:# do delete comment
        deleteComment('http://blog.csdn.net/qq_21268999/comment/delete?commentid='+s['data']+'&filename=50157639') #your other account info.
    
if __name__=='__main__':
    startThread(0) #chang your times for add score.
