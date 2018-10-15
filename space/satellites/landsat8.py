import requests
import decimal
from space import NASA_KEY


def imagery(lon=None, lat=None, dim=None, date=None, cloud_score=None):
    '''
    lat	float	n/a	Latitude
    lon	float	n/a	Longitude
    dim	float	0.025	width and height of image in degrees
    date	YYYY-MM-DD  today	date of image ----if not supplied, then the most recent image (i.e., closest to today) is returned
    cloud_score	bool	False	calculate the percentage of the image covered by clouds

    '''

    base_url = "https://api.nasa.gov/planetary/earth/imagery?"

    lon = decimal.Decimal(lon)
    lat = decimal.Decimal(lat)
    base_url += "lon=" + str(lon) + "&" + "lat=" + str(lat) + "&"

    if dim:
        dim = decimal.Decimal(dim)
        base_url += "dim=" + str(dim) + "&"

    if date:
        base_url += "date=" + date + "&"

    if cloud_score:
        base_url += "cloud_score=True" + "&"

    url = base_url + "api_key=" + NASA_KEY

    return requests.get(url).json()

    # This endpoint retrieves the date-times and asset names for available imagery for a supplied location.
    # The satellite passes over each point on earth roughly once every sixteen days.
    # This is an amazing visualization of the acquisition pattern for Landsat 8 imagery.
    # The objective of this endpoint is primarily to support the use of the imagery endpoint.


def assets(lon=None, lat=None, begin=None, end=None):
    '''
    lat	float	n/a	Latitude
    lon	float	n/a	Longitude
    begin	YYYY-MM-DD	n/a	beginning of date range

    end	        YYYY-MM-DD	today	end of date range  (optional)
    '''
    base_url = "https://api.nasa.gov/planetary/earth/assets?"

    lon = decimal.Decimal(lon)
    lat = decimal.Decimal(lat)
    base_url += "lon=" + str(lon) + "&" + "lat=" + str(lat) + "&"

    base_url += "begin=" + begin + "&"

    if end:
        base_url += "end=" + end + "&"

    url = base_url + "api_key=" + NASA_KEY

    return requests.get(url).json()
