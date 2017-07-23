# coding=UTF-8
import sqlite3

class Layout_Shape:
	def __init__(self):
		self.uid = -1
		self.shape = ''
		self.layout_name = ''
		self.remark = ''

class Layout_Env:
	def __init__(self):
		self.uid = -1
		self.center_shape = ''
		self.other_shape = ''
		self.zone = ''
		self.distance = 0.0
		self.layout_name = ''
		self.remark = ''

class Layout_Net:
	def __init__(self):
		self.uid = -1
		self.start_shape = ''
		self.net_shape = ''
		self.layout_name = ''
		self.remark = ''

def is_table_exist(pDatabase, pTable):
	"check if table exist"
	conn = sqlite3.connect(pDatabase)
	cursor = conn.execute("SELECT name FROM sqlite_master WHERE type=? AND name=?", ('table',pTable))
	is_table_exist = cursor.fetchone()
	return is_table_exist

def prepare_table():
	"create database tables"
	database_name = 'layout.sqlite3'
	conn = sqlite3.connect(database_name)
	cursor = conn.cursor()

	if is_table_exist(database_name, 'Layout_Shape') == None:
	    cursor.execute('CREATE TABLE Layout_Shape (uid integer AUTOINCREMENT, shape text, layout_name text, remark text)')
	    conn.commit()


	if is_table_exist(database_name, 'Layout_Env') == None:
	    cursor.execute('CREATE TABLE Layout_Env (uid integer AUTOINCREMENT, center_shape text, other_shape text, zone text, distance real, layout_name text, remark text)')
	    conn.commit()

	if is_table_exist(database_name, 'Layout_Net') == None:
	    cursor.execute('CREATE TABLE Layout_Net (uid integer AUTOINCREMENT, start_shape text, net_shape text, layout_name text, remark text)')
	    conn.commit()

if __name__ == '__main__':
	prepare_table()
