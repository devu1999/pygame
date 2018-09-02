#!/usr/bin/python
# -*- coding: utf-8 -*-
import bs4
from bs4 import BeautifulSoup as soup
import csv
import requests
i = 1
filename = 'in_books.csv'
with open(filename, 'wb') as csvfile:
    spanwriter = csv.writer(csvfile, delimiter=';')

    spanwriter.writerow([
        'Name',
        'URL',
        'Author',
        'Price',
        'Number of Ratings',
        'Average Rating',
        ])

    my_url = 'https://www.amazon.in/gp/bestsellers/books/#' + str(i)
    uClient = requests.get(my_url)
    page_html = uClient.content

    while i <= 5:
        page_soup = soup(page_html, 'html.parser')
        containers = page_soup.find_all('div', class_='zg_itemWrapper')

        for container in containers:

            title_container = container.find_all('div',
                    class_='p13n-sc-truncate p13n-sc-line-clamp-1')
            if title_container == []:
                title = 'Not Available'
            else:
                title = title_container[0].text.strip()

            author_container = container.find_all('a',
                    class_='a-size-small a-link-child')
            if author_container == []:
                author = 'Not Available'
            else:
                author = author_container[0].text.strip()

            url_container = container.find_all('a',
                    class_='a-link-normal a-text-normal')
            if url_container == []:
                url = 'Not Available'
            else:
                url = url_container[0]['href'].strip()

            avg_rating_container = container.find_all('span',
                    class_='a-icon-alt')
            if avg_rating_container == []:
                avg_rating = 'Not Available'
            else:
                avg_rating = avg_rating_container[0].text.strip()

            # print avg_rating

            price_container = container.find_all('span',
                    class_='p13n-sc-price')
            if price_container == []:
                price = 'Not Available'
            else:
                price = price_container[0].text.strip()

            nop_container = container.find_all('a',
                    class_='a-size-small a-link-normal')
            if nop_container == []:
                nop = 'Not Avaiable'
            else:
                nop = nop_container[0].text.strip()

            spanwriter.writerow([
                title,
                url,
                author,
                price,
                nop,
                avg_rating,
                ])

        i += 1


            
