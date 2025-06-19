# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("DataFrame Operations Basic to Intermediate").enableHiveSupport().getOrCreate()


