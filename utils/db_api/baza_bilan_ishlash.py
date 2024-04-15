import sqlite3

class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str, parametrs: tuple = None, fetchone=False,fetchall=False,commit=False):
        if not parametrs:
            parametrs = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parametrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql,parameters: dict):
        sql += " AND ".join([
            f"{item} = ?"for item in parameters
        ])
        return sql,tuple(parameters.values())

    def add_user(self,id: int,name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfolder_users(id, Name, email,language) VALUES(?,?,?)
        """
        self.execute(sql,parametrs=(id, name,email,language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfolder_users
        """
        return self.execute(sql,fetchall=True)
    def select_user(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id=1 And Name='John'"
        sql = "SELECT * FROM myfolder_users WHERE "
        sql, parameters = self.format_args(sql,kwargs)

        return self.execute(sql,parametrs=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfolder_users;",fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM myfolder_users WHERE TRUE", commit=True)

    def user_qoshish(self,ism: str,tg_id: int, fam: str = None, ):

         sql = """
         INSERT INTO myfolder_users(ism,fam,tg_id) VALUES(?,?,?)
         """
         self.execute(sql,parametrs=(ism,fam,tg_id),commit=True)

    def select_all_turlar(self):
        sql = """
            SELECT * FROM myfolder_turlar
            """
        return self.execute(sql, fetchall=True)

    def select_tur(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id=1 And Name='John'"
        sql = "SELECT * FROM myfolder_turlar WHERE "
        sql, parameters = self.format_args(sql,kwargs)

        return self.execute(sql,parametrs=parameters, fetchall=True)

    def select_all_maxsulotlar(self):
        sql = """
            SELECT * FROM myfolder_maxsulot
            """
        return self.execute(sql, fetchall=True)

    def select_maxsulotlar(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id=1 And Name='John'"
        sql = "SELECT * FROM myfolder_maxsulot WHERE "
        sql, parameters = self.format_args(sql,kwargs)

        return self.execute(sql,parametrs=parameters, fetchall=True)

    def select_maxsulot(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id=1 And Name='John'"
        sql = "SELECT * FROM myfolder_maxsulot WHERE "
        sql, parameters = self.format_args(sql,kwargs)

        return self.execute(sql,parametrs=parameters, fetchone=True)

# Buy
    def buy_product(self,product_id: int,tg_id: int,date:str,status:bool=False,number:int=1 ):
         sql = """
         INSERT INTO myfolder_savdo(product_id, tg_id, number, status, date) VALUES(?,?,?,?,?)
         """
         self.execute(sql,parametrs=(product_id,tg_id,number,status,date),commit=True)

    def update_trade_number(self, number,tg_id,product_id):
        sql = f"""
            UPDATE myfolder_savdo SET number=? WHERE tg_id=? And  product_id=?
            """
        return self.execute(sql,parametrs=(number,tg_id,product_id),commit=True)

    def select_trade(self,**kwargs):
        sql = "SELECT * FROM myfolder_savdo WHERE "
        sql, parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parametrs=parameters, fetchone=True)



def logger(statement):
    print(f"""
    ----------------------------------------------
    Executing:
    {statement}
    ----------------------------------------------
""")