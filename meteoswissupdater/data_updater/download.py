from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import time
from urllib.request import Request, urlopen

def download(configs):
    config = configs[0] # keep it simple for now
    headRequest = Request(url=config['url'], method='HEAD')
    for i in range(1):
        with urlopen(headRequest) as urlHandle:
            print(urlHandle.status)
            print(urlHandle.reason)
            info = urlHandle.info()
            etag = info.get('ETag')
            last_modified_str = info.get('Last-Modified')
            print(etag)
            print(last_modified_str)
            last_modified = parsedate_to_datetime(last_modified_str)
            print(last_modified)
            print(datetime.now(timezone.utc) - last_modified)

    getRequest = Request(url=config['url'], method='GET')
    with urlopen(getRequest) as urlHandle:
        with open(config['file'], 'wb+') as fileHandle:
            fileHandle.write(urlHandle.read())
