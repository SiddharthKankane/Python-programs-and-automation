import inspect
import logging

def test_loggingDemo():

    loggerName= inspect.stack()[1][3]
    logger= logging.getLogger(loggerName)
    filehandler = logging.FileHandler("logging.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")