from bs4 import BeautifulSoup
from prometheus_client import Gauge, start_http_server
from requests import get
from time import sleep
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

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

start_http_server(8000)
while True:
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
    sleep(60)
