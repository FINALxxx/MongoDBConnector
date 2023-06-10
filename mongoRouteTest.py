from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#1.导入装饰器
from tools.route import route

#2.自定义函数，并绑定装饰器route


@route("database_sandbox","list_collection_names")#参数内容：路径，操作的函数名，函数所需的参数
def myDatabase(connector,lens,data):#参数内容：连接器，路径指向的目标类型，操作返回的结果
    #a. 可以判断路径指向的目标类型
    if(lens==0): print("路径指向了连接器本身")
    if(lens==1): print("路径指向了database")
    if(lens==2): print("路径指向了collection")

    #b. 可以返回装饰器中执行完的操作结果
    print("数据库database_sandbox中的所有数据表如下：")
    for i in data:
        print(i)


doc_filter={"sex":"男"}
doc_display={"_id":0}
@route("database_sandbox/collection_sandbox","find",doc_filter,doc_display)
def myCollection(connector, lens, data):
    if (lens == 0): print("路径指向了连接器本身")
    if (lens == 1): print("路径指向了database")
    if (lens == 2): print("路径指向了collection")

    print("数据表collection_sandbox中过滤后的记录如下：")
    for i in data:
        print(i)




#3.创建连接，并传入参数
if __name__=='__main__':
    uri = "<连接到对应的Mongo数据库>"
    client = MongoClient(uri, server_api=ServerApi('1'))

    myDatabase(client)#只用传入一个参数（连接器）就行，不用传lens和data
    print("==============================")
    myCollection(client)
