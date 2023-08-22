import pojo
import pymysql

from util.DBConnection import DbConnection


def GetUserDao():
    return UserDao()


class UserDao(object):

    # 按照account与password搜索
    def select_one(self, account,password):
        conn = DbConnection().get_connection()
        curs = conn.cursor()
        sql = 'select * from users where account=%s and user_password = %s'

        # account = args['account']
        # password = args['password']
        curs.execute(sql, (account, password))
        row_count = curs.fetchone()

        conn.close()
        curs.close()
        return row_count


if __name__ == '__main__':
    pass
