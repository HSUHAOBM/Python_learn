psql -U odoo -h 127.0.0.1 -d 0217_wantang
psql -U postgres -h db -d postgres
# user enter
psql -U user

# create & drop
CREATE DATABASE DBNAME;
DROP DATABASE DBNAME;

# 切換db
\connect DBNAME
\c DBNAME


# 垂直表單方式顯示
\x

# all roles
\du

# all DATABASE
\l

# table column
\d table

# all tables
\z


# 設定環境變數
\set foo bar # 將 foo 設為 bar
\echo :foo   # 取得 foo 的變數值

# 變數名稱 DBNAME, ENCODING, HOST, PORT, USER
$ \echo :DBNAME

# 備份 test db 輸出 test-db-20121218.backup.sql
pg_dump test -U odoo -f test-db-20121218.backup.sql
pg_dump -U odoo -d test > dump.sql


# 使用 test-db-20121218.backup.sql 會附到test2 db
psql -f test-db-20121218.backup.sql test2 odoo
psql -U username -d dbname < dump.sql

# .bat
SET PGPASSWORD=database_password
pg_dump -U odoo -s -f kals-db-20141107-schema.backup.sql kals

# table create
create table posts (title varchar(255), content text);


# use db.sql set init DATABASE
# db.sql
'''
create table posts (title varchar(255), content text);
'''
# in database
\i db.sql


# column type
# 數值
'''
integer smallint bigint real serial
char varchar test
boolean
date time timestamp
array inet
json
xml
https://www.postgresql.org/docs/13/datatype.html
'''

# 約束
'''
not null
unique
check
default
primary key (not null, unique)
'''
ex
'''
create table posts (
    id serial primary key,
    title varchar(255) not null,
    content text check (length(content) > 3),
    is_draft boolean default TRUE,
    is_del boolean default FALSE,
    create_date timestamp default current_timestamp
);
'''
# 表單修改
# + -  欄位
ALTER TABLE posts ADD COLUMN active boolean;
ALTER TABLE posts DROP COLUMN active;
# 欄位名稱
ALTER TABLE posts RENAME COLUMN title TO link_title;
# + 欄位 默認 約束
ALTER TABLE link ALTER COLUMN target SET DEFAULT '_blank';
ALTER TABLE link ADD CHECK (target IN ('_self', '_blank', '_parent', '_top');
# tables 改名
ALTER TABLE link RENAME TO url;

# create
insert into posts (title, content) values ('2', '123456798');
INSERT INTO table1(name,source,class) VALUES(20,89,'B');


# read
select * from posts;

# where title = '阿%' 阿開頭
# where title = '阿_' 1字元

# order by 讚 asc desc （asc 遞增(由小到大); desc 遞減(由大到小
# limit 取幾筆
# offset 搭配limit 可作分頁

# distinct 過濾重複
# sum
# max min
# group by / having > 針對group 過濾

# \timing 查看搜尋時間
# EXPLAIN
# EXPLAIN ANALYZE

# update
update table1 set source = source -1


# deleate
表資料
DELETE FROM posts where id=3;
表全砍
DROP TABLE posts
表不在 不報錯
DROP TABLE IF EXISTS posts;
相關依賴也刪除
DROP TABLE posts CASCADE;

清除表
TRUNCATE TABLE table_name;
重置序列
TRUNCATE TABLE table_name RESET IDENTITY;
清除關聯ex 外鍵
TRUNCATE TABLE table_name CASCADE;

## 常用function length concat substring random


# Trigger
ex1 : animals.name 更新 > 新舊名更新至animals_log
1. 建立 funtion
'''
CREATE OR REPLACE FUNCTION animal_name_if_changed()
    RETURNS trigger AS
$$
BEGIN
    IF NEW.name <> OLD.name THEN
    INSERT INTO animals_log (
        animals_id,
        change_time,
        old_name,
        new_name)
    VALUES
        (OLD.id,
         now(),
         OLD.name,
         NEW.name);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
'''
2. 綁定到funtion
'''
CREATE TRIGGER animals_update
  AFTER UPDATE
  ON animals
  FOR EACH ROW
  EXECUTE PROCEDURE animal_name_if_changed();
'''

ex2 :更新資料,更新修改時間

CREATE TABLE users (
  ...
  create_at timestamp(6) default current_timestamp
  update_at timestamp
)

CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.update_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_table_name_update_at
BEFORE UPDATE
ON table_name
FOR EACH ROW
EXECUTE PROCEDURE  update_modified_column();