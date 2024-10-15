from metamorph.glue import build_glue, read_sample_data
from awsglue import DynamicFrame

from metamorph.transforms import add_h3_options

if __name__ == '__main__':
    data_sample = [
        {"h3_index": "840ccebffffffff"},
        {"h3_index": "840cce3ffffffff"},
    ]

    context, job = build_glue()
    df = read_sample_data(data_sample, context)

    df = df.add_h3_options(col='h3_index', max_km=100)

    df.show()

    job.commit()