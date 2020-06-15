import csv
from datetime import datetime
import json
import os
from typing import Optional

FIRST_LINE = 'MeteoSchweiz / MeteoSuisse / MeteoSvizzera / MeteoSwiss\n'
SECOND_LINE = ' \n'
DATE_FORMAT = '%Y%m%d%H%M'

def parse_date(input: str) -> str:
    return datetime.strptime(input, DATE_FORMAT).isoformat()

def parse_float(input: str) -> Optional[float]:
    if input == '-':
        return None
    return float(input)

def transform():
    transform_into_single_json()
    transform_into_station_jsons()


def transform_into_single_json():
    with open('raw_station_measurements.csv') as csvfile:
        csvreader = get_csvreader(csvfile)
        with open('station_measurements.json', 'w+') as jsonfile:
            json.dump(
                {
                    station_data['stn']: transform_station_data(station_data)
                    for station_data in csvreader
                },
                jsonfile,
                indent=2,
            )


def transform_into_station_jsons():
    os.makedirs('station_measurements')
    with open('raw_station_measurements.csv') as csvfile:
        csvreader = get_csvreader(csvfile)
        for station_data in csvreader:
            station_ident = station_data['stn']
            filename = f'station_measurements/{station_ident}.json'
            with open(filename, 'w+') as jsonfile:
                json.dump(
                    transform_station_data(station_data),
                    jsonfile,
                    indent=2,
                )


def transform_station_data(station_data):
    return {
        'time': parse_date(station_data['time']),
        'tre200s0': parse_float(station_data['tre200s0']),
        'rre150z0': parse_float(station_data['rre150z0']),
        'sre000z0': parse_float(station_data['sre000z0']),
        'gre000z0': parse_float(station_data['gre000z0']),
        'ure200s0': parse_float(station_data['ure200s0']),
        'tde200s0': parse_float(station_data['tde200s0']),
        'dkl010z0': parse_float(station_data['dkl010z0']),
        'fu3010z0': parse_float(station_data['fu3010z0']),
        'fu3010z1': parse_float(station_data['fu3010z1']),
        'prestas0': parse_float(station_data['prestas0']),
        'pp0qffs0': parse_float(station_data['pp0qffs0']),
        'pp0qnhs0': parse_float(station_data['pp0qnhs0']),
        'ppz850s0': parse_float(station_data['ppz850s0']),
        'ppz700s0': parse_float(station_data['ppz700s0']),
        'dv1towz0': parse_float(station_data['dv1towz0']),
        'fu3towz0': parse_float(station_data['fu3towz0']),
        'fu3towz1': parse_float(station_data['fu3towz1']),
        'ta1tows0': parse_float(station_data['ta1tows0']),
        'uretows0': parse_float(station_data['uretows0']),
        'tdetows0': parse_float(station_data['tdetows0']),
    }


def get_csvreader(csvfile):
    first_line = csvfile.readline()
    if first_line != FIRST_LINE:
        raise Exception(f'Unexpected first line: {first_line}')
    second_line = csvfile.readline()
    if second_line != SECOND_LINE:
        raise Exception(f'Unexpected second line: {second_line}')
    return csv.DictReader(csvfile, delimiter=';')
