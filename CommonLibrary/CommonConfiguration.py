# -*- coding: utf-8 -*-

from datetime import datetime
import time
import os


def driver_path():
    return r'E:\lulu.wu\shared\geckodriver.exe'


# change time to str
def get_current_time():
    form = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(form)


def result_path():
    path = r'E:\soft\webtest\TestResult' + '\\' + 'TestRun_' + datetime.now().strftime('%y%m%d')
    if not os.path.isdir(path):
        os.mkdir(path)
    return path


# Get time diff
def time_diff(start_time, end_time):
    form = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(end_time, form) - datetime.strptime(start_time, form)

def pic_path():
    return '..\\TestResult\\screenshot\\' + now + '.png'


if __name__ == '__main__':
    print(get_identify_code('automation'))
