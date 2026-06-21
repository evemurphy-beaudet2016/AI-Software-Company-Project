# PostgreSQl connection

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ai_software_company",
        user="postgres",
        password="Banana!!",
        host="localhost",
        port="5432"
    )