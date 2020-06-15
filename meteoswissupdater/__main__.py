import subprocess

from .data_updater import download, git_setup, git_push
from .transform import transform

git_setup('ci-build', 'ci-build@hatt.style')
download([
    {
        'url': 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv',
        'file': 'raw_station_measurements.csv',
    }
])
transform()
git_push('Data update')
