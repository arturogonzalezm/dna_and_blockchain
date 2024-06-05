import logging
from backend.logging_utils.singleton_logger import SingletonLogger


def test_singleton_logger_instance():
    logger1 = SingletonLogger("backend.logging_utils.singleton_logger").get_logger()
    logger2 = SingletonLogger("backend.logging_utils.singleton_logger").get_logger()
    assert logger1 is logger2


def test_logger_functionality(caplog):
    logger_name = "backend.logging_utils.singleton_logger"
    logger = SingletonLogger(logger_name).get_logger()
    with caplog.at_level(logging.DEBUG):
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

    print(caplog.record_tuples)  # Add this line to debug

    expected_log_tuples = [
        (logger_name, logging.DEBUG, "Debug message"),
        (logger_name, logging.INFO, "Info message"),
        (logger_name, logging.WARNING, "Warning message"),
        (logger_name, logging.ERROR, "Error message"),
        (logger_name, logging.CRITICAL, "Critical message")
    ]

    for expected in expected_log_tuples:
        assert expected in caplog.record_tuples

