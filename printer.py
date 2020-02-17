from argparse import ArgumentParser
from time import sleep

from bs4 import BeautifulSoup
from prometheus_client import Gauge, start_http_server
from requests import get
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

parser = ArgumentParser(description='Poll and serve information about the Next House printers.')
parser.add_argument('-d', '--daemon', action='store_true', help='Run as a daemon for serving printer information')
args = parser.parse_args()

disable_warnings(InsecureRequestWarning)

printers = [
    ('justinbieber', '2e', Gauge('ink_level_2e', '2E Ink Level')),
    ('next2w', '2w', Gauge('ink_level_2w', '2W Ink Level')),
    ('nalgas', '3e', Gauge('ink_level_3e', '3E Ink Level')),
    ('printerbena', '3w', Gauge('ink_level_3w', '3W Ink Level')),
    ('fourest', '4e', Gauge('ink_level_4e', '4E Ink Level')),
    ('derp', '4w', Gauge('ink_level_4w', '4W Ink Level')),
    ('stirfry', '5e', Gauge('ink_level_5e', '5E Ink Level')),
    ('page-fault', '5w', Gauge('ink_level_5w', '5W Ink Level'))
]


def poll_printers():
    for p, wing, gauge in printers:
        name = '{} ({})'.format(p, wing)
        try:
            page = get("https://" + p + ".mit.edu", verify=False, timeout=5).text
        except:
            print(name + ': Not online.')
            continue

        soup = BeautifulSoup(page, 'lxml')
        found = soup.find('', {'id': 'SupplyGauge0'})
        if not found:
            gauge.set(0)
            print(name + ": Online, unknown ink level.")
        else:
            level = found.findAll(text=True)[0]
            gauge.set(int(str(level)[:-1]))
            print(name + ': Online, {} ink.'.format(level))


if args.daemon:
    print('Running as daemon on port 8000')
    start_http_server(8000)
    while True:
        poll_printers()
        sleep(60)
else:
    poll_printers()
