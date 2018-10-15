import requests
from space import NASA_KEY


def coronal_mass_ejections(start_date=None, end_date=None):
    """
    Coronal Mass Ejection (CME)
    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/CME?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def coronal_mass_ejection_analysis(start_date=None, end_date=None, most_accurate_only=True, complete_entry_only=True,
                                   speed=0, half_angle=0, catalog="ALL", keyword="NONE"):
    """

    :param start_date: default 30 days prior to current UTC time
    :param end_date: default to current UTC time
    :param most_accurate_only:
    :param complete_entry_only:
    :param speed: (lower limit): default is set to 0
    :param half_angle:
    :param catalog:default is set to ALL (choices: ALL, SWRC_CATALOG, JANG_ET_AL_CATALOG)
    :param keyword: default is set to NONE (example choices: swpc_annex)
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/CMEAnalysis?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    if most_accurate_only:
        base_url += "mostAccurateOnly=true&"
    else:
        base_url += "mostAccurateOnly=false&"

    if complete_entry_only:
        base_url += "completeEntryOnly=true&"
    else:
        base_url += "completeEntryOnly=false&"

    base_url += "speed=" + str(speed) + "&"
    base_url += "halfAngle=" + str(half_angle) + "&"
    base_url += "catalog=" + catalog + "&"
    base_url += "keyword=" + keyword + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def geomagnetic_storms(start_date=None, end_date=None):
    """
    Coronal Mass Ejection (CME)
    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/GST?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def interplanetary_shock(start_date=None, end_date=None, location="ALL", catalog="ALL"):
    """
    Coronal Mass Ejection (CME)
    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    location: default to ALL (choices: Earth, MESSENGER, STEREO A, STEREO B)
    catalog: default to ALL (choices: SWRC_CATALOG, WINSLOW_MESSENGER_ICME_CATALOG)
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/GST?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    base_url += "location=" + location + "&"
    base_url += "catalog=" + catalog + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def solar_flare(start_date=None, end_date=None):
    """
    Solar Flare (FLR)

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/FLR?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def solar_energetic_particles(start_date=None, end_date=None):
    """
    Solar Energetic Particle (SEP)

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/SEP?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def magnetopause_crossing(start_date=None, end_date=None):
    """
    Magnetopause Crossing (MPC)

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/MPC?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def radiation_belt_enhancement(start_date=None, end_date=None):
    """
    Radiation Belt Enhancement (RBE)

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/RBE?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def high_speed_stream(start_date=None, end_date=None):
    """
    Hight Speed Stream (HSS)

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/HSS?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response


def WSA_EnlilSimulation(start_date=None, end_date=None):
    """
    WSA+EnlilSimulation

    startDate: default to 30 days prior to current UTC date
    endDate: default to current UTC date
    :return:
    """
    base_url = "https://api.nasa.gov/DONKI/WSAEnlilSimulations?"

    if start_date:
        base_url += "startDate=" + start_date + "&"

    if end_date:
        base_url += "endDate=" + end_date + "&"

    url = base_url + "api_key=" + NASA_KEY
    response = requests.get(url).json()
    return response
