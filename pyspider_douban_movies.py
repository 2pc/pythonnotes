#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-09-19 11:04:50
# Project: donbanjs

from pyspider.libs.base_handler import *

import sys
import pymysql
reload(sys)
#asii 乱码问题
sys.setdefaultencoding('utf-8')


class MysqlStore(object):
    
    def insert(self,result):
        if result:
            db = pymysql.connect(host='172.28.3.159', port=3306,
user='canal', passwd='canal', db='pyspider', charset='utf8')
            cursor = db.cursor()
            sql = "INSERT INTO movies(url,title,score,commenter_counts,tags,actors,related_info,img) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                print sql
                print result
                cursor.executemany(sql,result)
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                print 'error'
                print e
                db.rollback()
            # 关闭游标
            finally:
                cursor.close()
                # 关闭数据库连接
                db.close()
    


class Handler(BaseHandler):
    crawl_config = {
    }
    
    
    headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331',
    'Referer': 'https://movie.douban.com',
    'Connection': 'keep-alive'
    }

    def __init__(self):
            self.mysqlStore=MysqlStore()


            
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://movie.douban.com/tag/#/', callback=self.index_page,headers=self.headers,timeout=180,fetch_type='js',js_script='''
            function(){
                window.scrollTo(0,document.body.scrollHeight);
            }
            ''')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        print 'aaaaa'
        for each in response.doc('li > span').items():
            print each
            if '全部' not in each.text():
                for i in range(50):
                    tag='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags='+each.text()+'&start='+str(20*i)
                    self.crawl(tag, callback=self.list_page,headers=self.headers,timeout=180)
    def list_page(self, response):
        for i  in range(20):
            List=response.json['data'][i]['url']
            self.crawl(List,callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        
        print '###### ' +response.url
        url = response.url
        title = response.doc('h1 > span').text()
        score = response.doc('.rating_num').text()
        commenter_counts = response.doc('.rating_sum span').text(),
        tags = response.doc('.tags-body > a').text()
        actors = response.doc('.actor a').text()
        related_info = response.doc('.related-info > .indent').text()
        img = response.doc('#mainpic img').attr('src')
        '''
        return {
            "url": response.url,
            "title": response.doc('h1 > span').text(),
            "score":response.doc('.rating_num').text(),
            "commenter_counts":response.doc('.rating_sum span').text(),
            "tags":response.doc('.tags-body > a').text(),
            "actors":response.doc('.actor a').text(),
            "related_info":response.doc('.related-info > .indent').text(),
            "img":response.doc('#mainpic img').attr('src')
        }
        '''
        return [(url,title,score,commenter_counts,tags,actors,related_info,img)]

    def on_result(self,result):
        print result
        self.mysqlStore.insert(result)
           #super(Handler,self).on_result(result)
