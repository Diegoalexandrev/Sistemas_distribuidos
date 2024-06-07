import findspark
from pyspark.sql import SparkSession
import psycopg2

# Inicialização do findspark com o caminho correto para o Spark
findspark.init("/usr/spark-3.5.1/")

# Criação da sessão Spark
spark = SparkSession.builder.appName("Lab8").getOrCreate()
sc = spark.sparkContext

# Função para inserir dados no PostgreSQL
def insert_into_postgres(line):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',  # Seu usuário PostgreSQL
        password='diego',  # Sua senha PostgreSQL
        database='lab8'  # Seu banco de dados PostgreSQL
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO textdata (line) VALUES (%s)", (line,))
    conn.commit()
    cursor.close()
    conn.close()

# Caminho para o arquivo no HDFS
file_path = "hdfs://spark-master:9000/datasets/texto_500.txt"

# Carregar as linhas do arquivo no Spark
lines = sc.textFile(file_path)

# Aplicar a função de inserção para cada linha
lines.foreach(insert_into_postgres)

# Encerrar a sessão Spark
spark.stop()
