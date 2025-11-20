import os
import shutil
import threading

def copy_tree(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    items = os.listdir(source) #['folder1', 'folder2', 'file1', 'file2']

    for item in items:
        if os.path.isfile(item):
            shutil.copy(f"{source}/{item}", f"{dest}/{item}")
        if os.path.isdir(item):
            copy_tree(f"{source}/{item}", f"{dest}/{item}")

source, dest = "./static/", "./public/"
if not os.path.exists(source):
    raise Exception("Source path not found")

copy_tree(source, dest)
os.listdir(dest)


# https://pyquesthub.com/creating-a-custom-logging-library-in-python-a-step-by-step-guide
# Define log levels
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

class CustomLogger:
    def __init__(self, name='CustomLogger', level='DEBUG', log_file=None):
        self.name = name
        self.level = LOG_LEVELS[level]
        self.lock = threading.Lock()  # Ensure thread safety
        self.log_file = log_file

    def log(self, level, message):
        if LOG_LEVELS[level] >= self.level:
            log_message = f'{level}: {self.name} - {message}'
            self._write_log(log_message)

    def _write_log(self, log_message):
        with self.lock:
            print(log_message)  # Print to console
            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(log_message + '\n')

    def debug(self, message):
        self.log('DEBUG', message)
        
    def info(self, message):
        self.log('INFO', message)

    def warning(self, message):
        self.log('WARNING', message)

    def error(self, message):
        self.log('ERROR', message)

    def critical(self, message):
        self.log('CRITICAL', message)

# Example usage
if __name__ == '__main__':
    logger = CustomLogger(level='INFO', log_file='app.log')

    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')
