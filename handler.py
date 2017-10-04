#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 隐患：我使用id这个自增字段作为每一条数据的“把手”，但所这样带来了两个隐患。一是数据量巨大时，id的值会溢出；
#      二是随着数据的动态变化（有的条目会被删除），会有空缺的id值出现，且不会被填补，这实际上加剧了隐患一的到来。
# 或者，可以删掉id这个字段，但是就怕删掉以后，直接靠host删除一条数据的时候又浪费时间在查询上。
from pymysql import *
from random import randint


def getOneProxy():
    """从数据库拿取代理"""
    conn = None
    try:
        conn = connect(
            host='192.168.0.100',  # 记得修改数据库的地址
            port=3306,
            database='proxypool',
            user='root',
            password='mysql',
            charset='utf8',
        )
        cs = conn.cursor()
        # count = cs.execute('select id,protocol,host from proxies limit 5')
        count = cs.execute('select id,protocol,host from proxies ORDER BY rand() LIMIT 1;')
        result = cs.fetchone()
        # results = cs.fetchall()  # 其实是跟fetchone互斥的
        # print(count)
        # print(result)
        # print(results)
        cs.close()
    except Exception as e:
        print(e)
        result = None
    finally:
        conn.close()
    return result


if __name__ == "__main__":
    print(getOneProxy())
