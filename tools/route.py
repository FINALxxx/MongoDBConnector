from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def route(url,operator='',*args,**kwargs):
    def outer(func):
        def inner(connector,errorFlag=["无操作"]):
            attr_list=url.split('/')
            if '' in attr_list:
                attr_list.remove('')

            # 0为连接器本身，1为database，2为collection
            lens=len(attr_list)
            #路由跳转
            for i in range(lens):
                connector=connector[attr_list[i]]

            #执行操作
            if operator!='':
                data=getattr(connector, operator)(*args,**kwargs)
                return func(connector, lens, data)

            #不执行操作
            return func(connector,lens,errorFlag)
        return inner
    return outer