import sqlite3

# Create table for database
class Database():

    def __init__(self,db):
        # Connect
        self.conn=sqlite3.connect(db)
        # Cursor
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        # Commit changes
        self.conn.commit()


    # Insert Items
    def insert(self,title, author, year, isbn):
        # SQL
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        # Commit changes
        self.conn.commit()


    # View rows
    def view(self):
        # Cursor
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    # Search rows (Empty strings for null values)
    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    # View rows
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title, author, year, isbn,id))
        self.conn.commit()

    def __del__(self): #Closes connection in the class
        self.conn.close()
