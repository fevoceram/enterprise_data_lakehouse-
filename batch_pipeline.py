import pandas as pd
from pyspark.sql import SparkSession
from src.spark_session import get_spark_session
from delta.tables import DeltaTable

def run_batch_pipeline(input_path, output_path):
    spark = get_spark_session()
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    
    # Example transformation
    df_transformed = df.dropDuplicates().fillna(0)
    
    # Write to Delta Lake
    df_transformed.write.format("delta").mode("overwrite").save(output_path)
    print(f"Batch pipeline completed. Data saved to {output_path}")
