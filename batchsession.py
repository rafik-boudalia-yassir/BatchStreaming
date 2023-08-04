from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define the schema
schema = StructType([
    StructField("driver_id", IntegerType()),
    StructField("driver_location", StringType()),
    StructField("order_amount", IntegerType()),
    StructField("order_status", StringType())
])


# Create a SparkSession
spark = SparkSession.builder.appName("VTCApp").getOrCreate()

# Read the CSV file in a streaming manner
df = spark.readStream.schema(schema).csv('/home/ubuntu/Desktop/BatchStreaming/sample_data.csv', header=True)

# Perform some transformations if necessary

# Write the data out in a streaming manner
query = df.writeStream.outputMode("append").format("console").start()

query.awaitTermination()

