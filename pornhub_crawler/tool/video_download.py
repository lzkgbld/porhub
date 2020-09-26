# Author": "lzkgbld",
#  "Date": 2020/9/20 12:57
#  "LastEditors": "lzkgbld"
#  "LastEditTime": 2020/9/20 12:57
import requests, os
from lxml import etree
from tool.mysql import ManagementMysql


def por_favorites(video_id, video_file, host, user, password, name):
    # 创建mysql工具类 请注释
    mysql = ManagementMysql(host, user, password, name)
    # 原地址
    video_url = 'https://cn.pornhub.com'
    # 获取视频数量
    num_url = 'https://cn.pornhub.com/playlist/'+video_id
    # 获取视频列表
    html_num = requests.get(num_url)
    html_num = html_num.text
    html_num = etree.HTML(html_num)
    data_num = html_num.xpath('//*[@id="aboutPlaylist"]/div[1]/text()')
    video_num = data_num[1].strip()
    video_num = int(video_num.split('个')[0].split('-')[-1].strip())
    video_num = int(video_num/50)+1
    num = 1
    page = 0
    while num <= video_num:
        # 获取视频列表
        url = 'https://cn.pornhub.com/playlist/viewChunked?id='+video_id+'&offset='+str(num)+'&itemsPerPage=50'
        # 获取视频链接
        html = requests.get(url)
        html = html.text
        html = etree.HTML(html)
        data = html.xpath("//li/div/div/a/@href")
        for d in data:
            dd = d.split('&')[0]
            video_u = video_url+dd
            # 如果不需要去重请注释这句话
            if mysql.check_video(video_u) == "OK":
                # 添加下载任务  Linux="youtube-dl " + video_u + " -o " +video_file + "/" + "%\(title\)s.%\(ext\)s"
                cmd = "youtube-dl -f 1080p " + video_u + " -o " + video_file + "/" + "%\(title\)s.%\(ext\)s"
                print(cmd)
                results = os.system(cmd)
                print("下载状态" + str(results))
                if results == 0:
                    pass
                else:
                    cmd1 = "youtube-dl " + video_u + " -o " +video_file + "/" + "%\(title\)s.%\(ext\)s"
                    print(cmd1)
                    # 添加下载任务
                    results = os.system(cmd1)
                    print("画质下载错误,使用备用方案，选择已有最好画质下载")
                    print("修正下载状态码" + str(results))
                # 请注释这条添加语句
                mysql.add_video(url)
            else:
                print("视频重复:"+video_u)
        page += 50
        num += 1


def por_type(start_num, end_num, video_url, charge_type, video_file, host, user, password, name, user_name, user_pwd):
    start_num = int(start_num)
    end_num = int(end_num)
    # 创建mysql工具类 请注释
    mysql = ManagementMysql(host, user, password, name)
    urls = 'https://cn.pornhub.com'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'
    }
    # 不收费类型
    if charge_type == 1:
        while start_num <= end_num:
            urls = video_url + '&page=' + str(start_num)
            html = requests.get(urls, headers=headers).text
            html = etree.HTML(html)
            video_list = html.xpath('//*[@data-segment="straight"]/div/div[1]/a/@href')
            for vl in video_list:
                # 拼接地址下载
                url = urls+vl
                if mysql.check_video(url) == "OK":
                    # 添加下载任务  Linux="youtube-dl " + url + " -o " +video_file + "/" + "%\(title\)s.%\(ext\)s"
                    cmd = "youtube-dl -f 1080p " + url + " -o " + video_file + "/" + "%\(title\)s.%\(ext\)s"
                    results = os.system(cmd)
                    print("下载状态" + str(results))
                    if results == 0:
                        pass
                    else:
                        cmd1 = "youtube-dl " + url + " -o " +video_file + "/" + "%\(title\)s.%\(ext\)s"
                        # 添加下载任务
                        results = os.system(cmd1)
                        print("画质下载错误,使用备用方案，选择已有最好画质下载")
                        print("修正下载状态码" + str(results))
                    # 请注释这条添加语句
                    mysql.add_video(url)
                else:
                    print("视频重复:"+url)

            start_num += 1
    # 收费类型
    elif charge_type == 2:
        urls = 'https://cn.pornhubpremium.com'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            'Referer': 'https://cn.pornhubpremium.com/premium/login'
        }

        html_login = requests.get('https://cn.pornhubpremium.com/premium/login')
        h_cookie = html_login.cookies
        h_cookie = requests.utils.dict_from_cookiejar(h_cookie)
        html_login = html_login.text
        html = etree.HTML(html_login)
        token = html.xpath('//*[@id="token"]/@value')
        token = token[0]
        redirect = {'from': 'pc_premium_login', 'segment': 'straight'}
        # username=用户名  password=密码
        data = {'username': user_name, 'password': user_pwd, 'token': token, 'redirect': redirect}
        r = requests.post("https://cn.pornhubpremium.com/front/authenticate", headers=headers, data=data,
                          cookies=h_cookie)
        # print(r.text)
        cookice = r.cookies
        cookice = requests.utils.dict_from_cookiejar(cookice)

        while start_num <= end_num:
            urls = video_url + '&page=' + str(start_num)
            html = requests.get(urls, headers=headers, cookice=cookice).text
            html = etree.HTML(html)
            video_list = html.xpath('//*[@data-segment="straight"]/div/div[1]/a/@href')
            for vl in video_list:
                # 拼接地址下载
                url = urls+vl
                # 如果需要进行去重验证请注释这条IF语句
                if mysql.check_video(url) == "OK":
                    # 添加下载任务  Linux="youtube-dl " + url + " -o " +video_file + "/" + "%\(title\)s.%\(ext\)s"
                    cmd = "youtube-dl -f 1080p " + url +' --cookies cookies.txt -o ' + video_file + "/" + "%\(title\)s.%\(ext\)s"
                    results = os.system(cmd)
                    print("下载状态" + str(results))
                    if results == 0:
                        pass
                    else:
                        cmd1 = "youtube-dl " + url +' --cookies cookies.txt -o ' + video_file + "/" + "%\(title\)s.%\(ext\)s"
                        # 添加下载任务
                        results = os.system(cmd1)
                        print("画质下载错误,使用备用方案，选择已有最好画质下载")
                        print("修正下载状态码" + str(results))
                    # 请注释这条添加语句
                    mysql.add_video(url)
                else:
                    print("视频重复:"+url)
            start_num += 1