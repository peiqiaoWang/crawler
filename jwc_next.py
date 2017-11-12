# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import re


page = 1
url = 'http://59.77.226.32/logincheck.asp'
cookies = cookielib.CookieJar()
postdata = urllib.urlencode({
    'muser': '031402418',
    'passwd': '041033',
    'x': 50,
    'y': 20
})
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
# opener.addheaders.append(('User-Agent', user_agent))
# opener.addheaders.append(('Host', '59.77.226.32'))
# opener.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'))
# opener.addheaders.append(('Accept-Encoding', 'gzip, deflate'))
# opener.addheaders.append(('Accept-Language', 'zh-CN,zh;q=0.8'))
# opener.addheaders.append(('Origin', 'http://jwch.fzu.edu.cn'))
opener.addheaders.append(('Referer', 'http://jwch.fzu.edu.cn/'))
# opener.addheaders.append(('Cache-Control', 'max-age=0'))
# opener.addheaders.append(('Connection', 'keep-alive'))
# opener.addheaders.append(('Content-Type', 'application/x-www-form-urlencoded'))
# opener.addheaders.append(('Upgrade-Insecure-Requests', '1'))



request = urllib2.Request(url=url, data=postdata)
result = opener.open(request)
# result = opener.open('')
result = result.read().decode('utf-8')
# print result
pattern = re.compile('top.*?id=(.*?)"', re.S)
cotent = re.findall(pattern, result)
# print cotent[0]
gradeurl = 'http://59.77.226.35/jcxx/xsxx/StudentInformation.aspx?id='+str(cotent[0])
result = opener.open(gradeurl)
result = result.read().decode('utf-8')
print result
