# coding: utf-8
from douyu.chat.room import ChatRoom
import time,os
import sys,conf

f = open(str(conf.room_num)+'.txt','a+')
def on_chat_message(msg):
	os.environ['TZ']='Asia/Shanghai'
	#time.tzset()
	msg_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	user = msg.attr('nn')
	txt = msg.attr('txt')
	level = msg.attr('level')
	d = "[%s] [lv%s %s]:%s\n" % (msg_time,level,user,txt)
	f.write(d)

def run():
	room = ChatRoom(str(conf.room_num))
	room.on('chatmsg', on_chat_message)
	room.knock()

if __name__ == '__main__':
	run()
