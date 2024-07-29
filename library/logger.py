import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='../quickbase_task.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
