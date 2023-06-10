# MongoDBConnector
一种更简便直观的mongoDB食用方式

# 食用方式
1. 导入tool.route包
2. 自定义函数myConnect，并绑定装饰器route，通过装饰器的数据库/数据表操作后，在函数体内可对执行结果进行处理
3. 创建连接client，并传入myConnect

# 装饰器route的参数格式
**@route(url,operator,\*args,\*\*kwargs)**
1. url：字符串，“路径”参数，一般是"/数据库/数据表"、"/数据库"、"/"几种格式，表示指向的目标，其中，首尾的/并不是必需的
2. operator：字符串，“操作”参数，与MongoDB中的操作算子名称必须一致，否则将找不到对应函数
3. 其余参数：表示操作函数所需的参数，请参见MongoDB的函数说明

# 自定义函数的参数格式
自定义函数**myConnect(connector,lens,data)**

其中，仅第一个参数是必需的，类似于oop中的self参数

1. connector：传入MongoDB的连接器，一般通过MongoClient函数进行连接
2. lens：对于route装饰器的“路径”参数所指向的目标来说，lens是这个目标的类型（0=连接器本身，1=数据库database，2=数据表colletions）
3. data：如果在route装饰器中传入了“操作”参数，那么此处将返回对应的操作结果，否则将返回errorFlag的内容（默认是["无操作"]）

创建连接时需要调用myConnect，但是只需要传入connector，即上文提到的client，如果需要自定义errorFlag，也可以再继续传入errorFlag的指定值
