
# from .settings import IMAGES_STORE
from scrapy.utils.project import get_project_settings
import os


def GetFileNum(Filename):
    # IMAGES_STORE = '/www/MOACG/mostore/comic/detailed/cover'
    IMAGES_STORES = get_project_settings().get("IMAGES_STORE")
    filename = IMAGES_STORES+"/"+Filename
    if os.path.exists(filename) == False:
        os.mkdir(filename)
    return len([lists for lists in os.listdir(filename) if os.path.isdir(os.path.join(filename, lists))])


