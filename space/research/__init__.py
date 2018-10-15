import requests
from space import NASA_KEY


def search_patents(query):
    """
    The NASA patent portfolio is available to benefit US citizens. Through partnerships and licensing agreements with industry, these patents ensure that NASA’s investments in pioneering research find secondary uses that benefit the economy, create jobs, and improve quality of life. This endpoint provides structured, searchable developer access to NASA’s patents that have been curated to support technology transfer.

    HTTP REQUEST
    GET https://api.nasa.gov/patents

    QUERY PARAMETERS
    Parameter	Type	Default	Description
    query	string	None	Search text to filter results
    concept_tags	bool	False	Return an ordered dictionary of concepts from the patent abstract
    limit	int	all	number of patents to return
    api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage

    :param query:
    :return:
    """
    url = "https://api.nasa.gov/patents/content?query=temperature&limit=5&api_key=DEMO_KEY"