# Databricks notebook source
print("hello world")


# COMMAND ----------

# MAGIC %sql
# MAGIC create table teja (
# MAGIC   emp_id int,
# MAGIC   emp_name varchar(100),
# MAGIC   salary decimal(10,2)
# MAGIC   );
# MAGIC   insert into teja(emp_id,emp_name,salary)
# MAGIC   values
# MAGIC     (101, 'Alice', 70000.00),
# MAGIC     (102, 'Bob', 65000.00),
# MAGIC     (103, 'Charlie', 72000.00),
# MAGIC     (104, 'Diana', 68000.00);
# MAGIC
# MAGIC     

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from teja;

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/us1-1.csv
