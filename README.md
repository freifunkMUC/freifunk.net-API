Installation:
* Clone this repo, e.g. to /opt/freifunk.net-API
* Check URLs in freifunkAPIUpdater.py and node_stats.py
* Make sure the user has pubkey SSH access to the freifunkt.net-API git repo
* Install Crontabs, e.g.:
  0 0 * * * cd /opt/freifunk.net-API && ./updateFreifunkAPI.sh
  * * * * * cd /opt/freifunk.net-API && python node_stats.py > node_stats
