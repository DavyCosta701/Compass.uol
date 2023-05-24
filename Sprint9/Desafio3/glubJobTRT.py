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
    return dframe.select("adult",
                          "backdrop_path",
                          "id",
                          "name",
                          "original_language",
                          "original_name",
                          "overview",
                          "poster_path",
                          "media_type",
                          "genre_ids",
                          "popularity",
                          "first_air_date",
                          "vote_average",
                          "vote_count",
                          "origin_country").dropna()



df = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
source_file
]
},
"JSON",
{"multiline": True}
)

spark_df = df.toDF()
series = dataframe_select(spark_df)
dynamic_df = DynamicFrame.fromDF(series, glueContext)

glueContext.write_dynamic_frame.from_options(
frame = dynamic_df,
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet")

job.commit()