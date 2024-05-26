import sys


# Sample logger
class LoggerWriter:
    """
    Example Logger Writer:
    Takes all output from stdout and stderr and prints them on stdout's console. Not required by flask.
    """

    def __init__(self, log_name):
        self.log_name = log_name
        self.buf = []

    def write(self, msg):
        msg = msg.replace("\n", '')
        if len(msg) > 0:
            self.buf.append(f"[{self.log_name}] " + msg)
            print(''.join(self.buf), file=sys.__stdout__, flush=True)
            self.buf = []

    def flush(self):
        self.buf = []
        pass


# Para acceder a stdout/stderr, usar sys.__stdout__/sys.__stderr__
# sys.stdout = LoggerWriter("INFO")
# sys.stderr = LoggerWriter("ERROR")
