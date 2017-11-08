import logging
import settings

logging.basicConfig(filename=f'{settings.BASE_DIR}/sample.log', level=logging.INFO)

logging.debug('[D] This is a debug message')
logging.info('[I] Info message')
logging.error('[E] Cheese \'n Crackers!')
