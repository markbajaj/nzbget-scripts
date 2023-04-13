#!/usr/bin/env python
###########################################
### NZBGET POST-PROCESSING SCRIPT       ###
#  Update Jellyfin Library
#
# Short one liner to update
# The Jellyfin Library on given host/
#
################################
### OPTIONS                  ###
# Jellyfin server IP
#ipaddress=jellyfin_server_ip

# Jellyfin Port
#port=8096

# Jellyfin API Key
#apikey=your_jellyfin_api_key

### NZBGET POST-PROCESSING SCRIPT       ###

import requests
import os
import sys
import shutil

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_NONE=95
POSTPROCESS_ERROR=94

addr=os.environ['NZBPO_IPADDRESS']
port=os.environ['NZBPO_PORT']
apikey=os.environ['NZBPO_APIKEY']

# For DEBUG
print(f"{port=}, {addr=}, {apikey=}")

url = 'http://' + addr + ':' + str(port) + '/library/refresh?api_key=' + str(apikey)
print(f"{url=}")
text = ""
res = requests.post(url, data = text)

# Returing status to NZBGet
sys.exit(POSTPROCESS_SUCCESS)
