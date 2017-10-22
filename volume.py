import json
from pprint import pprint

#cm
point_length = 40
point_width = 40

#cm
silo_width = 320
silo_length = 320
silo_height = 600

json_file = 'medicao-silo.json'


def cm_cubed_to_m_cubed(value):
    return value / 100 ** 3


def calc_volume(distances):
    c1 = distances['c1']['p1'] + distances['c1']['p2'] + distances['c1']['p3'] + distances['c1']['p4'] + \
         distances['c1']['p5'] + distances['c1']['p6'] + distances['c1']['p7'] + distances['c1']['p8']
    c2 = distances['c2']['p1'] + distances['c2']['p2'] + distances['c2']['p3'] + distances['c2']['p4'] + \
         distances['c2']['p5'] + distances['c2']['p6'] + distances['c2']['p7'] + distances['c2']['p8']
    c3 = distances['c3']['p1'] + distances['c3']['p2'] + distances['c3']['p3'] + distances['c3']['p4'] + \
         distances['c3']['p5'] + distances['c3']['p6'] + distances['c3']['p7'] + distances['c3']['p8']
    c4 = distances['c4']['p1'] + distances['c4']['p2'] + distances['c4']['p3'] + distances['c4']['p4'] + \
         distances['c4']['p5'] + distances['c4']['p6'] + distances['c4']['p7'] + distances['c4']['p8']
    c5 = distances['c5']['p1'] + distances['c5']['p2'] + distances['c5']['p3'] + distances['c5']['p4'] + \
         distances['c5']['p5'] + distances['c5']['p6'] + distances['c5']['p7'] + distances['c5']['p8']
    c6 = distances['c6']['p1'] + distances['c6']['p2'] + distances['c6']['p3'] + distances['c6']['p4'] + \
         distances['c6']['p5'] + distances['c6']['p6'] + distances['c6']['p7'] + distances['c6']['p8']
    c7 = distances['c7']['p1'] + distances['c7']['p2'] + distances['c7']['p3'] + distances['c7']['p4'] + \
         distances['c7']['p5'] + distances['c7']['p6'] + distances['c7']['p7'] + distances['c7']['p8']
    c8 = distances['c8']['p1'] + distances['c8']['p2'] + distances['c8']['p3'] + distances['c8']['p4'] + \
         distances['c8']['p5'] + distances['c8']['p6'] + distances['c8']['p7'] + distances['c8']['p8']
    return cm_cubed_to_m_cubed(point_length * point_width * (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8))


with open(json_file) as data_file:
    measures = json.load(data_file)
    data_file.close()

    silo_volume = cm_cubed_to_m_cubed(silo_width * silo_length * silo_height)

    for measure in measures:
        free_space = calc_volume(measure['distances'])
        occupied_volume = silo_volume - free_space
        pprint('Occupied Volume: ' + str(round(occupied_volume, 2)) + 'm³, ' +
               'Free space: ' + str(round(free_space, 2)) + 'm³')
