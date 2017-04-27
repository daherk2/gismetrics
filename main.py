
from __future__ import division
from math import radians, cos, sin, asin, sqrt

def Haversine(ponto1, ponto2, medida = 'metro'):
    lat1 = ponto1[0]
    lng1 = ponto1[1]
    lat2 = ponto2[0]
    lng2 = ponto2[1]
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * 6371 * asin(sqrt(d))  #diametro em km
    if medida == 'metro':
        return h * 1000
    if medida == 'kilometros':
        return h * 0.621371
    if medida == 'pes':
        return h * 3280.84

#print Haversine([-22.540540, -44.773176],[-22.540687, -44.773793])

