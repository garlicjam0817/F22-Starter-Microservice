import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        #usr = os.environ.get("DBUSER")
        #pw = os.environ.get("DBPW")
        #h = os.environ.get("DBHOST")

        #usr = "root"
        #pw = "jjwjjwjjw520"
        #h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user="root",
            password="jjwjjwjjw520",
            host="e61561.caummjdubjdy.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

