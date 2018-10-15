import requests
from bs4 import BeautifulSoup

NASA_KEY = "DEMO_KEY"


def astronomy_picture_of_the_day(date=None, concept_tags=None):
    """

    date	YYYY-MM-DD	today	The date of the APOD image to retrieve
    concept_tags	bool	False	Return an ordered dictionary of concepts from the APOD explanation

    """

    base_url = "https://api.nasa.gov/planetary/apod?"

    if date:
        base_url += "date=" + date + "&"

    if concept_tags:
        base_url += "concept_tags=True" + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def space_news():
    url = "https://dry-eyrie-9951.herokuapp.com/"
    return requests.get(url).json()


def iss():
    url = "http://api.open-notify.org/iss-now.json"
    return requests.get(url).json()


def astronauts_in_space():
    url = "http://api.open-notify.org/astros.json"
    return requests.get(url).json()


def next_cool_thing():
    base_url = "http://spaceiscool.com/"
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, "html.parser")
    date = soup.find("h3").text[:-1]  # remove trailing :
    event = soup.find("h2").text
    _, text, more = soup.find_all("p")
    description = text.text
    urls = {}
    bucket = []
    for url in text.find_all("a"):
        urls[url.text] = url["href"]
        bucket.append(url["href"])
    for url in more.find_all("a"):
        if url["href"] not in bucket:
            urls[url.text] = url["href"]
    pic = base_url + soup.find_all("img")[1]["src"]
    pic_credits = soup.find_all("img")[1]["title"]
    return {"date": date, "event": event, "picture": pic, "picture_credits": pic_credits,
            "description": description, "info": urls}


