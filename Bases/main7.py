import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="prueba" )
cursor = connection.cursor()

sql = ('INSERT INTO persona(nombre, apellido, edad, email) VALUES (%s,%s,%s,%s);')
valores = (
('Diego','Zitelli',30,'zitelli@gmail.com'),
('Carlos','Lara',23,'carla@gmail.com'),
('Mariela','Ortellado',26,'mari@gmail.com')
)
#cursor.executemany(sql,valores)
#connection.commit()

registros_insertados = cursor.rowcount
print(registros_insertados)


sql = 'SELECT * FROM persona ORDER BY id_persona;'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)


id_persona = 6
sql = ('UPDATE persona SET nombre = %s,apellido = %s,email = %s,edad = %s WHERE id_persona = %s;')
valores = (
    ('1Diego','Zitelli',30,'zitelli@gmail.com',6),
    ('2Carlos','Lara',23,'carla@gmail.com',7),
    ('3Mariela','Ortellado',26,'mari@gmail.com',8)
)
cursor.executemany(sql,valores)
connection.commit()

registros_actualizado = cursor.rowcount
print(registros_actualizado)


sql = 'SELECT * FROM persona ORDER BY id_persona;'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)




sql = 'DELETE FROM persona WHERE id_persona = %s;'
valor = (7,)
cursor.execute(sql,valor)
connection.commit()
registros_eliminados = cursor.rowcount
print(registros_eliminados)


sql = 'SELECT * FROM persona ORDER BY id_persona;'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)


cursor.close()
# some other statements  with the help of cursor
connection.close()