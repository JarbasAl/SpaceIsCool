import requests
from space import NASA_KEY


def search_genelab(query, type):
    """
    GeneLab provides a RESTful Application Programming Interface (API) to its full-text search_exoplanet capability,
    which provides the same functionality available through the GeneLab public data repository website.
    The API provides a choice of standardized web output formats, such as JavaScript Object Notation (JSON)
    or Hyper Text Markup Language (HTML), of the search_exoplanet results. The GeneLab Search API can also
    federate with other heterogeneous external bioinformatics databases, such as the
    National Institutes of Health (NIH) / National Center for Biotechnology Information's (NCBI)
    Gene Expression Omnibus (GEO); the European Bioinformatics Institute's (EBI)
    Proteomics Identification (PRIDE); the Argonne National Laboratory's (ANL)
    Metagenomics Rapid Annotations using Subsystems Technology (MG-RAST).

    :param query:
    :return:
    """
    url = "https://genelab-data.ndc.nasa.gov/genelab/data/search_exoplanet?term=mouse%20liver&type=cgene"