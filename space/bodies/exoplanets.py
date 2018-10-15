import requests


def search_exoplanet(query, table="exoplanets"):
    """
    https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html

        The Exoplanet Archive API allows programatic access to NASA's Exoplanet Archive database.
        This API contains a ton of options so to get started please visit this page for introductory materials.
         To see what data is available in this API visit here and also be sure to check out best-practices
         and troubleshooting in case you get stuck. Happy planet hunting!

OR if astropical

    Exoplanets API (experimental)
    This simple API queries the exoplanet catalog the of Observatoire de Paris in France.

        :return:
        """
    base_url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=" + table
    if table == "astropical":
        base_url = "http://www.astropical.space/astrodb/api-exo.php?"

    if not query.startswith("&"):
        query = "&" + query
    url = base_url + query + "&format=json"
    response = requests.get(url).json()
    return response


def all_confirmed_planets():
    query = "where=*"
    return search_exoplanet(query)


def all_unconfirmed_planets():
    query = "where=koi_disposition like 'CANDIDATE'"
    return search_exoplanet(query, table="cumulative")


def all_microlensing_planets_with_time_series():
    query = "where=pl_discmethod like 'Microlensing' and st_nts > 0"
    return search_exoplanet(query, table="cumulative")


def stars_known_to_host_exoplanets():
    query = "select=distinct pl_hostname&order=pl_hostname"
    return search_exoplanet(query)


def confirmed_planets_in_mission_star_list():
    query = "here=st_ppnum>0"
    return search_exoplanet(query, table="missionstars")


def confirmed_planets_in_kepler_field():
    query = "where=pl_kepflag=1"
    return search_exoplanet(query)


def confirmed_planets_that_transit_host_stars():
    query = "where=pl_tranflag=1"
    return search_exoplanet(query)


def planetary_candidates(max_radius=2, max_temperature=303, min_temperature=180):
    query = "where=koi_prad<" + str(max_radius)
    query += " and koi_teq>" + str(min_temperature)
    query += " and koi_teq<" + str(max_temperature)
    query += " and koi_disposition like 'CANDIDATE'"
    return search_exoplanet(query)


def k2_targets_campaign9():
    query = "where=k2_campaign=9"
    return search_exoplanet(query, table="k2targets")


def exoplanet_by_mass(max_jovian_masses):
    """
    Get all exoplanets with up to x Jovian masses
    :param max_jovian_masses:
    :return:
    """
    query = "which=mass&limit=" + str(max_jovian_masses)
    return search_exoplanet(query, table="astropical")


def exoplanet_by_name(name):
    """
    :param name:
    :return:
    """
    query = "which=name&limit=" + name
    return search_exoplanet(query, table="astropical")


def exoplanet_by_radius(max_jovian_raddi):
    """
    Get all exoplanets with up to x Jovian raddi
    :param max_jovian_raddi:
    :return:
    """
    query = "which=radius&limit=" + str(max_jovian_raddi)
    return search_exoplanet(query, table="astropical")


def exoplanet_by_distance(max_parsecs):
    """
    Get all exoplanets up to x parsecs
    :param max_parsecs:
    :return:
    """
    query = "which=distance&limit=" + str(max_parsecs)
    return search_exoplanet(query, table="astropical")


def exoplanet_by_esi(esi):
    """
    :param esi:
    :return:
    """
    query = "which=esi&limit=" + str(esi)
    return search_exoplanet(query, table="astropical")


def exoplanet_by_star_type(star_type):
    """
    valid star types are, o, b, a, f, g, k, m
    :param star_type: str  m , g ...
    :return:
    """
    query = "which=spectral&limit=" + star_type
    return search_exoplanet(query, table="astropical")


def exoplanet_by_class(planet_class):
    """
    valid classes are "jovian", "neptunian", "superterran", "terran", and "subterran".

    :param planet_class: str
    :return:
    """
    query = "which=class&limit=" + planet_class
    return search_exoplanet(query, table="astropical")


def exoplanet_by_zone(zone):
    """
    Valid zones are "hot", "warm" and "cold" "subterran".

    :param zone: str
    :return:
    """
    query = "which=class&limit=" + zone
    return search_exoplanet(query, table="astropical")


def all_trappist_planets():
    """
    :return:
    """
    query = "which=name&limit=trappist"
    return search_exoplanet(query, table="astropical")


def all_subterran_planets():
    """
    :return:
    """
    query = "which=class&limit=subterran"
    return search_exoplanet(query, table="astropical")


def all_terran_planets():
    """
    :return:
    """
    query = "which=class&limit=terran"
    return search_exoplanet(query, table="astropical")


def all_superterran_planets():
    """
    :return:
    """
    query = "which=class&limit=superterran"
    return search_exoplanet(query, table="astropical")


def all_neptunian_planets():
    """
    :return:
    """
    query = "which=class&limit=neptunian"
    return search_exoplanet(query, table="astropical")


def all_jovian_planets():
    """
    :return:
    """
    query = "which=class&limit=jovian"
    return search_exoplanet(query, table="astropical")


def all_warm_zone_planets():
    """
    :return:
    """
    query = "which=zone&limit=warm"
    return search_exoplanet(query, table="astropical")


def all_hot_zone_planets():
    """
    :return:
    """
    query = "which=zone&limit=hot"
    return search_exoplanet(query, table="astropical")


def all_cold_zone_planets():
    """
    :return:
    """
    query = "which=zone&limit=cold"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_o_stars():
    query = "which=spectral&limit=o"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_b_stars():
    query = "which=spectral&limit=b"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_a_stars():
    query = "which=spectral&limit=a"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_f_stars():
    query = "which=spectral&limit=f"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_g_stars():
    query = "which=spectral&limit=g"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_k_stars():
    query = "which=spectral&limit=k"
    return search_exoplanet(query, table="astropical")


def all_exoplanet_around_m_stars():
    query = "which=spectral&limit=m"
    return search_exoplanet(query, table="astropical")
