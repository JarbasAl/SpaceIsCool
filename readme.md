# Space Is Cool
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

Space is Awesome, get all the space data with this package


# Install 

    pip install SPACEisCool

# usage

Getting the next cool thing happening in space

    from space import next_cool_thing
        
    space_thing = next_cool_thing()
    text = space_thing["description"]
    
output

    {'date': 'On January 1, 2019 (2 months from now):',
     'description': 'New Horizons (the probe that took our best ever photos of '
                    'Pluto) is still going strong. It will pass Kuiper Belt Object '
                    '2014 MU69 at the start of 2019.',
     'event': 'new horizons will arrive at KBO 2014 MU69',
     'info': {'2014 MU69': 'https://en.wikipedia.org/wiki/2014_MU69',
              'NASA': 'https://www.nasa.gov/mission_pages/newhorizons/main/',
              'best ever photos of Pluto': 'https://www.nasa.gov/sites/default/files/thumbnails/image/edu_what_is_pluto_1.png'},
     'picture': 'http://spaceiscool.com/cool/new-horizons.png',
     'picture_credits': 'By National Aeronautics and Space Administration (NASA), '
                        'Applied Physics Laboratory - PEPSSI Instrument Tastes '
                        "Pluto's Atmosphere from the Applied Physics Laboratory "
                        'New Horizons website., Public Domain, '
                        'https://commons.wikimedia.org/w/index.php?curid=41340864'}

Getting info about astronauts in orbit

    from space import next_cool_thing, astronauts_in_space
    
    astronauts = astronauts_in_space()
    
output

    {'message': 'success',
     'number': 3,
     'people': [{'craft': 'ISS', 'name': 'Sergey Prokopyev'},
                {'craft': 'ISS', 'name': 'Alexander Gerst'},
                {'craft': 'ISS', 'name': 'Serena Aunon-Chancellor'}]}
                
                
                
Wondering where the ISS is?
 
    from space import iss
    
    iss_data = iss()
    
    import reverse_geocode
    
    coordinates = (iss_data["iss_position"]["latitude"], iss_data[
        "iss_position"]["longitude"])
    
    location = reverse_geocode.search([coordinates])

output

    {'iss_position': {'latitude': '-51.4413', 'longitude': '-66.4392'},
     'message': 'success',
     'timestamp': 1541367222}
    [{'country_code': 'AR', 'country': 'Argentina', 'city': 'San Julián'}]
