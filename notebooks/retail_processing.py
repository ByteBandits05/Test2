# Databricks notebook source
# Example retail ETL job
df = spark.read.format("csv").option("header", "true").load("/mnt/data/raw/retail.csv")
df_clean = df.dropna()
df_clean.write.format("delta").mode("overwrite").save("/mnt/data/gold/retail_sales")
