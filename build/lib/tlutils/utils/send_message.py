#! /usr/bin/env python
# -*- coding:utf8 -*-
# __author__ : "ZhangTianliang"
# Date: 12/28/17

import requests


def send_message(message, title=None):
    """
     send_message(message, title=None)
    """
    text = {
        "source": "s-638d2dca-a286-455c-be25-4f9a07b5",
        "receiver": "u-38c794ad-be73-42ae-ad62-5e820ef9",
        "content": "init",
        "title": "hello",
    }
    if title is not None:
        text['title'] = title
    text['content'] = message
    requests.post(
        "https://api.alertover.com/v1/alert",
        data=text,
    )

if __name__ == '__main__':
    title = 'Done'
    message = '%d is done!' % 10
    send_message(message, title)
