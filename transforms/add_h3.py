import h3

from awsglue import DynamicFrame

def add_h3_for_record(row, resolution):
    row['h3_index'] = h3.geo_to_h3(row['lat'], row['lon'], resolution)
    lat, lon = h3.h3_to_geo(row['h3_index'])
    row['h3_lat_bin'] = (lat // 10) * 10
    row['h3_lon_bin'] = (lon // 10) * 10
    row['h3_resolution'] = resolution
    return row

def add_h3(self, resolution):
    resolution = int(resolution.strip())
    return self.map(f = lambda r: add_h3_for_record(r, resolution))

DynamicFrame.add_h3 = add_h3