


## 使用方法：

1.部署环境
pip install -r requirements.txt
--2.
手动安装环境：(以下库默认请安装最新版)
1.request
2.PyMySQL
3.youtube-dl
4.lxml
5.requests-toolbelt

2.修改配置文件
请打开configure.txt文件进行修改.

3.创建数据库环境(可选)
此步不一定需要,仅是为了防止第二次运行导致获取重复视频,如果需要请按照下面数据库结构进行创建.
数据库相关配置信息请自行前往configure.txt填写。
去重原理是数据库只会记录抓取视频地址，由于名称存储使用pymysql存储会出现一些奇怪的错误,所以选择根据url地址进行去重。
数据库构建有两种方案:
1.自行导入pornhub_video.sql文件
2.自行创建数据库,并且在configure.txt填写好数据库名称，确定里面有张表名称为video,如果需要更换请自行修改源码目录下的tool/mysql.py。
3.如果使用自行创建数据库造成的数据库执行出错,请自行研究源码修复,本人不做过多的指导！

3--1
如果不需要去重,请自行打开源码里面tool/video_download.py下面留下注释的执行语句,但是请确保configure.txt的数据还是有填写的,请勿留空.


4.运行爬虫,进入目录看到main.py文件,直接运行Python main.py



## 如果需要下载pornhub会员收费视频,请执行下列步骤



1.请使用对应cookie获取插件,获取cookie值,比如谷歌浏览器请使用cookies.txt(https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg)
由于本人只有谷歌，获取cookie浏览器插件仅介绍谷歌能用的,其他浏览器请自行寻找其他插件,将下载的cookie文本里面的内容全部复制粘贴,替换源码中的cookies.txt里面内容.

2.请在configure.txt填好账号密码,请确定能够访问付费视频权限的账号！

3.请在下载配置文件主动填写对应的配置信息.(1:免费 2:收费视频)

4.运行爬虫,进入目录看到main.py文件,直接运行Python main.py


## 备注:
如果有任何问题请留言,尽可能修复.
预计后面会配置一个页面控制端,运行在页面直接配置好信息后直接调度爬虫...(开发时间未定)

画质自动下载1080p如果有需要请pipelines.py文件里面第26行修改那段代码里面的1080p选项,可改正720p和480p,请确定P站有的画质!
请Linux运行的哥们修改一下pipelines.py文件,把最后的%(title)s.%(ext)s修改为%\(title\)s.%\(ext\)s  (原因是Linux不识别%加括号的命令....)
