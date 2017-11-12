# crawler
**这是一个爬虫代码训练仓库**

---

## 代码目录

- [jwc_sign_up.py](https://github.com/peiqiaoWang/crawler/blob/master/jwc_sign_up.py)（模拟登入fzu教务处）
- [practice.py](https://github.com/peiqiaoWang/crawler/blob/master/practice.py) （简单的学习一下爬虫)
- [jwc_next.py](https://github.com/peiqiaoWang/crawler/blob/master/jwc_next.py)（模拟登入fzu教务处，并查看相关信息）

---

## 学习链接

**了解全貌**

- [知乎第一个和第二个回答](https://www.zhihu.com/question/20899988)

**关于爬虫**

- [《Python爬虫学习系列教程》学习笔记](http://www.cnblogs.com/xin-xin/p/4297852.html)

**关于正则表达式**

- [正则表达式](http://cuiqingcai.com/977.html)

  几个常用的搭配

> 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。
>
> 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。