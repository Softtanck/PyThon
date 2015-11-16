#By:Tanck
import urllib2
import urllib
import math
import thread

def readUrl(readtimes,url):
    for i in range(readtimes): #read times
        #url = '' #your url
        req = urllib2.Request(url, headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        oper = urllib2.urlopen(req)
        print "currentTimes:",i+1
    print("over")

def callRead(url,times):
    thread.start_new_thread(readUrl, (times,url))

def startThread(): #Use thread.start_new_thread() to create many new read url threads  
    callRead("http://blog.csdn.net/u010316858/article/details/46778365",421)
    callRead("http://blog.csdn.net/u010316858/article/details/45025531",330)
    callRead("http://blog.csdn.net/u010316858/article/details/41286979",260)


if __name__=='__main__':
    startThread()
