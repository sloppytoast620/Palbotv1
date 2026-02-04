
import sqlite3, time
DB="palbot.db"
def init_db():
    con=sqlite3.connect(DB)
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, coins INTEGER, last_catch INTEGER, last_daily INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS pals(id INTEGER PRIMARY KEY AUTOINCREMENT, user INTEGER, name TEXT)")
    con.commit(); con.close()
def ensure(uid):
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("INSERT OR IGNORE INTO users VALUES(?,?,?,?)",(uid,0,0,0))
    con.commit(); con.close()
def add_pal(uid,name):
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("INSERT INTO pals(user,name) VALUES(?,?)",(uid,name))
    con.commit(); con.close()
def get_pals(uid):
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("SELECT name FROM pals WHERE user=?",(uid,))
    r=cur.fetchall(); con.close(); return r
def get_user(uid):
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("SELECT coins,last_catch,last_daily FROM users WHERE id=?",(uid,))
    r=cur.fetchone(); con.close(); return r
def update(uid,coins=None,last_catch=None,last_daily=None):
    con=sqlite3.connect(DB); cur=con.cursor()
    if coins is not None: cur.execute("UPDATE users SET coins=? WHERE id=?",(coins,uid))
    if last_catch is not None: cur.execute("UPDATE users SET last_catch=? WHERE id=?",(last_catch,uid))
    if last_daily is not None: cur.execute("UPDATE users SET last_daily=? WHERE id=?",(last_daily,uid))
    con.commit(); con.close()
