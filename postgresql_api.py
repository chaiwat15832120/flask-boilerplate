import psycopg2
import os
try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://ieleliaubmehkq:d99b4a4efac7e97feba41df31312571f9d4975ce62e1eff5ba328eb8dfddb610@ec2-52-200-48-116.compute-1.amazonaws.com:5432/d2rb9fbc5vidu5'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)

    cur = connection.cursor()
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
    """)
    rows = cur.fetchall()
    print('Table list:')
    for row in rows:
        print("   ", row[0])
    cur.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def get_student_data():
    cur = connection.cursor()
    cur.execute("""
    SELECT firstname,lastname,age
     FROM student;
    """)
    rows = cur.fetchall()
    print('Student firstname:')
    print(rows)
    #for row in rows:
     #   print("   ", row[0])
    cur.close()
    return rows

get_student_data()