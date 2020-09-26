# Author": "lzkgbld",
#  "Date": 2020/9/20 13:26
#  "LastEditors": "lzkgbld"
#  "LastEditTime": 2020/9/20 13:26
import pymysql, time, os


class ManagementMysql(object):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 检查视频是否存在
    def check_video(self, video_url):
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset="utf8")
            cursor = conn.cursor()
            # 搜索数据库是否已有该内容
            cursor.execute("SELECT video_url from video WHERE video_url=" + "'" + str(video_url) + "'" + ";")
            # 关闭数据库连接
            cursor.close()
            conn.close()
            if cursor.fetchone():
                return "NO"
            else:
                return "OK"
        except Exception as e:
            # 如果文件存在则删除
            # if os.path.exists("checklog.txt"):
            #     os.remove("dest.txt")
            # 写出错误log日志
            with open("check_log.txt", "a+",encoding='utf-8') as f:
                f.writelines(str(e))
                f.writelines("\n")
                f.writelines("错误视频URL地址:"+str(video_url))
                f.writelines("\n")
                f.writelines("错误发生时间:" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
                f.writelines("\n")

    def add_video(self, video_url):
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset="utf8")
            cursor = conn.cursor()
            # 搜索数据库是否已有该内容
            cursor.execute("SELECT video_url from video WHERE video_url=" + "'" + str(video_url) + "'" + ";")
            # 关闭数据库连接
            cursor.close()
            conn.close()
            if cursor.fetchone():
                return "视频已存在"
            else:
                cursor = conn.cursor()
                # 数据库插入语句
                cursor.execute(
                    "INSERT INTO video(video_url) values ('%s')" % (str(video_url)))
                # 执行插入语句
                conn.commit()
                # 关闭数据库连接
                cursor.close()
                conn.close()

        except Exception as e:
            # 如果文件存在则删除
            # if os.path.exists("checklog.txt"):
            #     os.remove("dest.txt")
            # 写出错误log日志
            with open("add_log.txt", "a+",encoding='utf-8') as f:
                f.writelines(str(e))
                f.writelines("\n")
                f.writelines("添加错误URL地址:"+str(video_url))
                f.writelines("\n")
                f.writelines("错误发生时间:" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
                f.writelines("\n")