import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from helpers.logging1 import logger_module

logger = logger_module()


def create_dataframe():
    return pd.DataFrame(columns=['title', 'price'], index=[])


def get_url(i):
    return f'https://books.toscrape.com/catalogue/page-{i}.html'


def get_soup(url):
    ua = UserAgent()
    useragent = ua.random
    headers = {"user-agent": useragent}
    # logger.info(f'got header {useragent}')
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'html.parser')
    return soup


def add_to_df(df: pd.DataFrame, result: dict):
    return df._append(result, ignore_index=True)


if __name__ == '__main__':
    pass
