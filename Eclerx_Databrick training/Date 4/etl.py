# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

# Create Spark session
spark = SparkSession.builder.appName("ShortETL").getOrCreate()

# Read source CSV
input_path = "dbfs:/FileStore/circuits.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

df = (spark.read.csv("dbfs:/FileStore/circuits.csv", header=True, inferSchema=True)
      .withColumnRenamed("circuitId", "circuit_id")
      .withColumn("load_date", current_date())
      .drop("url"))

df.display()





# COMMAND ----------


