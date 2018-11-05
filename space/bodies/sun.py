import requests
from space.weather import solar_energetic_particles, solar_flare


def recent_sunspots():
    """
    World Data Center for the production, preservation and dissemination of the international sunspot number

    For more information on the data, visit http://www.sidc.be/silso/datafiles and look at the Daily Estimated Sunspot Number.

    :return:
    """
    spdata = requests.get("http://www.sidc.be/silso/DATA/EISN/EISN_current.csv")
    sptext = spdata.text
    splines = sptext.splitlines()
    splines.reverse()
    spdays = splines[1].split(',')[4] + ", " + \
             splines[2].split(',')[4] + ", " + \
             splines[3].split(',')[4] + ", " + \
             splines[4].split(',')[4] + ", " + \
             splines[5].split(',')[4] + ", " + \
             splines[6].split(',')[4]
    data = {'spotcounts': spdays}
    return data


def sunspot_count():
    """
    World Data Center for the production, preservation and dissemination of the international sunspot number

    For more information on the data, visit http://www.sidc.be/silso/datafiles and look at the Daily Estimated Sunspot Number.

    :return:
    """
    spdata = requests.get("http://www.sidc.be/silso/DATA/EISN/EISN_current.csv")
    sptext = spdata.text
    splines = sptext.splitlines()
    splines.reverse()
    spfields = splines[1].split(',')
    spyfields = splines[2].split(',')
    chngcomment = " "
    pcchange = float(spyfields[4]) / float(spfields[4])
    if (pcchange < 0.5):
        chngcomment = " down a lot "

    if (pcchange > 2):
        chngcomment = " up a lot "

    data = {'spotcount': spfields[4], 'stations': spfields[7], 'spcomment': chngcomment}
    return data

print(sunspot_count())