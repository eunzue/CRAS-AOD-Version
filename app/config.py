import psycopg2

CRAS_CONEXION_BBDD="host='localhost' dbname='CRAs'  port='5432' user='user_cras' password='C0ntr4$3n4'"

def conexion():
	return psycopg2.connect(CRAS_CONEXION_BBDD)
