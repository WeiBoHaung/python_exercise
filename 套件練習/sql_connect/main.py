import mysql.connector as mysql

conn = mysql.connect(host="localhost", user='root', password="", database="cloud")
def showtable(conn):
    cursor=conn.cursor()
    cursor.execute('select * from member')
    values=cursor.fetchall()
    cursor.close()
    for x in values:
        print(x)

def add(conn):
    ls=[['楊大大','abcd','2000-01-02'],
        ['張大大','SSSSd','2000-01-02'],
        ['林大大','HHHHH','2000-01-02'],
    ]
    for l in ls:
        cmd="insert into member (account,password,bethday) values ('{0}','{1}','{2}')".format(l[0],l[1],l[2])
        cursor = conn.cursor()
        cursor.execute(cmd)
    conn.commit()
    showtable(conn)
    cursor.close()


def updatesql(conn,str):
    cursor = conn.cursor()
    cursor.execute(str)
    conn.commit()
    cursor.close()
    showtable(conn)


if __name__ == '__main__':


    add(conn)
    updatesql(conn,"update member set account='xxxx' where id=4")
    conn.close()