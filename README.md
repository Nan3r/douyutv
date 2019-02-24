# pccold

**douyu斗鱼 自动化工具 主播上线通知 & 视频自动录制 & 弹幕抓取 & 下载斗鱼视频**

2018/10/5 by DKZ




## Dependence

- python3
- [streamlink](https://github.com/streamlink/streamlink)
- [bypy](https://github.com/houtianze/bypy)
- [psutil](https://github.com/giampaolo/psutil)

## Config

当前目录下新建conf.py

```
room_id="cold" #斗鱼房间ID
room_num=20360 #斗鱼房间数字ID
stream_type='medium' #录像质量 source|medium|low
is_cut=True #是否分段
how_long=60*30 #录像分段长度(秒)
is_bypy=True #是否使用bypy上传百度云
is_bypy_rm=False #上传百度云后删除
download_path="./download" #录像保存路径
videolist_path='videolist.md' #批量下载斗鱼视频列表

#api
room_api='https://www.douyu.com/betard/' 
room_url="http://www.douyutv.com/"

#邮件配置
my_email="recv@xx.com"
mail_sender='send@xx.com'
mail_passwd='xxx'
mail_host='xxx'
mail_port=25 #exmail.qq 465 or 25
pccold_contact="\n\npccold by DKZ \n---------------------\ngithub:https://github.com/davidkingzyb/pccold\ncontact:davidkingzyb@qq.com  @__DKZ__\naboutme:https://davidkingzyb.tech\n"

#手动录像脚本路径
manual_tmpl_path='./douyutv.py'
now_tmpl_path='xxx'
douyutv_plug_path='/Library/Python/2.7/site-packages/streamlink/plugins/douyutv.py'
```

## Usage

### 上线通知 & 录像 & 弹幕抓取

`$ sh run.sh`

### 自动录像

`$ nohup python3 pccold.py &`

### 弹幕抓取

`$ nohup python3 danmu.py >/dev/null 2>&1 &`

### 下载斗鱼视频

编辑下载列表
格式`[文件名](URL路径)`

`$ nohup python3 videodownload.py &`

### 清除已上传的视频

`$ nohup python3 bypyrm.py &`



### Nan3r

修改于`https://github.com/davidkingzyb/pccold`

修改了获取弹幕的文件，添加了将弹幕转化为ASS的文件，方便在本地观看带弹幕的效果，弹幕太多可能会重合。

当你从百度云或者本地还有视频文件时，使用`python text2ass.py`会读取弹幕文件，然后转为对应的MP4视频的ASS文件。




