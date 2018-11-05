from space import iss
import requests
iss_data = iss()
latISS = iss_data["iss_position"]["latitude"]
lngISS = iss_data["iss_position"]["longitude"]
user = "demo"

ocean_geo_names_req = "http://api.geonames.org/oceanJSON?lat=" + latISS \
                      + "&lng=" + lngISS + "&username=" + user
land_geo_names_req = "http://api.geonames.org/countryCodeJSON?formatted=true" \
                     "&lat=" + latISS + "&lng=" + lngISS + "&username=" + user \
                     + "&style=full"

try:
    land_geo_names_res = requests.get(land_geo_names_req)
    toponym_obj = land_geo_names_res.json()
    if toponym_obj.get("status", {}).get("value", 0) == 15:
        ocean_geo_names_res = requests.get(ocean_geo_names_req)
        toponym_obj = ocean_geo_names_res.json()
        toponym = "the " + toponym_obj['ocean']['name']
    else:
        toponym = toponym_obj['countryName']
except:
    toponym = "unknown"

print(toponym)
