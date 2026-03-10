from pyspark.sql.functions import *
from src.spark_session import get_spark_session

def run_streaming_pipeline(input_path, output_path):
    spark = get_spark_session()
    
    # Read streaming data
    df_stream = spark.readStream.format("csv").option("header", True).load(input_path)
    
    # Example transformation
    df_stream = df_stream.withColumn("processed_time", current_timestamp())
    
    # Write to Delta Lake in streaming mode
    query = df_stream.writeStream \
        .format("delta") \
        .outputMode("append") \
        .option("checkpointLocation", output_path + "/_checkpoints") \
        .start(output_path)
    
    query.awaitTermination()
