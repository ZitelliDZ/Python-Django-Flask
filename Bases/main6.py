import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="prueba" )
cursor = connection.cursor()
sql = 'SELECT * FROM persona ORDER BY id_persona;'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)

#id_persona = 2
id_persona = input('Persona?: ')
sql = 'SELECT * FROM persona WHERE id_persona = %s;'
llave_primaria = (id_persona,)
cursor.execute(sql,llave_primaria)
registros = cursor.fetchone()
print(registros)


sql = 'SELECT * FROM persona WHERE id_persona IN %s;'
entradas = input('Persona?: ')
tupla = tuple(entradas.split(','))
#llaves_primarias = ((1,),)
#llaves_primarias = ((1,2,3),)
llaves_primarias = (tupla,)
cursor.execute(sql,llaves_primarias)
registros = cursor.fetchall()
print(registros)




sql = ('INSERT INTO persona(noombre, apellido, edad, email) VALUES (%s,%s,%s,%s);')
valores = ('Carlos','Lara',23,'carla@gmail.com')
cursor.execute(sql,valores)
print(registros)

cursor.close()
# some other statements  with the help of cursor
connection.close()