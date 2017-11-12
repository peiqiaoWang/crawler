# -*- coding: utf-8 -*-
import urllib2
import urllib
import re


page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

# pattern = re.compile('<div.*?author\sclearfix">.*?<div.*?content">.*?<span>(.*?)</span>.*?'
                     # + '<div class="stats-vote">.*?number">(.*?)</i>', re.S)

pattern = re.compile('<div.*?content">.*?<span>(.*?)</span>.*?stats">.*?<span.*?i.*?number">(.*?)<', re.S)


try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    content = response.read().decode('utf-8')
    # print content
    items = re.findall(pattern, content)
    for item in items:
        print item[0], item[1]
except urllib2.URLError, e:
    print urllib2.URLError
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason