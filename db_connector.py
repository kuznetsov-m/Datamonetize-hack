import os
import sqlite3

class DbConnector():
    def __init__(self, path: str, db_name: str):
        self._db_name = f'{path}/{db_name}' if path else db_name
        
        self._recipts_table = 'recipts'
        self._recipts_table_row_names = ['title', 'products', 'text']

    def create_db(self, shuld_rewrite_file=False):
        if os.path.isfile(self._db_name) and shuld_rewrite_file == True:
            try:
                os.remove(self._db_name)
            except Exception as e:
                print('ERROR: ' + str(e))

        if not os.path.isfile(self._db_name):
            try:
                f = open(self._db_name, 'w+')
            except IOError:
                print('ERROR: db not created')
            finally:
                f.close()

        self._create_table(self._recipts_table, self._recipts_table_row_names)

    def _create_table(self, name: str, rows: str):
        with sqlite3.connect(self._db_name) as connection:
            c = connection.cursor()
            
            sql = '''CREATE TABLE IF NOT EXISTS %s''' \
                  '''(id INTEGER PRIMARY KEY''' % (name)
                
            for item in rows:
                sql += ', %s TEXT' % (item)
            sql += ');'

            c.execute(sql)
            print('INFO:' + str(c.fetchall()))
            
            connection.commit()

    def create_recipt(self, title: str, products: list, text: str):
        if not title or not products or not text:
            print('ERROR: incorrect parameters')
            return

        with sqlite3.connect(self._db_name) as connection:
            c = connection.cursor()

            sql = f'''INSERT INTO {self._recipts_table}
                        (title, products, text)
                        VALUES(?, ?, ?)'''
            products_str = ','.join(products)
            values = [title, products_str, text]
            c.execute(sql, values)
            print('INFO:' + str(c.fetchall()))
            
            connection.commit()

    def get_recipts_by_products_list(self, products: list):
        if not products:
            print('ERROR: incorrect parameters')
            return

        with sqlite3.connect(self._db_name) as connection:
            c = connection.cursor()
            
            sql = f'''SELECT * FROM {self._recipts_table}
                        WHERE products LIKE ?'''

            for product in products[1:]:
                sql += ' AND products LIKE ?'

            new_products = []
            for product in products:
                new_products.append(f'%{product}%')
            
            c.execute(sql, new_products)
            recipts = [dict(id=row[0], title=row[1], products=row[2], \
                            text=row[3]) for row in c.fetchall()]

            return recipts

    def get_recipts_count(self):
        with sqlite3.connect(self._db_name) as connection:
            c = connection.cursor()
            
            sql = f'''SELECT COUNT(*) FROM {self._recipts_table}'''
            
            c.execute(sql)
            count = int([row[0] for row in c.fetchall()][0])

            return count

    def get_recipt_by_id(self, id: int):
        if not id:
            print('ERROR: incorrect parameters')
            return

        with sqlite3.connect(self._db_name) as connection:
            c = connection.cursor()
            
            sql = f'''SELECT * FROM {self._recipts_table}
                        WHERE id = ?'''
            
            c.execute(sql, [id])
            recipt = [dict(id=row[0], title=row[1], products=row[2], \
                            text=row[3]) for row in c.fetchall()][0]

            return recipt