import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import explode
from awsglue.dynamicframe import DynamicFrame



## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_JSON', 'S3_TARGET_PATH_JSON'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH_JSON']
target_path = args['S3_TARGET_PATH_JSON']

def dataframe_select(dframe):
    dframe = dframe.select("tv_results.adult",
                          "tv_results.backdrop_path",
                          "tv_results.id",
                          "tv_results.name",
                          "tv_results.original_language",
                          "tv_results.original_name",
                          "tv_results.overview",
                          "tv_results.poster_path",
                          "tv_results.media_type",
                          "tv_results.genre_ids",
                          "tv_results.popularity",
                          "tv_results.first_air_date",
                          "tv_results.vote_average",
                          "tv_results.vote_count",
                           explode("tv_results.origin_country").alias('origin_country'))
    dframe = dframe.withColumnRenamed('tv_results.popularity', 'popularity') \
  .withColumnRenamed('tv_results.vote_average', 'vote_average') \
  .withColumnRenamed('tv_results.vote_count', 'vote_count') \
  .withColumnRenamed('tv_results.name', 'name') \
  .withColumnRenamed('tv_results.first_air_date', 'first_air_date') \
  .withColumnRenamed('tv_results.id', 'id') 
  
  
    return dframe.withColumn('popularity', explode('popularity')) \
  .withColumn('vote_average', explode('vote_average')) \
  .withColumn('vote_count', explode('vote_count')) \
  .withColumn('first_air_date', explode('first_air_date')) \
  .withColumn('origin_country', explode('origin_country')) \
  .withColumn('name', explode('name')) \
  .withColumn('id', explode('id')) 
  


df = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_file
]
},
"JSON"
)


spark_df = df.toDF()
series = dataframe_select(spark_df)
dynamic_df = DynamicFrame.fromDF(series, glueContext)
series.show(20)


glueContext.write_dynamic_frame.from_options(
frame = dynamic_df,
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet")

job.commit()
