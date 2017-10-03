#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 隐患：我使用id这个自增字段作为每一条数据的“把手”，但所这样带来了两个隐患。一是数据量巨大时，id的值会溢出；
#      二是随着数据的动态变化（有的条目会被删除），会有空缺的id值出现，且不会被填补，这实际上加剧了隐患一的到来。
from pymysql import *
from random import randint


def getOneProxy(ids):
    """从数据库拿取代理"""
    try:
        conn = connect(
            host='localhost',  # 记得修改数据库的地址
            port=3306,
            database='proxypool',
            user='root',
            password='mysql',
            charset='utf8',
        )
        cs = conn.cursor()
        # count = cs.execute('select id,protocol,host from proxies limit 5')
        count = cs.execute('select id,protocol,host from proxies WHERE id=%s' % ids)
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
    ids = randint(1, 1640)  # 当时数据库里有1640条http代理
    proxy = getOneProxy(ids)
    return proxy


if __name__ == "__main__":
    print(getARanProxy())
