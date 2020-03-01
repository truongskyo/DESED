import logging
import sys
import logging.config


def create_logger(logger_name, terminal_level=logging.INFO, file_level=logging.INFO):
    """ Create a logger.
    Args:
        logger_name: str, name of the logger
        terminal_level: int, logging level in the terminal
        file_level: int, logging level in the file
    """
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
    })
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    tool_formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')

    if type(terminal_level) is str:
        if terminal_level.lower() == "debug":
            res_terminal_level = logging.DEBUG
        elif terminal_level.lower() == "info":
            res_terminal_level = logging.INFO
        elif "warn" in terminal_level.lower():
            res_terminal_level = logging.WARNING
        elif terminal_level.lower() == "error":
            res_terminal_level = logging.ERROR
        elif terminal_level.lower() == "critical":
            res_terminal_level = logging.CRITICAL
        else:
            res_terminal_level = logging.NOTSET
    else:
        res_terminal_level = terminal_level
    logger.setLevel(res_terminal_level)
    # Remove the stdout handler
    logger_handlers = logger.handlers[:]
    for handler in logger_handlers:
        if handler.name == 'std_out':
            logger.removeHandler(handler)

    terminal_h = logging.StreamHandler(sys.stdout)
    terminal_h.setLevel(res_terminal_level)
    terminal_h.set_name('stdout')
    terminal_h.setFormatter(tool_formatter)
    logger.addHandler(terminal_h)
    return logger


class DesedWarning(Warning):
    """The root DESED warning class"""
    pass


class DesedError(Exception):
    """The root DESED exception class"""
    pass