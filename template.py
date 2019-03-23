# -*- coding: utf-8 -*-
# filename: template.py
import urllib

class Template(obejct):
    def __init__(self):
        pass

    def send(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()