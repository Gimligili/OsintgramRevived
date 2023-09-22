import datetime
import json
import sys
import urllib
import os
import codecs
from pathlib import Path

import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from instagram_private_api import Client as AppClient
from instagram_private_api import ClientCookieExpiredError, ClientLoginRequiredError, ClientError, ClientThrottledError
from geopy.geocoders import Nominatim

from prettytable import PrettyTable

from src import printcolors as pc
from src import config