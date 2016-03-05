import requests
import json

base_url = 'https://server16808.contentdm.oclc.org'

collections_url = '{url}/dmwebservices/index.php?q=dmGetCollectionList/json'.format(url=base_url)
collections = requests.get(collections_url).json()

out = []

for collection in collections:
    alias = collection['alias'].lstrip('/')
    records_url = '{url}/dmwebservices/index.php?q=dmQuery/{alias}/json'.format(url=base_url, alias=alias)
    records = requests.get(records_url).json()['records']
    collection['items'] = []
    for record in records:
        item_url = '{url}/dmwebservices/index.php?q=dmGetItemInfo/{alias}/{find}/json'.format(url=base_url, alias=alias, find=record['find'])
        item = requests.get(item_url).json()
        collection['items'].append(item)
    out.append(collection)

with open('collections.json', 'w') as outfile:
    json.dump(out, outfile, indent = 4)
