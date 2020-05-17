"""
测试项目：
创建100万个随机数，并生成插入这些随机数的SQL语句。
连接本地数据库，如不成功，尝试创建数据库。
删除并创建数据库表，引擎类型为InnoDB，主键为自动递增的整数，此外有个浮点型的字段（无索引）。
分成100组，每次插入1万个随机数。（因为每组的执行量都很大，因此启用自动提交事务。）
用SELECT COUNT(*)统计小于0.1的随机数个数。（约10万个）
用SELECT *取出再统计大于0.9的随机数个数。（约10万个）
将所有0.4～0.5之间的随机数加1。（约10万个）
将所有0.5～0.6之间的行删除。（约20万个）
断开数据库连接。
再次连接数据库。
"""
import MySQLdb
from random import random
from time import perf_counter

SIZE1 = 10000
SIZE2 = 100
DB_ENGINE = 'InnoDB' # InnoDB Memory MyISAM
print('测试数据量：', SIZE1 * SIZE2)
print('测试引擎：', DB_ENGINE)

t1 = perf_counter()

sqls = ['INSERT INTO test (value) VALUES (%s)' % '),('.join([repr(random()) for i in range(SIZE1)]) for j in range(SIZE2)]
t2 = perf_counter()

try:
  con = MySQLdb.connect(host="localhost", user='root', passwd='landy8530', database='test')
  t3 = perf_counter()
  cu = con.cursor()
except:
  con = MySQLdb.connect(host="localhost", user='root', passwd='landy8530')
  t3 = perf_counter()
  cu = con.cursor()
  cu.execute('CREATE DATABASE test')
  con.select_db('test')

con.autocommit(True)

try:
  cu.execute('DROP TABLE test')
except:
  pass
cu.execute('''CREATE TABLE test (
`id` INT AUTO_INCREMENT PRIMARY KEY,
`value` REAL)
ENGINE = %s''' % DB_ENGINE)
t4 = perf_counter()

for sql in sqls:
  cu.execute(sql)
t5 = perf_counter()

cu.execute('SELECT COUNT(*) FROM test WHERE value < 0.1')
print( '共有%d个小于0.1的随机数' % cu.fetchone()[0])
t6 = perf_counter()

cu.execute('SELECT * FROM test WHERE value > 0.9')
print( '共有%d个大于0.9的随机数' % len(cu.fetchall()))
t7 = perf_counter()

cu.execute('UPDATE test SET value = value + 0.1 WHERE value > 0.4 AND value < 0.5')
t8 = perf_counter()

cu.execute('DELETE FROM test WHERE value > 0.5 AND value < 0.6')
t9 = perf_counter()

cu.close()
con.close()
t10 = perf_counter()

con = MySQLdb.connect(host="localhost", user='root', passwd='landy8530', database='test')
t11 = perf_counter()
con.close()

print('创建随机数：', t2 - t1)
print( '初次连接数据库：', t3 - t2)
print( '再次连接数据库：', t11 - t10)
print( '初始化数据库：', t4 - t3)
print( '插入：', t5 - t4)
print( '选择（COUNT）', t6 - t5)
print( '选择：', t7 - t6)
print( '更新：', t8 - t7)
print( '删除：', t9 - t8)
print( '关闭连接：', t10 - t9)
print( '总时间：', t10 - t1)
