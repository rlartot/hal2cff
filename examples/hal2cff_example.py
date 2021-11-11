from rdflib import Graph


def hal2cff(halref):
    """
    halref: str
        HAL document URL or identifier
    """
    pass


def get_hal_graph(halref):
    g = Graph()
    g.parse(halref)
    return g


def halref_to_url(halref):
    if halref.startswith("https://data.archives-ouvertes.fr/document/"):
        pass


g = get_hal_graph("https://data.archives-ouvertes.fr/document/hal-02371715.rdf")

for (sub, obj, pred) in g:
    print(sub,obj,pred)


