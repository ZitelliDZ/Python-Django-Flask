import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="prueba" )
cursor = connection.cursor()

try:
    #connection.autocommit(True)
    sql = ('INSERT INTO persona(nombre, apellido, edad, email) VALUES (%s,%s,%s,%s);')
    valores = (
    ('Diego','Zitelwwwwwwwwwwwwwwwwwwwwwwwwwwwwli',30,'zitelli@gmail.com'),
    ('Carlos','Larwwwwwwwwwwwwwwwwwwwwwwwwwa',2322,'carla@gmail.com'),
    ('Mariela','Ortellwwwwwwwwwwwwwwwwwwwwwwwado',26,'mari@gmail.com')
    )
    cursor.executemany(sql,valores)

    registros_insertados = cursor.rowcount
    print(registros_insertados)


    id_persona = 6
    sql = ('UPDATE persona SET nombre = %s,apellido = %s,email = %s,edad = %s WHERE id_persona = %s;')
    valores = (
        ('1Diego','Zitelli',30,'zitelli@gmail.com',6),
        ('2Carlos','Lara22222222222222222222222222222222222222222222',2322,'carla@gmail.com',7),
        ('3Mariela','Ortellado',26,'mari@gmail.com',8)
    )
    cursor.executemany(sql,valores)
    connection.commit()
    registros_insertados = cursor.rowcount
    print(registros_insertados)
except Exception as e:
    connection.rollback()
    print('Error:',e)
finally:
    sql = 'SELECT * FROM persona ORDER BY id_persona;'
    cursor.execute(sql)
    registros = cursor.fetchall()
    print(registros)


    cursor.close()
    # some other statements  with the help of cursor
    connection.close()