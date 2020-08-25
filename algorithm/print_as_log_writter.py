from builtins import print as sys_print
import logging

module_logger = logging.getLogger('print')
class LogWritter:
    logger = logging.getLogger('print.logwritter')

    @staticmethod
    def info(info):
        __name__.logger.info(info)

    @staticmethod
    def info(debbug):
        __name__.logger.debug(debbug)

    @staticmethod
    def info(warning):
        __name__.logger.warning(warning)

def print(*args, sep=' ', end='\n', file=None, writter='info'):
    print.prompt = ' ==> '
    print.prompt_enabled = True

    if print.prompt_enabled:
        sys_print( print.prompt , *args, sep, end=None, file=None )
    else:
        sys_print( *args, sep, end=None, file=None )
    getattr(LogWritter.logger, writter)(*args)
