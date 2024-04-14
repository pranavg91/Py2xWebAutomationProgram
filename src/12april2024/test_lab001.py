import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("this is info")