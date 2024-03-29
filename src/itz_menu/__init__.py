import logging as log

import itz_menu.persistence.database as database
from itz_menu.config.settings import Settings

__version__ = '0.0.1'
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
log.info(f'Running with settings: {Settings()}')
database.init()
