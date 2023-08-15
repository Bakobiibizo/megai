import enum
from datetime import datetime


class LogLevel(enum.Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


class Logger:
    def __init__(self, log_level=LogLevel.INFO):
        self.log_level = log_level

    def log(self, message, level=None):
        if not level:
            level = LogLevel.INFO
        if level.value >= self.log_level.value:
            log_entry = f"{datetime.now()} - {level.name} - {message}"
            print(log_entry)  # print to console (mocking stdout)
            self.write_to_file(log_entry)  # write to file

    def write_to_file(self, message):
        # This is a mock function for writing log messages to a file
        pass

    def debug(self, message):
        self.log(message, LogLevel.DEBUG)

    def info(self, message):
        self.log(message, LogLevel.INFO)

    def warning(self, message):
        self.log(message, LogLevel.WARNING)

    def error(self, message):
        self.log(message, LogLevel.ERROR)

    def critical(self, message):
        self.log(message, LogLevel.CRITICAL)


#  # Testing the logger
#  logger = Logger(log_level=LogLevel.DEBUG)
#  
#  logger.debug("This is a debug message")
#  logger.info("This is an info message")
#  logger.warning("This is a warning message")
#  logger.error("This is an error message")
#  logger.critical("This is a critical message")
