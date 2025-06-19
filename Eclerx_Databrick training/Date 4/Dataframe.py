# Databricks notebook source
user_data=[(1,'teja'),(2,'swaroop')]
user_schema="id int, name string"
df=spark.createDataFrame(data=user_data, schema=user_schema)

# COMMAND ----------

df.show()

# COMMAND ----------

df.select("*").display()

# COMMAND ----------

df.select(col("id").alias("emp_id"))
from pyspark.sql.functions import col
df1=df.select(col("id").alias("emp_id"))

# COMMAND ----------

df1.show()

# COMMAND ----------

df1=df.withColumnsRenamed({"id":"emp_id","name":"emp_name"}).display()

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------


