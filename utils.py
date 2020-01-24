import logging
from logging import FileHandler, StreamHandler, Formatter
from datetime import date, timedelta

import config

LOG_DIR = config.LOG_DIR
LOG_LV_MAPPER = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

def get_dates(start_date, end_date):
    y_start, m_start, d_start = start_date.split('-')
    y_end, m_end, d_end = end_date.split('-')

    d1 = date(int(y_start), int(m_start), int(d_start))  # start date
    d2 = date(int(y_end), int(m_end), int(d_end))  # end date
    delta = d2 - d1  # timedelta

    date_list = [str(d1 + timedelta(i)) for i in range(delta.days + 1)]
    return date_list


def get_logger(name, fh_lv='debug', ch_lv='error', logger_lv='debug'):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LV_MAPPER[logger_lv])  # set log level of logger

    fh = FileHandler(LOG_DIR + '/' + name + '.log')  
    ch = StreamHandler()
    formatter = Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    fh.setLevel(LOG_LV_MAPPER[fh_lv])  # set log level of filehandler
    ch.setLevel(LOG_LV_MAPPER[ch_lv])
    logger.addHandler(fh)  # set log level of streamhandler
    logger.addHandler(ch)
    return logger


def get_jyutping_from_api(char):
    import requests
    from bs4 import BeautifulSoup
    
    base_url = 'https://jyut.net/query'
    data = '?q=' + char
    endpoint = base_url + data
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.find('span', class_='jyutping')

    return tag.string

