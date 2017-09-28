#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib


def host_abstarct(host):
    """md5指纹"""
    md5 = hashlib.md5()
    md5.update(host.encode())
    return md5.hexdigest()


class Xici(object):
    """西刺网免费代理"""
    def __init__(self):
        self.start_url = 'http://www.xicidaili.com/nn'

    def onePageContent(self, html):
        """
        每一页的解析
        :param html: 页面的etree对象
        :return: list，包含一页的代理ip：port信息
        """
        page = 1
        content = []
        if len(html) != 0:
            div_list = html.xpath('//*[@id="ip_list"]/tr')[1:]
            for line in div_list:
                temp = line.xpath('./td/text()')
                protol = temp[5].lower()
                host = temp[0] + ':' + temp[1]
                distin = host_abstarct(host)
                con = {'pro':protol, 'host': host, 'md5': distin}
                print(con)
                content.append(con)
        return content

    def next_page(self, pageNum):
        return self.start_url + '/' + str(pageNum)


class Nianshao(object):
    def __init__(self):
        self.start_url = 'http://www.nianshao.me/?stype=1'

    def onePageContent(self, html):
        """

        :param html: 
        :return: 
        """
        page = 1
        content = []
        if len(html) != 0:
            div_list = html.xpath('//*[@id="main"]/div/div/table/tbody/tr')
            for lan in div_list:
                temp = lan.xpath('./td/text()')
                host = temp[0] + ':' + temp[1]
                distin = host_abstarct(host)
                con = {'pro': 'http', 'host': host, 'md5': distin}
                print(con)
                content.append(con)
        return content

    def next_page(self, pageNum):
        return self.start_url + '&page=' + str(pageNum)


if __name__ == "__main__":
    pass