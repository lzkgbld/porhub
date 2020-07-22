import pymysql, time, os


class ManagementMysql(object):

    # 检查是否重复
    def check_video(self,video_name):
        try:
            conn = pymysql.connect(host="127.0.0.1", user="", password="", database="", charset="utf8")
            cursor = conn.cursor()
            # 搜索数据库是否已有该内容
            cursor.execute("SELECT Video_Name from DownloadRecord_pornhubdownloadrecord WHERE Video_Name=" + "'" + str(video_name) + "'" + ";")
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
            with open("checklog.txt", "a+",encoding='utf-8') as f:
                f.writelines(str(e))
                f.writelines("\n")
                f.writelines("错误视频名:"+str(video_name))
                f.writelines("\n")
                f.writelines("错误发生时间:" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
                f.writelines("\n")

    # 检查路径
    def check_path(self,video_path):
        try:
            conn = pymysql.connect(host="127.0.0.1", user="videodownload", password="bRBHt6T2ihByE7XN", database="videodownload", charset="utf8")
            cursor = conn.cursor()
            # 搜索数据库是否已有该内容
            cursor.execute("SELECT Video_Path from DownloadRecord_pornhubdownloadrecord WHERE Video_Path=" + "'" + str(video_path) + "'" + ";")
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
            with open("check_path.txt", "a+",encoding='utf-8') as f:
                f.writelines(str(e))
                f.writelines("\n")
                f.writelines("错误文件夹路径:"+str(video_path))
                f.writelines("\n")
                f.writelines("错误发生时间:" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
                f.writelines("\n")

    # 写入下载信息数据
    def add_video(self,video_name,video_path,video_url):
        try:
            conn = pymysql.connect(host="127.0.0.1", user="videodownload", password="bRBHt6T2ihByE7XN", database="videodownload", charset="utf8")
            cursor = conn.cursor()
            # 二次检查数据库是否存在
            cursor.execute("SELECT Video_Name from DownloadRecord_pornhubdownloadrecord WHERE Video_Name=" + "'" + str(video_name) + "'" + ";")
            if cursor.fetchone():
                return "NO"
            else:
                cursor = conn.cursor()
                # 数据库插入语句
                cursor.execute("INSERT INTO DownloadRecord_pornhubdownloadrecord(Video_Name,Video_Path,Video_Url,Video_Time) values ('%s','%s','%s','%s')" %(str(video_name),str(video_path),str(video_url),str(time.strftime("%Y-%m-%d %H:%M:%S"))))
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
            with open("add_video.txt", "a+") as f:
                f.writelines(str(e))
                f.writelines("\n")
                f.writelines("错误视频名:"+str(video_name))
                f.writelines("\n")
                f.writelines("错误视频路径:" + str(video_path))
                f.writelines("\n")
                f.writelines("错误发生时间:" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
                f.writelines("\n")
