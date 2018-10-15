import requests


def launches():
    url = "https://api.spacexdata.com/v3/launches"
    return requests.get(url).json()


def capsules():
    url = "https://api.spacexdata.com/v3/capsules"
    return requests.get(url).json()


def rockets():
    url = "https://api.spacexdata.com/v3/rockets"
    return requests.get(url).json()
