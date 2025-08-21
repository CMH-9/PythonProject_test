import requests # 导入爬虫工具
url =""
r = requests.get(url).content#content是二进制数据
with open('r.mp3','wb') as f:
    f.write(r)