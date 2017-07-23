# coding=UTF-8
import sqlite3

class Layout_Env:
	def __init__(self):
		self.uid = ''
		self.center_shape = ''
		self.other_shape = ''
		self.zone = ''
		self.distance = 0.0
		self.remark = ''

class Layout_Net:
	def __init__(self):
		self.uid = ''
		self.start_shape = ''
		self.net_shape = ''
		self.remark = ''

def is_table_exist(pDatabase, pTable):
	"check if table exist"
	conn = sqlite3.connect(pDatabase)
	cursor = conn.execute("SELECT name FROM sqlite_master WHERE type=? AND name=?", ('table',pTable))
	is_table_exist = cursor.fetchone()
	return is_table_exist

def prepare_table():
	"create database tables"
	database_name = 'stock.sqlite3'
	conn = sqlite3.connect(database_name)
	cursor = conn.cursor()

	if is_table_exist(database_name, 'Layout_Env') == None:
	    cursor.execute('CREATE TABLE Layout_Env (uid text, center_shape text, other_shape text, zone text, distance real, remark text)')
	    conn.commit()

	if is_table_exist(database_name, 'Layout_Net') == None:
	    cursor.execute('CREATE TABLE Layout_Net (uid text, start_shape text, net_shape text, remark text)')
	    conn.commit()

if __name__ == '__main__':
	prepare_table()
