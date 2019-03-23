# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json
import sqlite3
from sqlite3 import Error

class Basic:    
    def __init__(self):        
        self.__accessToken = ''        
        self.__leftTime = 0   
        self.__conn = DB.create_connection() 
    
    def __real_get_access_token(self):        
        appId = "wxfc1a67f2d7bccbc7"        
        appSecret = "fc4bfaf80bf1cb4cc64183420fc6359e"        
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))        
        urlResp = urllib.urlopen(postUrl)        
        urlResp = json.loads(urlResp.read())                
        self.__accessToken = urlResp['access_token']        
        self.__leftTime = urlResp['expires_in']    
        
    def get_access_token(self): 
        token = DB.get_token(self.__conn)     
        if token: 
            return token
        else:           
            self.__real_get_access_token()        
            return self.__accessToken    

    def run(self):        
        while(True):            
            if self.__leftTime > 10:                
                time.sleep(2)                
                self.__leftTime -= 2            
            else:                
                self.__real_get_access_token()        
    
class Token:
    def __init__(self):
        __db_file = '/root/tools/scripts/cary_tools_db'

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.__db_file)
            print("Successfully connected to the database")
            return conn
        except Error as e:
            print(e)
        return None

    def get_token():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("select * from token")
            print("token selected!")
            row = cur.fetchone()
            if row:
                print row
                return row
            else:
                return None

    def set_token(token):
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("invert into token('token') values(?)",(token))
            print("token set")

    def main():
        DB.set_token("test")
        token = DB.get_token()
        print token
    
if __name__ == '__main__':
    main()