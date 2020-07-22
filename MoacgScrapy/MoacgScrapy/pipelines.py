import os, requests, time, re
from io import BytesIO
from PIL import Image
from scrapy.utils.project import get_project_settings
from MoacgScrapy.utils.WriteMysql import ManagementMysql
from MoacgScrapy.utils.DownloadVideo import GetItem


class MoacgscrapyPipeline(object):
    def process_item(self, item, spider):
        # 视频下载地址
        video_url = item['splj']
        # 存储路径
        video_path = item['spfile']
        # 过滤特殊符号
        video_names = re.sub(r'[\/?"<>|].', '-', item['spmc'])
        video_names = video_names.replace(".","")
        # 创建数据库分类 如果需要使用数据库请把下面代码#去掉
        # mysql = ManagementMysql()

        # 检查视频是否重复  使用数据库请把下面代码#去掉
        # if mysql.check_video(video_names) == "NO":
        #     print("视频已重复"+str(video_names))
        #     return item

        # 添加下载任务
        cmd = "youtube-dl -f 1080p " + video_url +' --cookies cookies.txt -o ' + video_path + "/" + "%(title)s.%(ext)s"
        results = os.system(cmd)
        print("下载状态"+str(results))
        if results == 0:
            # 添加下载记录 使用数据库请把下面代码#去掉
            # mysql.add_video(video_names, video_path + "/" + video_names,video_url)
            pass
        else:
            cmd1 = "youtube-dl " + video_url + ' --cookies cookies.txt -o ' + video_path + "/" + "%(title)s.%(ext)s"
            print(cmd1)
            # 添加下载任务
            results = os.system(cmd1)
            print("画质下载错误,使用备用方案，选择已有最好画质下载")
            print("修正下载状态码"+str(results))
            # 添加下载记录 使用数据库请把下面代码#去掉
            # mysql.add_video(video_names, video_path + "/" + video_names,video_url)
        return item



