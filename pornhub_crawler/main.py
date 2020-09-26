# Author": "lzkgbld",
#  "Date": 2020/9/20 12:56
#  "LastEditors": "lzkgbld"
#  "LastEditTime": 2020/9/20 12:56
from tool.video_download import por_favorites, por_type


if __name__ == "__main__":
    # 调用方法将txt数据读取到list中
    txt_data = []
    for line in open('configure.txt', "r", encoding='UTF-8'):
        txt_data.append(line.strip('\n'))
    cl_video_type =None
    cl_path = None
    cl_num = None
    cl_end = None
    cl_url = None
    cl_type = None
    cl_host = None
    cl_user = None
    cl_pwd = None
    cl_name = None
    user_name = None
    user_pwd = None
    # 进行数据分类
    # 如果只抓收藏，在完整地址输入抓的ID即可，默认抓收藏夹全部内容
    # 选择收藏类型只需要填存储文件夹和完整地址里面输入ID即可，其他不会受到任何影响
    for t in txt_data:
        if t.split("==")[0] in "爬取类型(1:分类 2:收藏)":
            cl_video_type = int(t.split("==")[1])
        elif t.split("==")[0] in "存储文件夹":
            cl_path = t.split("==")[1]
        elif t.split("==")[0] in "起始页":
            cl_num = t.split("==")[1]
        elif t.split("==")[0] in "结束页":
            cl_end = t.split("==")[1]
        elif t.split("==")[0] in "完整地址":
            cl_url = t.split("==")[1]
        elif t.split("==")[0] in "是否收费(1:免费 2:收费视频)":
            cl_type = t.split("==")[1]
        elif t.split("==")[0] in "数据库地址":
            cl_host = t.split("==")[1]
        elif t.split("==")[0] in "数据库账号":
            cl_user = t.split("==")[1]
        elif t.split("==")[0] in "数据库密码":
            cl_pwd = t.split("==")[1]
        elif t.split("==")[0] in "数据库名称":
            cl_name = t.split("==")[1]
        elif t.split("==")[0] in "账号":
            user_name = t.split("==")[1]
        elif t.split("==")[0] in "密码":
            user_pwd = t.split("==")[1]
    if cl_video_type == 1:
        por_type(cl_num, cl_end, cl_url, cl_type, cl_path, cl_host, cl_user, cl_pwd, cl_name, user_name, user_pwd)
    elif cl_video_type == 2:
        por_favorites(cl_url, cl_path, cl_host, cl_user, cl_pwd, cl_name)

# D:/Demo/video
# 101749201