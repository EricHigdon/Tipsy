import os
from dotenv import load_dotenv


load_dotenv()

DEBUG = os.getenv('DEBUG', 'false') == 'true'
if DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
CONFIG_FILE = os.getenv('PUMP_CONFIG_FILE', 'pump_config.json')
COCKTAILS_FILE = os.getenv('COCKTAILS_FILE', 'cocktails.json')
LOGO_FOLDER = os.getenv('LOGO_FOLDER', 'drink_logos')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    OZ_COEFFICIENT= [
    (24.38),   # Pump 1
    (24.23),  # Pump 2
    (25.43),   # Pump 3
    (30.56),   # Pump 4
    (25.60),   # Pump 5
    (19.29),  # Pump 6
    (24.53),  # Pump 7
    (26.94),  # Pump 8
    (25.16),    # Pump 9
    (20.46),  # Pump 10
    (22.52),  # Pump 11
    (25),  # Pump 12
]
except ValueError:
    OZ_COEFFICIENT = 8.0

INVERT_PUMP_PINS = os.getenv('INVERT_PUMP_PINS', 'false') == 'true'
PUMP_CONCURRENCY = int(os.getenv('PUMP_CONCURRENCY', 3))
FULL_SCREEN = os.getenv('FULL_SCREEN', 'true') == 'true'
SHOW_RELOAD_COCKTAILS_BUTTON = os.getenv('SHOW_RELOAD_COCKTAILS_BUTTON', 'false') == 'true'
RELOAD_COCKTAILS_TIMEOUT = int(os.getenv('RELOAD_COCKTAILS_TIMEOUT', 0))
RETRACTION_TIME = float(os.getenv('RETRACTION_TIME', '0'))
USE_GPT_TRANSPARENCY = os.getenv('USE_GPT_TRANSPARENCY', 'false') == 'true'
COCKTAIL_IMAGE_SCALE = float(os.getenv('COCKTAIL_IMAGE_SCALE', '1.0'))