import requests
from space.bodies.exoplanets import stars_known_to_host_exoplanets


def search_star(query, table="stars"):
    """
        http://www.astropical.space/astrodb/apiref.php
        query the HIP stars database
        Currently, only the Hipparcos Star stars (down to mag 6.5) and Nearby Stars (139 stars) tables are connected to this API.

        table: stars or nearby
        :return:
        """
    base_url = "http://www.astropical.space/astrodb/api.php?&table=" + table

    if not query.startswith("&"):
        query = "&" + query
    url = base_url + query + "&format=json"
    response = requests.get(url).json()
    return response


def stars_by_constellation(constelation):
    """

    :param constelation: umi = ursa minor
    :return:
    """
    query = "which=constellation&limit=" + constelation
    return search_star(query)


def stars_by_magnitude(magnitude):
    """

    :param magnitude: int
    :return:
    """
    query = "which=magnitude&limit=" + str(magnitude)
    return search_star(query)


def stars_by_distance(max_light_years):
    """

    :param max_light_years: int
    :return:
    """
    query = "which=distance&limit=" + str(max_light_years)
    return search_star(query)


def stars_by_spectral_class(spectral_class):
    """

    :param spectral_class: str
    :return:
    """
    query = "which=spectrum&limit=" + spectral_class
    return search_star(query)


def stars_by_radial_velocity(min_velocity):
    """

    :param min_velocity: int km/s
    :return:
    """
    query = "which=radial&limit=" + str(min_velocity)
    return search_star(query)


def stars_by_solar_mass(min_mass):
    """

    :param min_mass: int solar masses
    :return:
    """
    query = "which=mass&limit=" + str(min_mass)
    return search_star(query)


def stars_by_radius(min_radius):
    """

    :param min_radius: int solar radius
    :return:
    """
    query = "which=radius&limit=" + str(min_radius)
    return search_star(query)


def stars_by_common_name(star_name):
    """

    :param star_name:str star name
    :return:
    """
    query = "which=name&limit=" + star_name
    return search_star(query)


def stars_by_designation(designation):
    """

    :param designation:str star name
    :return:
    """
    query = "which=designation&limit=" + designation
    return search_star(query)
