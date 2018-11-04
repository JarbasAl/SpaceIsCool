import requests


def EPIC_listing(natural=True, available=True):
    '''

    Natural Color	Metadata on the most recent date of natural color imagery.
    ost Recent Enhanced Color	Metadata on the most recent date of enhanced color imagery.The EPIC API provides information on the daily imagery collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC) instrument.
     Uniquely positioned at the Earth-Sun Lagrange point, EPIC provides full disc imagery of the Earth and captures
     unique perspectives of certain astronomical events such as lunar transits using a 2048x2048 pixel
     CCD (Charge Coupled Device) detector coupled to a 30-cm aperture Cassegrain telescope.


    :param natural: (bool) if False return enhanced imagery, if True return natural
    :param available: (bool) Retrieve a listing of all dates with available natural color imagery or all dates if false
    :return:
    '''
    base_url = "https://epic.gsfc.nasa.gov/api"
    if natural:
        base_url += "natural/"
    else:
        base_url += "enhanced/"

    if available:
        base_url += "available"
    else:
        base_url += "all"

    response = requests.get(base_url).json()
    return response


def EPIC(natural=True, date=None):
    '''
    The EPIC API provides information on the daily imagery collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC) instrument. Uniquely positioned at the Earth-Sun Lagrange point, EPIC provides full disc imagery of the Earth and captures unique perspectives of certain astronomical events such as lunar transits using a 2048x2048 pixel CCD (Charge Coupled Device) detector coupled to a 30-cm aperture Cassegrain telescope.


    Args:
        natural (bool): natural color or enhanced.
        date (str): Date to look up imagery, YYYY-MM-DD

    Returns:
        Dictionary object containing image data.
    '''
    base_url = "https://epic.gsfc.nasa.gov/api"
    if natural:
        base_url += "natural"
    else:
        base_url += "enhanced"

    if date:
        base_url += "/date/" + date

    response = requests.get(base_url).json()
    return response
