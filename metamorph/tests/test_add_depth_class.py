
from metamorph.glue import build_glue, read_sample_data
from awsglue import DynamicFrame

from metamorph.transforms import add_depth_class

if __name__ == '__main__':
    data_sample = [
        {"depth": 50},
        {"depth": 100},
        {"depth": 75}
    ]

    context, job = build_glue()
    df = read_sample_data(data_sample, context)

    df = df.add_depth_class(depth_classes='25,50,100,150', depth_column='depth')

    df.show()

    job.commit()
