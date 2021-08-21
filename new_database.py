import mysql.connector
import time
import atexit

class db:
    def __init__(self, category=""):
        self.category = category
        self.time = time.time()
        self.five_days = 60 * 60 * 24 * 5
        self.hour = 60 * 60
        self.db = mysql.connector.connect(host="localhost",
                                          user="user", #*
                                          password="password", #*
                                          )
        cursor = self.db.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS words")

        self.db = mysql.connector.connect(host="localhost",
                                          user="user", #*
                                          password="password", #*
                                          database="words",
                                          )
        self.cursor = self.db.cursor()
        # self.cursor.execute("DROP TABLE IF EXISTS {}".format(self.category))
        if self.category != "" :
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, en VARCHAR(64), repeat_count INT, rec_time VARCHAR(64))".format(
                    self.category))
        self.db.autocommit = True
        atexit.register(self.quit)

    def insert_to_db(self, en):
        insert_sql = "INSERT INTO {} (en, repeat_count, rec_time) VALUES (%s, %s, %s)".format(self.category)
        search_sql = "SELECT en FROM {} WHERE en = %s".format(self.category)
        update_sql = "UPDATE {} SET repeat_count = %s WHERE en = %s".format(self.category)
        self.cursor.execute(search_sql, (en,))
        if not self.cursor.fetchall():
            self.cursor.execute(insert_sql, (en, 1, 0))
        else:
            self.cursor.execute("SELECT repeat_count FROM {} WHERE en = %s".format(self.category), (en,))
            c = self.cursor.fetchone()[0] + 1
            self.cursor.execute(update_sql, (c, en))

    def quit(self):
        print("on quit")
        self.cursor.close()
        self.db.commit()
        self.db.close()

    def readDB(self, back, en):
        loc = True
        temp = [None]*4
        readsql = f"SELECT * FROM {self.category} ORDER BY repeat_count DESC"
        updatesql = f"UPDATE {self.category} SET rec_time =%s WHERE en=%s"

        self.cursor.execute(readsql)
        while True:
            data = self.cursor.fetchone()
            if data is None:
                return [None]*4

            if en is None:
                loc = False

            if loc:
                if en == data[1]:
                    loc = False
                    continue
                temp = data
                continue

            if back:
                if temp[0] is None:
                    self.cursor.fetchall()
                    return [None]*4
                elif abs(float(temp[3]) - self.time) < self.hour or abs(float(temp[3]) - self.time) > self.five_days:
                    self.cursor.fetchall()
                    return temp
                else:
                    self.cursor.fetchall()
                    self.cursor.execute(f"SELECT * FROM {self.category} WHERE en = %s", (en,))
                    data = self.cursor.fetchone()
                    return data

            if abs(float(data[3]) - self.time) < self.hour or abs(float(data[3]) - self.time) > self.five_days:
                if int(data[2]) < 2:
                    print("anlamlı olabilecek verilerin sonuna gelindi")
                    self.cursor.fetchall()
                    self.cursor.execute(f"SELECT * FROM {self.category} WHERE en = %s", (en,))
                    data = self.cursor.fetchone()
                    return data

                self.cursor.fetchall()
                self.cursor.execute(updatesql, (self.time, data[1]))
                return data

    def remove_from_db(self, en): #main screen dont save function
        data = self.readDB(True, en)
        self.cursor.execute(f"DELETE FROM {self.category} WHERE en = %s", (en,))
        self.cursor.reset()
        return data

    def table_list(self):
        self.cursor.execute("SHOW TABLES")
        x = self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return x