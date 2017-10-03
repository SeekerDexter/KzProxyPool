#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from retrying import retry
import pymysql
from handler import getARanProxy


class HtmlCatcher(object):
    """暂时是使用http代理去获取https代理"""
    def __init__(self, special):
        self.loading = special
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
        }

    def get_a_proxy(self):
        return getARanProxy()

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        print('now parsing:', url)
        # proxy = self.getAProxy()
        # response = requests.get(url, headers=self.headers, proxy=proxy, timeout=5)
        response = requests.get(url, headers=self.headers, timeout=5)
        assert response.status_code == 200
        # print(response.content)
        return etree.HTML(response.content)

    def parse_url(self, url):
        try:
            html = self._parse_url(url)
        except Exception as e:
            print(e)
            html = ''
        return html

    def save_data(self, content):
        try:
            conn = pymysql.connect(host='localhost', port=3306, database='proxyPool', user='root', password='mysql',
                           charset='utf8')
            cur = conn.cursor()
            for li in content:
                params = [li['pro'], li['host'], li['md5']]
                count = cur.execute('INSERT INTO proxies(protocol, host,md5) VALUES (%s,%s,%s);', params)
            cur.close()
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def run(self):
        """ """
        page = 2
        next_url = self.loading.start_url
        while page is not None:
            html = self.parse_url(next_url)
            if len(html) != 0:
                next_url = self.loading.next_page(page)
                page += 1
                self.save_data(self.loading.onePageContent(html))
                # print(self.loading.onePageContent(html))
            else:
                break


if __name__ == "__main__":
    # 注意，测试时切换注释run方法里的输出方式
    # from sitebullets import Xici
    # htmlCatcher(Xici()).run()
    pass
    # from sitebullets import Nianshao
    # htmlCatcher(Nianshao()).run()
