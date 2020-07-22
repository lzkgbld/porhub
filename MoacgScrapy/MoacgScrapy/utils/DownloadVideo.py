import os,youtube_dl


class GetItem(object):
    file_path = None

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            file_name = self.file_path+'{}.mp4'.format(d['filename'])
            os.rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

    def download(self,youtube_url, download_path):
        self.file_path = download_path
        # 定义某些下载参数
        ydl_opts = {
            'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(title)s%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # 下载给定的URL列表
            result = ydl.download([youtube_url])