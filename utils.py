import datetime
import os
import re
import sys


def get_file(file_name):
    return os.path.join(sys.path[0], file_name)


def get_time():
    return datetime.datetime.today()


def strip_non_alphanumeric_chars(text):
    return re.sub(r'\W+', '', text)


def init_log_file(log_file):
    sys.stdout = log_file
