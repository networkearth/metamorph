
from metamorph.glue import build_glue, read_sample_data
from awsglue import DynamicFrame

from metamorph.transforms import add_h3

if __name__ == '__main__':

    data_sample = [
        {"lon": 10, "lat": 10, "epoch": 300},
        {"lon": 45, "lat": 56, "epoch": 600},
    ]

    context, job = build_glue()
    df = read_sample_data(data_sample, context)

    df = df.add_h3(resolution='4', lon_column='lon', lat_column='lat', prefix='my_')

    df.show()

    job.commit()
