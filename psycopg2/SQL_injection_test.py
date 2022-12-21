import psycopg2
from psycopg2 import sql

# Update connection string information
host = "localhost"
dbname = "1101_jingyou_1031_copy4"
user = "odoo"
password = "odoo"
#SSL 模式說明
sslmode = "allow"
port = "5432"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(host, user, dbname, password, sslmode, port)
conn = psycopg2.connect(conn_string)
print("Connection established")
cur = conn.cursor()

# --------------------------------------------------

# your_input = "流動性轉移' or '1'= '1"
# your_input = "流動性轉移"

# SQL injection
# sql_string = "SELECT * FROM account_account WHERE name = '{your_input}' ".format(your_input=your_input)
# sql_string = f"SELECT * FROM account_account WHERE name = '{your_input}' "
# cur.execute(sql_string)
# --------------------------------------------------

# can't search for injection
# 方法 1
# sql_string = "SELECT * FROM account_account WHERE name = %s "
# cur.execute(sql_string, (your_input,))

# 方法2
# your_input = "流動性轉移' or '1'= '1"
# your_input = "流動性轉移"
# sql_string = sql.SQL(
#     "SELECT * FROM account_account WHERE {name123} = %s").format(
#         name123 = sql.Identifier('name'))
# cur.execute(sql_string,(your_input,))

records = cur.fetchall()
print(records)

