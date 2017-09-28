#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pymysql import *
from random import randint

def getOneProxy(ids):
    """从数据库拿取代理"""
    try:
        conn = connect(
            host='localhost',
            port=3306,
            database='proxypool',
            user='root',
            password='mysql',
            charset='utf8',
        )
        cs = conn.cursor()
        # count = cs.execute('select id,protocol,host from proxies limit 5')
        count = cs.execute('select id,protocol,host from proxies WHERE id=%s' %ids)
        result = cs.fetchone()
        # results = cs.fetchall()  # 其实是跟fetchone互斥的
        # print(count)
        # print(result)
        # print(results)
        cs.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return result[2]


def getARanProxy():
    ids = randint(1,1640)  # 当时数据库里有1640条http代理
    proxy = getOneProxy(ids)
    return proxy

if __name__ == "__main__":
    print(getARanProxy())
