import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import explode
from awsglue.dynamicframe import DynamicFrame



## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_SERIES', 'S3_OUTPUT_PATH_SERIES', 'S3_INPUT_PATH_MOVIES', 'S3_OUTPUT_PATH_MOVIES'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_series = args['S3_INPUT_PATH_SERIES']
target_series = args['S3_OUTPUT_PATH_SERIES']

source_movies = args['S3_INPUT_PATH_MOVIES']
target_movies = args['S3_OUTPUT_PATH_MOVIES']

series = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_series
]
},
"CSV",
{"withHeader": True, "separator": "|"}
)

movies = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_series
]
},
"CSV",
{"withHeader": True, "separator": "|"}
)

glueContext.write_dynamic_frame.from_options(
frame = series,
connection_type = "s3",
connection_options = {"path": target_series},
format = "parquet")

glueContext.write_dynamic_frame.from_options(
frame = movies,
connection_type = "s3",
connection_options = {"path": target_movies},
format = "parquet")

job.commit()