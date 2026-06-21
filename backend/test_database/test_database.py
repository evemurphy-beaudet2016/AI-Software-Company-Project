import psycopg2

conn = psycopg2.connect(
    dbname="ai_software_company",
    user="postgres",
    password="Banana!!",
    host="localhost",
    port="5432"
)

print("Connection successful!")

conn.close()