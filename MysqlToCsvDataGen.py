import pymysql.cursors
import pymysql
from pandas import DataFrame

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='@Asad11',
                             db='idea_ledger_v2',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT profile_desc from profiles"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = DataFrame(result)
        df.to_csv('ideaDesc.csv')
        print(result)
finally:
    connection.close()
