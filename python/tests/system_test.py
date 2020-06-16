from os.path import dirname, join, realpath
import pytest
import re
import sys

sys.path.append(realpath(join(dirname(__file__), '..')))

from meteoswissdata import StationMeasurementsFetcher
from meteoswissdata.station_measurements import get_base_url, REPOSITORY


STATION_IDENT_REGEX = re.compile('^[A-Z]{3}$')
EXPECTED_STATION_DATA_KEYS = {
    'time',
    'tre200s0',
    'rre150z0',
    'sre000z0',
    'gre000z0',
    'ure200s0',
    'tde200s0',
    'dkl010z0',
    'fu3010z0',
    'fu3010z1',
    'prestas0',
    'pp0qffs0',
    'pp0qnhs0',
    'ppz850s0',
    'ppz700s0',
    'dv1towz0',
    'fu3towz0',
    'fu3towz1',
    'ta1tows0',
    'uretows0',
    'tdetows0',
}

class TestSystem:
    @pytest.fixture
    def branch(self, request):
        return request.config.getoption("--branch")

    @pytest.fixture
    def fetcher(self, branch):
        fetcher = StationMeasurementsFetcher()
        fetcher.base_url = get_base_url(REPOSITORY, branch)
        return fetcher

    def test_get_stations(self, fetcher):
        stations = fetcher.get_stations()
        assert len(stations) > 0
        for station in stations:
            assert STATION_IDENT_REGEX.match(station)

    def test_get_stations_data(self, fetcher):
        stations_data = fetcher.get_stations_data()
        assert len(stations_data) > 0
        for station_ident, station_data in stations_data.items():
            assert STATION_IDENT_REGEX.match(station_ident)
            assert set(station_data.keys()) == EXPECTED_STATION_DATA_KEYS

    def test_get_station_data(self, fetcher):
        station_indents = fetcher.get_stations()
        station_ident = station_indents[0]
        station_data = fetcher.get_station_data(station_ident)
        assert set(station_data.keys()) == EXPECTED_STATION_DATA_KEYS
