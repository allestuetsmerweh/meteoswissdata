import subprocess
import sys

from .data_updater import download, git_setup, git_push
from .transform import transform

BRANCH = sys.argv[1] if len(sys.argv) > 1 else 'data'

git_setup('ci-build', 'ci-build@hatt.style', BRANCH)
download([
    {
        'url': 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv',
        'file': 'raw_station_measurements.csv',
    }
])
transform()
git_push('Data update', BRANCH)
