from logging.handlers import SocketHandler


class DjangoElkHandler(SocketHandler):
    def emit(self, record):
        if hasattr(record, "request"):
            record.request = None
        return super().emit(record)
