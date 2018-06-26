#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

import requests
import json
import time


def call_ding_robot(at_all, msg):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
          '2b23a10fe566def473ea1b11960c80cb2e47fd3d3f456adf280d529cb4b62837'

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": msg,
        },
        "at": {
            "atMobiles": [],
            "isAtAll": at_all,
        }
    }

    result = requests.post(
        url,
        data=json.dumps(data),
        headers=headers)

    return result


def get_current_datetime():
    now = time.strftime('%Y年%m月%d日-%H时%M分%S秒',
                        time.localtime(time.time()))
    return str(now)
