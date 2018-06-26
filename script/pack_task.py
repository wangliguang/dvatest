#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

import os
import sys
import datetime
from threading import Timer


def pack_task(command, hour, minute):
    now = datetime.datetime.now()
    print str(now.hour) + ' h ' + str(now.minute) + ' m ' + str(now.second)
    if str(now.hour) == str(hour) and str(now.minute) == str(minute):
        print "定时任务启动"
        os.system(command)

    def next_task():
        pack_task(command, hour, minute)

    t = Timer(60, next_task)
    t.start()


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print """
        Please input platform (android/ios) as first argument!
        Please input task execute time (hour) as second argument!
        Please input task execute time (minute) as second argument!
        """
        exit()

    command = sys.argv[1]
    hour = sys.argv[2]
    minute = sys.argv[3]

    pack_task(command, hour, minute)
