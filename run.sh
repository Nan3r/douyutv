#!/bin/bash
DATE=$(date +%m%d_%H%M)

ps aux|grep pccold.py|awk '{print $2}'|xargs kill -9
ps aux|grep danmu.py|awk '{print $2}'|xargs kill -9
ps aux|grep streamlink|awk '{print $2}'|xargs kill -9
ps aux|grep bypy|awk '{print $2}'|xargs kill -9


rm nohup.out
rm coldlog.log

nohup python3 pccold.py &
nohup python douyu.py >/dev/null 2>&1 &
