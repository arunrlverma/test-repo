import math
from os import rename
import sys

import requests

print(sys.version)
print(sys.executable)




r = requests.get("https://coreyms.com")
print(r)
