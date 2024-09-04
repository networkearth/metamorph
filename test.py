
from metamorph.glue import build_glue, read_sample_data
from awsglue import DynamicFrame

from transforms.add_suntimes import add_suntimes

DynamicFrame.add_suntimes = add_suntimes

if __name__ == '__main__':
    data_sample = [
        {"lon": 10, "lat": 10, "epoch": 300},
        {"lon": 45, "lat": 56, "epoch": 600},
    ]

    context, job = build_glue()
    df = read_sample_data(data_sample, context)

    df = df.add_suntimes()

    df.show()

    job.commit()
