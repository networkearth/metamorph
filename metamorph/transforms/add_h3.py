import h3

from awsglue import DynamicFrame

def add_h3_for_record(row, resolution, lon_column, lat_column, prefix):
    row[f'{prefix}h3_index'] = h3.geo_to_h3(row[lat_column], row[lon_column], resolution)
    lat, lon = h3.h3_to_geo(row[f'{prefix}h3_index'])
    row[f'{prefix}h3_lat_bin'] = (lat // 10) * 10
    row[f'{prefix}h3_lon_bin'] = (lon // 10) * 10
    row[f'{prefix}h3_resolution'] = resolution
    return row

def add_h3(self, resolution, lon_column='lon', lat_column='lat', prefix=''):
    resolution = int(resolution.strip())
    return self.map(f = lambda r: add_h3_for_record(r, resolution, lon_column, lat_column, prefix))

DynamicFrame.add_h3 = add_h3