# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import template
import basic
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "1qaz2wsxE" 

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            if isinstance(recMsg, receive.EventMsg):
                print("event")
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpGuide':
                        toUser = recMsg.FromUserName
                        data = """
                        {
                            "touser":"%s",
                            "template_id":"GVnSlVUMHDAr6uNtd7dJhnUr_Y0qEopR7SGwzyGVpto",
                            "url":"http://www.mej.cn",         
                            "data":{
                            }
                        }
                        """ % toUser
                        token = basic.Basic().get_access_token()
                        reply_template = template.Template().send(data, token)
                        return data
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            print(Argment)
            return Argment