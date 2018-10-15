import requests
from space import NASA_KEY


def probe_distances():
    url = "https://murmuring-anchorage-8062.herokuapp.com/distances.json"
    return requests.get(url).json()


def probes():
    url = "https://murmuring-anchorage-8062.herokuapp.com/dsn/probes.json"
    return requests.get(url).json()





