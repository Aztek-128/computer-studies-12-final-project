import sqlite3
import os
class main():
    def __init__(self):
        
        file = 'dbase2.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists funny (
            id integer primary key autoincrement,
            funny_points int);
        """
        self.cursor.execute(query)
        self.funnypoint = 0
        query = f"insert into funny (funny_points) values ('{self.funnypoint}')"
        self.cursor.execute(query)
        if os.path.exists('dbase2.db'):
            query = "select * from funny where id=1"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            x = result[0]
            self.p_funnypoint = x[1]
            
        else:
            file = 'dbase2.db'
            self.connection = sqlite3.connect(file)
            self.cursor = self.connection.cursor()
            query = """
            create table if not exists funny (
                id integer primary key autoincrement,
                funny_points int,
                );
            """
            self.cursor.execute(query)

    def main(self):
        x = input("how many points do you want")
        self.funnypoint += x
        query = f"update funny set (funny_points) = ('{self.funnypoint}') where id=1"
        self.cursor.execute(query)
        query = "select * from funny"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result) #this is a tuple in a list #a list of things in a list
        x = result[0] #retrieving from the first tuple
        print(x[1])
main()