# 使用Python的scrapy框架开发的pornhub视频爬虫。


## 使用方法：

1.部署环境
pip install -r requirements.txt

2.修改配置文件
请打开configure.txt文件进行修改.

3.创建数据库环境(可选)
此步不一定需要,仅是为了防止第二次运行导致获取重复视频,如果需要请按照下面数据库结构进行创建.
由于使用pymysql进行连接,请自行修改utils下面WriteMysql.py文件,将里面配置信息填上您数据库的配置信息.
数据库构建有两种方案:
1.下载项目中的pornhubdownload.sql
2.自行构建,结构为video_name,video_path,为字段名，类型为varchar.
`video_name` varchar(255) NULL,`video_path` varchar(255) NULL
3.随后需要修改pipelines.py文件里面的语句,把里面添加数据库语句和判断视频重复语句打开,去掉注释即可.

4.运行爬虫,进入目录看到main.py文件,直接运行Python main.py



## 如果需要下载pornhub会员收费视频,请执行下列步骤



1.请使用对应cookie获取插件,获取cookie值,比如谷歌浏览器请使用cookies.txt(https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg)
由于本人只有谷歌，获取cookie浏览器插件仅介绍谷歌能用的,其他浏览器请自行寻找其他插件,将下载的cookie文本里面的内容全部复制粘贴,替换源码中的cookies.txt里面内容.

2.请打开源码内spiders文件夹里面的spider.py,在第五十行中有两个字典对象,分别是username和password,请在这里填写自己会员账号密码,让爬虫有权限进去获取内容,这里我解释一下,cookies是给下载用的.
由于某些技术问题导致获取信息的时候需要模拟登陆,下载采取用cookies文件获取下载权限,后期可能会考虑修复这个毛病.

3.请在下载配置文件主动填写对应的配置信息.(1:免费 2:收费视频)

4.运行爬虫,进入目录看到main.py文件,直接运行Python main.py


## 备注:
如果有任何问题请留言,尽可能修复.
预计后面会配置一个页面控制端,运行在页面直接配置好信息后直接调度爬虫...(开发时间未定)

画质自动下载1080p如果有需要请pipelines.py文件里面第26行修改那段代码里面的1080p选项,可改正720p和480p,请确定P站有的画质!
请Linux运行的哥们修改一下pipelines.py文件,把最后的%(title)s.%(ext)s修改为%\(title\)s.%\(ext\)s  (原因是Linux不识别%加括号的命令....)
