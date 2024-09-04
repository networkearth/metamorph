import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue import DynamicFrame

def build_glue():
    params = []
    if '--JOB_NAME' in sys.argv:
        params.append('JOB_NAME')
    args = getResolvedOptions(sys.argv, params)

    context = GlueContext(SparkContext.getOrCreate())
    job = Job(context)

    if 'JOB_NAME' in args:
        jobname = args['JOB_NAME']
    else:
        jobname = "test"
    job.init(jobname, args)

    return context, job

def read_sample_data(data, context):
    df1 = context.sparkSession.sparkContext.parallelize(data).toDF()
    return DynamicFrame.fromDF(df1, context, None)