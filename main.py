NBH_URL_TEMPLATE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/%H/text/blend_nbhtx.t%Hz"
NBH_LENGTH = 38

NBS_URL_TEMPLATE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/%H/text/blend_nbstx.t%Hz"
NBS_LENGTH = 42

NBE_URL_TEMPLATE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/%H/text/blend_nbetx.t%Hz"
NBE_LENGTH = 31

NBX_URL_TEMPLATE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/%H/text/blend_nbxtx.t%Hz"
NBX_LENGTH = 30

from datetime import datetime, timedelta
from requests import get
from re import search

def chronological_plan ():
    '''Plan a list of ten UTC datetimes, one hour apart in reverse.'''
    plan = []
    for i in range(0, 10):
        plan.append(datetime.utcnow() - i * timedelta(hours=1))

    return plan

def url_plan (dts, url_template):
    plan = []
    for dt in dts:
        plan.append(dt.strftime(url_template))

    return plan

def fetch_plan (plan):
    '''Try fetching a list of URL's in order, return the first success.'''
    for url in plan:
        r = get(url)
        if r.ok:
            return r.text

def parse_nbm (text, station, length):
    '''Return N lines describing the specified station.'''
    pattern = '^ ' + station
    lines = text.splitlines()

    for i in range(len(lines)):
        if search(pattern, lines[i]):
            return ('\n').join(lines[i:i+length])

if __name__ == "__main__":
    t = fetch_plan(url_plan(chronological_plan(), NBH_URL_TEMPLATE))
    print(parse_nbm(t, "KBNA", NBH_LENGTH))

    print()

    t = fetch_plan(url_plan(chronological_plan(), NBS_URL_TEMPLATE))
    print(parse_nbm(t, "KBNA", NBS_LENGTH))

    print()

    t = fetch_plan(url_plan(chronological_plan(), NBE_URL_TEMPLATE))
    print(parse_nbm(t, "KBNA", NBE_LENGTH))

    print()

    t = fetch_plan(url_plan(chronological_plan(), NBX_URL_TEMPLATE))
    print(parse_nbm(t, "KBNA", NBX_LENGTH))
