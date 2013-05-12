import requests
from bs4 import BeautifulSoup


FEED_URL = 'http://www.tfl.gov.uk/tfl/businessandpartners/syndication/feed.aspx?email=errkkgeorge@gmail.com&feedId=12'

STATION_IDS = [200, 33, 489]



def get_data():
    r = requests.get(FEED_URL)
    print r.status_code
    return r.text


def get_data_local():
    with open('cached.xml', 'r') as f:
        return f.read()


def get_by_id(station):
    """ Return True if the station's ID node matches the ids in the list """
    if station.id and int(station.id.text) in STATION_IDS:
        return True


def bikes():
    text = get_data_local()
    xml = text[38:]
    soup = BeautifulSoup(xml, 'xml')

    stations = soup.stations.find_all(get_by_id)
    res = []
    for station in stations:
        name = station.find('name').text
        total = int(station.nbDocks.text)
        spaces = int(station.nbEmptyDocks.text)
        bikes = int(station.nbBikes.text)
        res.append({'id': id, 'total': total, 'spaces': spaces, 'bikes': bikes,
                    'name': name})

    return res


if '__main__' == __name__:
    main()
