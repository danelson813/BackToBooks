from helpers.helpers import get_soup, add_to_df, get_url, create_dataframe
from helpers.logging1 import logger_module
import pandas as pd


logger = logger_module()
logger.info('logging has started')


def main(url: str, df2: pd.DataFrame):
    soup = get_soup(url)
    items = soup.find_all('article', class_='product_pod')
    # logger.info(f'There are {len(items)} items')

    for item in items:
        title = item.find('h3').find('a')['title']
        price = item.find('p', class_='price_color').text[2:]
        result = {'title': title, 'price': price}
        df2 = add_to_df(df2, result)
    return df2


if __name__ == '__main__':
    df = create_dataframe()
    for i in range(1, 51):
        url = get_url(i)
        df = main(url, df)

    df.to_csv('data/Results.csv', index=False)
