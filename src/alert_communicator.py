"""
Alert Communicator Module
Sends emergency alerts to contacts and authorities
"""

import logging
import json
import requests
from datetime import datetime
from typing import Dict, List

logger = logging.getLogger(__
