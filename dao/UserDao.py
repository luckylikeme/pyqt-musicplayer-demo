from pymysql import IntegrityError

import pojo
import pymysql

from util.DBConnection import DbConnection


def GetUserDao():
    return UserDao()


class UserDao(object):

    # 按照account与password搜索
    def select_one(self, account, password):
        conn = DbConnection().get_connection()
        curs = conn.cursor()
        sql = 'select * from users where account=%s and user_password = %s'

        curs.execute(sql, (account, password))
        row_count = curs.fetchone()
        conn.close()
        curs.close()
        return row_count

    def insert_one(self, account, password):
        conn = DbConnection().get_connection()
        curs = conn.cursor()
        sql = "insert into users(account,nick_name,sex,user_password,auth) values (%s,%s,%s,%s,%s)"
        try:
            row_count = curs.execute(sql, (account, 'user_12', '男', password, '0'))
        except IntegrityError:
            print("唯一键冲突")
            row_count = 0
        finally:
            conn.commit()
            conn.close()
            curs.close()
        return row_count


if __name__ == '__main__':
    pass
