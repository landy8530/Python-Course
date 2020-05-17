# -*- coding: gbk -*-
# import _mysql
# from MySQLdb.converters import conversions
# from random import random
# from time import clock
#
# SIZE1 = 10000
# SIZE2 = 100
# DB_ENGINE = 'InnoDB' # InnoDB Memory MyISAM
# print('������������', SIZE1 * SIZE2)
# print('�������棺', DB_ENGINE)
#
# t1 = clock()
#
# sqls = ['INSERT INTO test (value) VALUES (%s)' % '),('.join([repr(random()) for i in range(SIZE1)]) for j in range(SIZE2)]
# t2 = clock()
#
# try:
#   con = _mysql.connect(host="localhost", user='root', passwd='landy8530', db='test', conv=conversions)
#   t3 = clock()
# except:
#   con = _mysql.connect(host="localhost", user='root', passwd='landy8530', db='test', conv=conversions)
#   t3 = clock()
#   con.query('CREATE DATABASE test')
#   con.select_db('test')
#
# con.autocommit(True)
#
# try:
#   con.query('DROP TABLE test')
# except:
#   pass
# con.query('''CREATE TABLE test (
# `id` INT AUTO_INCREMENT PRIMARY KEY,
# `value` REAL)
# ENGINE = %s''' % DB_ENGINE)
# t4 = clock()
#
# for sql in sqls:
#   con.query(sql)
# t5 = clock()
#
# con.query('SELECT COUNT(*) FROM test WHERE value < 0.1')
# print('����%d��С��0.1�������' % con.store_result().fetch_row()[0])
# t6 = clock()
#
# con.query('SELECT * FROM test WHERE value > 0.9')
# print('����%d������0.9�������' % con.store_result().num_rows())
# t7 = clock()
#
# con.query('UPDATE test SET value = value + 0.1 WHERE value > 0.4 AND value < 0.5')
# t8 = clock()
#
# con.query('DELETE FROM test WHERE value > 0.5 AND value < 0.6')
# t9 = clock()
#
# con.close()
# t10 = clock()
#
# con = _mysql.connect(host="localhost", user='root', passwd='landy8530', db='test', conv=conversions)
# t11 = clock()
# con.close()
#
# print('�����������', t2 - t1)
# print( '�����������ݿ⣺', t3 - t2)
# print( '�ٴ��������ݿ⣺', t11 - t10)
# print( '��ʼ�����ݿ⣺', t4 - t3)
# print( '���룺', t5 - t4)
# print( 'ѡ��COUNT��', t6 - t5)
# print( 'ѡ��', t7 - t6)
# print( '���£�', t8 - t7)
# print( 'ɾ����', t9 - t8)
# print( '�ر����ӣ�', t10 - t9)
# print( '��ʱ�䣺', t10 - t1)