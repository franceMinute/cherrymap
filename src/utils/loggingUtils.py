import logging

def parse_log_level(log_level):
    """ Return log level from input arg """
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    level = levels.get(log_level.upper())

    if level is None:
        raise ValueError(f'Invalid log level: {log_level}')
    return level