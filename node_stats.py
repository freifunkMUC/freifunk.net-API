
from datetime import datetime
from requests import get as rget

NODESJSON = 'https://map.ffmuc.net/data/meshviewer.json'


def scrape(url):
    '''returns remote json'''
    try:
        return rget(url, timeout=10).json()
    except Exception as ex:
        print(f"Error: {ex}")


if __name__ == '__main__':
    nodes = scrape(NODESJSON)

    if nodes:
        ONLINE = 0
        NONCLIENT = 0
        # print(nodes['nodes'])
        for node in nodes['nodes']:
            if node['is_online']:
                ONLINE += 1
                if node['is_gateway']:
                    NONCLIENT += 1
                    # print(node)

        now = datetime.now().strftime('%H:%M %d.%m.%Y')
        resultmsg = f"Status: online: {ONLINE} ({NONCLIENT} Router, {ONLINE-NONCLIENT} Teilnehmer) {now}"

        print(resultmsg)
