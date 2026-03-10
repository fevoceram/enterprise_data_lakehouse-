from delta.tables import DeltaTable
from src.spark_session import get_spark_session

def merge_data(delta_table_path, new_data_df, merge_condition):
    spark = get_spark_session()
    delta_table = DeltaTable.forPath(spark, delta_table_path)
    
    delta_table.alias("target").merge(
        new_data_df.alias("source"),
        merge_condition
    ).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
    
    print("Merge operation completed")
