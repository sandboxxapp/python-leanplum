import logging

logging.basicConfig()  # dunno why, this makes it work in iPython (https://stackoverflow.com/a/44188369/6460591)

__all__ = ["Logger"]


def new_default_logger():
    return Logger()


class Logger(object):

    def __init__(self, name="leanplum", level="DEBUG"):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

    def set_level(self, level):
        self._logger.setLevel(level)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.warning(message)
