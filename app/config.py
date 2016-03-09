import psycopg2

CRAS_CONEXION_BBDD="host='localhost' dbname='cras'  port='5432' user='cras_aragon' password='C0ntr4$3n4'"

def conexion():
	return psycopg2.connect(CRAS_CONEXION_BBDD)
