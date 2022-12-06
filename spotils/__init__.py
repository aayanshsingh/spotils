"""Initialises the global instance & console and setups logging."""

import dotenv
from rich.console import Console

from spotils.client import generate_global_instance
from spotils.helpers.logging import setup_logging
from spotils.meta import __app_name__, __version__

setup_logging()

dotenv.load_dotenv()
console = Console()
instance = generate_global_instance()
