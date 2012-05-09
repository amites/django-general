from math import sin, cos, radians, degrees

from general.models import ZipCode


def calc_dist(lat_a, long_a, lat_b, long_b):
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    distance = (sin(lat_a) * sin(lat_b) +
                cos(lat_a) * cos(lat_b) * cos(long_a - long_b))
    return degrees(cos(distance)) * 69.09


def calc_dist_zip(zip_a, zip_b):
    loc_a = ZipCode.objects.get(zip_code=zip_a)
    loc_b = ZipCode.objects.get(zip_code=zip_b)
    return calc_dist(loc_a.lat, loc_a.lon, loc_b.lat, loc_b.lon)
