# -*- coding: utf-8 -*-
import urllib2
import urllib
import httplib

class TextBrower:
    '''
    A Text based brower to get webpage
    '''
    def __init__(self,header=None):
        '''
        Initial parameters for brower
        '''
        if header==None:
            self.header= {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': ('Mozilla/5.0 (Linux; U; Android 4.0.4; zh-CN; Lenovo A798t Build/IMM76D)' 
                    'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.9.439 U3/0.8.0 Mobile Safari/533.1'),
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4'    
            }
    def t_get(self,url,data=None):
        '''
        get method,type(data)=dict
        '''
        
        host =  url.split('/')[2]
        conn = httplib.HTTPConnection(host)
        ####get data
        if data!=None:
            param = ''
            for k,v in data.items():
                param = param + k + '=' + v.encode('utf-8')+ '&'
            url = url + '?' + param[:-1] 
               
        conn.request(method="GET",url=url,headers=self.header)
        response = conn.getresponse()
        
        respond_header = response.getheaders()        
        res= response.read()
        
        conn.close()
        return respond_header,res
        
        
    def t_get1(self,url,data=None):
        '''
        get methond,type(data)=dict
        '''
        try:
            head = dict(self.header)
            req = urllib2.Request(url,headers=head)
            if data!=None:
                data = urllib.urlencode(data)
                data = data.encode('utf-8')

                fp = urllib2.urlopen(req,data)
            else:                
                fp = urllib2.urlopen(req)
            html = fp.read()
            #type1 = sys.getfilesystemencoding()      # local encode format  
            #html.decode("UTF-8").encode(type1)  # convert encode format
        except Exception as e:
            print 'Exception:',e
            return None
        
        return html
    
    def t_post(self,url,data=None):
        '''
        post method,type(data)=dict
        '''
        head = self.header
        head['Content-type']="application/x-www-form-urlencoded"
        
        host =  url.split('/')[2]
        conn = httplib.HTTPConnection(host)
        ####get data
        if data!=None and isinstance(data, dict):
            data = urllib.urlencode(data)
            data = data.encode('utf-8')
            
        conn.request(method="POST",url=url,body=data,headers=head)
        response = conn.getresponse()
        
        respond_header = response.getheaders()        
        res= response.read()
        
        conn.close()
        return respond_header,res

    
