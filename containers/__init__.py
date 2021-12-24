"""
Implementation of a docker based container service
"""

import os
from dotenv import load_dotenv
from .service import Service

load_dotenv()
service = Service(os.getenv("TOOLS_DIR"))
