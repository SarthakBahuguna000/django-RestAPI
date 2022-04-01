import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="qazplm000",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select Id from profiles_api_userprofile where email = 'sarthakbahuguna@outlook.com';"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall()

   print(mobile_records)
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
