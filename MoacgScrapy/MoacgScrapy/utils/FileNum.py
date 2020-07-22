from scrapy.utils.project import get_project_settings
from googletrans import Translator
import os,requests


# 获取文件夹下所有文件数量

def GetFileNum(Filename):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    FileName = IMAGES_STORE+"/"+Filename
    if os.path.exists(FileName) == False:
        os.mkdir(FileName)
    return len([lists for lists in os.listdir(FileName) if os.path.isdir(os.path.join(FileName, lists))])
