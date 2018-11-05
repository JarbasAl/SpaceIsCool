import requests
import decimal


def space_events(lon, lat, limit=None, date=None, elevation=None):
    '''
    http://api.predictthesky.org
    lat & lon expect decimal latitude and longitude values. (Required)
    elevation assumes meters. (Optional)
    limit assumes an integer. Default is 5. (Optional)
    date expects an ISO 8601 formatted date. (Optional)
    '''

    base_url = 'http://api.predictthesky.org/?'

    base_url += "lon=" + str(lon) + "&" + "lat=" + str(lat)

    if elevation is not None:
        base_url += "&" + 'elevation=' + elevation

    if date:
        base_url += "&" + 'date=' + date

    if limit:
        base_url += "&" + "limit=" + str(limit)

    return requests.get(base_url).json()


