import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://data-lake-desafio-1/TRT/TMDB/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node MappingDimName
MappingDimName_node1684653215343 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[("id", "int", "id", "int"), ("name", "string", "name", "string")],
    transformation_ctx="MappingDimName_node1684653215343",
)

# Script generated for node MappingFact
MappingFact_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("popularity", "double", "popularity", "double"),
        ("vote_average", "double", "vote_average", "double"),
        ("vote_count", "int", "vote_count", "int"),
        ("id", "int", "id", "int"),
    ],
    transformation_ctx="MappingFact_node2",
)

# Script generated for node MappingDimData
MappingDimData_node1684653212604 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("first_air_date", "string", "first_air_date", "string"),
        ("id", "int", "id", "int"),
    ],
    transformation_ctx="MappingDimData_node1684653212604",
)

# Script generated for node MappingDimLoc
MappingDimLoc_node1684653594066 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("id", "int", "id", "int"),
        ("origin_country", "string", "origin_country", "string"),
    ],
    transformation_ctx="MappingDimLoc_node1684653594066",
)

# Script generated for node name_pop
name_pop_node1684653448077 = glueContext.write_dynamic_frame.from_catalog(
    frame=MappingDimName_node1684653215343,
    database="desafio",
    table_name="dim_name",
    transformation_ctx="name_pop_node1684653448077",
)

# Script generated for node fact_pop
fact_pop_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=MappingFact_node2,
    database="desafio",
    table_name="fact_series",
    transformation_ctx="fact_pop_node3",
)

# Script generated for node data_pop
data_pop_node1684653223464 = glueContext.write_dynamic_frame.from_catalog(
    frame=MappingDimData_node1684653212604,
    database="desafio",
    table_name="dim_data",
    additional_options={"partitionKeys": ["first_air_date"]},
    transformation_ctx="data_pop_node1684653223464",
)

# Script generated for node loc_pop
loc_pop_node1684653596400 = glueContext.write_dynamic_frame.from_catalog(
    frame=MappingDimLoc_node1684653594066,
    database="desafio",
    table_name="dim_localidade",
    transformation_ctx="loc_pop_node1684653596400",
)

job.commit()