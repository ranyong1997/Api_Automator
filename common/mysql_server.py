import pymysql
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mysql"]

DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}


class MysqlDB():
    def __init__(self, db_conf=DB_CONF):
        # 通过字典解包传递配置信息，建立数据库链接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall()获取查询结果
        data = self.cur.fetchall()
        logger.info(data)
        return data

    def execute_db(self, sql):
        """增删改查"""
        try:
            # 检查连接是否断开，如果断开就重连
            self.conn.ping(reconnect=True)
            # 使用execute()执行sql
            self.cur.execute(sql)
            # 提交事务
            self.cur.execute(sql)
        except Exception as e:
            logger.info("操作MYSQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


if __name__ == '__main__':
    db = MysqlDB(DB_CONF)
    # db.select_db('SELECT * FROM sp_report_1 WHERE id')
