from flaskext.mysql import MySQL

mysql_1 = MySQL(app, prefix=”mysql1”, host=os.getenv(“db_host”), user=os.getenv(“db_username”),password=os.getenv(“db_pass”),db=os.getenv(“db_name), autocommit=True, cursorclass=pymysql.cursors.DictCursor) mysql_2 = MySQL(app, prefix=”mysql2”, host=”host2”, user=”UN”, passwd=”&&”, db=”DB”,autocommit=True,cursorclass=pymysql.cursors.DictCursor)

@app.route(‘/’) @app.route(‘/index’) def hello():

cursor1 = mysql_1.get_db().cursor() #… cursor2 = mysql_2.get_db().cursor() #…
#mycursor.execute("CREATE TABLE input_table (latitude INTEGER(20),longitude INTEGER(20),bedrooms INTEGER(10),area INTEGER(20),seller VARCHAR(20),property_type VARCHAR(20), rent INTEGER(20))")
#mycursor.execute("CREATE TABLE data_table (latitude INTEGER(20),longitude INTEGER(20),bedrooms INTEGER(10),area INTEGER(20),seller VARCHAR(20),property_type VARCHAR(20),rent INTEGER(20))")
#mycursor.execute("SHOW TABLES")
#df = pd.read_csv('hyd_rents')
#df['area']= df['area'].apply(lambda x: int(x.replace(',','')))
#df = df[['latitude','longitude','bedrooms','area','seller','property_type','rent']]
#df.to_sql('data',connection,if_exists='replace',index=False)
print(df)
