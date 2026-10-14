import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="bruhhelloworld", database="musicians"
)

if con.is_connected():
    print("Connected Dayo!")

cur = con.cursor()


def retrieve():
    cur.execute("select * from musicians where guitarist=1;")

    # data = cur.fetchmany(5)
    # print(data)

    # data = cur.fetchall()
    # for i in data:
    #     print(i)

    while True:
        data_ = cur.fetchone()

        if data_ == None:
            break

        print(data_, cur.rowcount)


def modify():
    cur.execute('insert into guitar_brands values ("test1"), ("test2");')
    con.commit()

    cur.execute("select * from guitar_brands;")
    data = cur.fetchall()

    print(data)

    cur.execute('delete from guitar_brands where brand_name in ("test1", "test2");')
    con.commit()

    cur.execute("select * from guitar_brands;")
    data = cur.fetchall()

    print(data)


retrieve()
