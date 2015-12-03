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
            'Cookie':'your cookie',
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
            'Cookie':'your cookie',
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
