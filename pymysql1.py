import pymysql

conn = pymysql.connect(
    host='192.168.88.100',
    port=3306,
    user='root',
    passwd='123456',
    database='jingdong',
    charset='utf8'
)

# 3. 创建游标对象
cursor = conn.cursor()

# 根据用户输入的商品的名称，查询对应的商品的数据。
# 输入的时候 输入 " or 1=1 or "
g_name = input('请输入要查询的商品名称：')
data_list = [g_name]
print(data_list)
# 想要去解决sql注入的问题，将数据进行参数化。放到列表中中。
sql_str = 'select * from goods where name=%s;'
sql_str1 = 'alter table jingdong.goods add constraint good_bfr foreign key (brand_id) references goods_brands(id);'

print(sql_str)
# 执行查询的sql语句 将构造好的参数的列表 传个 execute方法。

cursor.execute(sql_str, data_list)

# 获取一下查询的结果：
result = cursor.fetchall()
print(f'获取到的查询结果为： {result}')

# 4. 关闭
# cursor.close()
# conn.close()
