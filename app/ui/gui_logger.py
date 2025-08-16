import logging
from PyQt5.QtCore import QObject, pyqtSignal

class GuiLogger(logging.Handler, QObject):
    """
    A custom logging handler that emits a PyQt signal for each log record.
    This allows routing log messages to a GUI widget.
    """
    # Define a signal that carries the log message string
    message_written = pyqtSignal(str)

    def __init__(self):
        # Initialize both parent classes
        logging.Handler.__init__(self)
        QObject.__init__(self)

    def emit(self, record):
        """
        This method is called by the logging framework for each log record.
        It formats the record and emits the message_written signal.
        """
        log_entry = self.format(record)
        self.message_written.emit(log_entry)
