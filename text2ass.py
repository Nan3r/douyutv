#coding:utf-8
#author:Nan3r
# Dialogue: 0,0:00:00.00,0:00:08.00,R2L,,20,20,2,,{\move(580,25,-20,25)}hiu
# [2019-02-23 01:02:43] [lv23 超超超超级背锅侠]:谢谢大家的支持。
#Dialogue: 0,0:00:02.46,0:00:10.46,R2L,,20,20,2,,{\move(685,25,-125,25)}无赖，剧里最恶心他了
#Dialogue: 0,0:00:17.43,0:00:25.43,R2L,,20,20,2,,{\move(635.5,25,-75.5,25)\c&H9966FF}小帅哥LJ出场
#Dialogue: 0,0:00:26.62,0:00:34.62,R2L,,20,20,2,,{\move(589,25,-29,25)}susu

#每8秒一个弹幕，只是起始时间不一样

import re,datetime,conf

#return "2019-02-23 01:02:43"
def getHourMinute(text):
	r = re.compile(r'\[.*?\]')
	res = r.search(text)
	if res:
		return res.group(0)[1:-1]
	else:
		return False

def getMsg(text):
	r = re.compile(r'\[(lv.*?)\]\:\S*')
	res = r.search(text)
	if res:
		return res.group(0)
	else:
		return False

'''
\move(<x1>,<y1>,<x2>,<y2>[,<t1>,<t2>])
提供字幕的移动效果。<x1>,<y1> 是开始点坐标，<x2>,<y2> 是结束点坐标。
<t1> 和 <t2> 是相对于字幕显示时间的开始运动与结束运动的毫秒时间。

在 <t1> 之前，字幕定位在 <x1>,<y1>。
在 <t1> 与 <t2> 之间，字幕从 <x1>,<y1> 均速移动到 <x2>,<y2>。
在 <t2> 之后，字幕定位在 <x2>,<y2>。
当 <t1> 和 <t2> 没写或者都是 0 时，则在字幕的整段时间内均速移动。
当一行中有多个 \pos 和 \move 时，以第一个为准。
当 \move 和 Effect 效果同时存在时，结果比较迷。
当一行中含有 \move 时会忽略字幕重叠冲突的检测。
'''
def danmuMsg(text):
	#,R2L,,20,20,2,,{\move(589,25,-29,25)}susu
	import random
	t0 = [580, 680, 889, 630, 950, 830, 730, 780]
	t = [25, 135, 85, 230, 280, 330, 380, 180]
	a = random.SystemRandom().choice(t0)
	a1 = random.SystemRandom().choice(t)
	b = 200 - a 
	b1 = a1
	return ',R2L,,20,20,2,,{\\move(%s,%s,%s,%s)}%s' % (str(a), str(a1), str(b), str(b1), text)

def danmuMsg1(text):
	import random
	t = xrange(100, 700)
	t1 = t
	return ',R2L,,20,20,2,,{\\pos(%s,%s)}%s' % (str(random.choice(t)), str(random.choice(t1)), text)


#读取弹幕文件，将时间在开始和结束之间的视频的弹幕，保存为开始时间的名称的ASS
def getVideoDanmu(text, startTime, endTime):
	danmuTime = getHourMinute(text)
	msg = getMsg(text)
	st = startTime.split('.')[0].split('_')
	et = endTime.split('.')[0].split('_')
	fstartTime = '-'.join(st[1:4])+' '+':'.join(st[4:])+':00'
	fendTime = '-'.join(et[1:4])+' '+':'.join(et[4:])+':00'
	if msg and danmuTime:
		ndanmuTime = datetime.datetime.strptime(danmuTime,"%Y-%m-%d %H:%M:%S")
		nstartTime = datetime.datetime.strptime(fstartTime,"%Y-%m-%d %H:%M:%S")
		nendTime = datetime.datetime.strptime(fendTime,"%Y-%m-%d %H:%M:%S")
		if (ndanmuTime < nendTime) and (ndanmuTime > nstartTime):
			resStart = ndanmuTime - nstartTime
			#print resStart
			#print resStart + datetime.timedelta(seconds=8)
			resEnd = resStart + datetime.timedelta(seconds=22)
			#'Dialogue: 0,0:00:02.46,0:00:10.46'
			return "Dialogue: 0,{resStart}.43,{resEnd}.51{danmuMsg}\n".format(resStart=resStart, resEnd=resEnd, danmuMsg=danmuMsg(msg))
	return False

def main(filelist, danmuFile, header):
	finishFile = False
	for key,value in enumerate(filelist):
		resDanmu = []
		for i in open(danmuFile, 'r'):
			if key+1 == len(filelist):
				#替换最后一个文件夹的分钟数+30,并且赋值到filelist中
				st1 = value.split('.')[0].split('_')
				sTime = '_'.join(st1[1:])
				nTime = datetime.datetime.strptime(sTime,"%Y_%m_%d_%H_%M")
				finishFile = st1[0]+'_'+(nTime + datetime.timedelta(minutes=30)).strftime("%Y_%m_%d_%H_%M")+'.mp4'

			if not finishFile:
				tmp = getVideoDanmu(i, value, filelist[key+1])
			else:
				tmp = getVideoDanmu(i, value, finishFile)
			if tmp:
				resDanmu.append(tmp)

		with open(value.split('.')[0]+'.ass', 'w') as f:
			f.write(header+"\n")
			f.writelines(resDanmu)


if __name__ == '__main__':
	#text = "[2019-02-23 00:12:43] [lv23 超超超超级背锅侠]:谢谢大家的支持。"
	#startTime = '3022003_2019_02_22_23_52.mpeg'
	#endTime = '3022003_2019_02_23_00_22.mpeg'

	header = """
[Script Info]
Title: douyu ASS 弹幕转换
Original Script: 把获取到弹幕的TXT，转化为ASS文件
ScriptType: v4.00+
Collisions: Normal
PlayResX: 560
PlayResY: 420
Timer: 10.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Fix,Microsoft YaHei UI,15,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0
Style: R2L,Microsoft YaHei UI,15,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
	"""
	import os
	DIR = "./"
	danmuFile = str(conf.room_num)+'.txt'
	def compare(x, y):
		stat_x = os.stat(DIR + "/" + x)
		stat_y = os.stat(DIR + "/" + y)
		if stat_x.st_ctime > stat_y.st_ctime:
		    return 1
		elif stat_x.st_ctime < stat_y.st_ctime:
		    return -1
		else:
		    return 0
	 
	filelist = os.listdir(DIR)
	filelist.sort(compare)
	filelist = [file for file in filelist if os.path.splitext(file)[1] == '.mp4']
	main(filelist, danmuFile, header)
	#print getVideoDanmu(text, startTime, endTime)
