"""
todo:封装一个database链接，并将这个连接返回
作用：将python与数据库进行连接，并返回可操作的连接
"""
import pymysql
import json

class DbConnection:
    def __init__(self, host='localhost', user='root', password='mysql', db='mysql'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def get_connection(self):
        # 获取配置信息
        data = self.get_configuration()
        # print(data)
        connection = pymysql.connect(host=data['host'], user=data['user'], password=data['password'], db=data['db'])
        return connection

    def get_configuration(self):
        # 读取json文件，获取相关配置
        with open("G:/pt_test/musicPlayer/util/Configuration.json", "r") as fp:
            data = json.load(fp)
            data = data['database']
        return data


if __name__ == '__main__':
    obj_1 = DbConnection()
    connection = obj_1.get_connection()
    sql ='select * from users '
    cur = connection.cursor()
    cur.execute('use  music_player')
    cur.execute(sql)
    print(cur.fetchone())
    connection.close()
    cur.close()



