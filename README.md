## Description

This project scrapes book data from the Books to Scrape website ([https://books.toscrape.com/](https://books.toscrape.com/)) using Scrapy, a Python web scraping framework. It extracts information such as book titles, prices, categories, ratings, and availability.

## Features

- Automatically crawls the website's pages to discover books.
- Extracts key information from individual book pages.
- Stores the extracted data in a structured format (CSV).

## Technologies Used

- Python
- Scrapy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TalChemerinsky/scrapy-project
   ```
2. Install dependencies:
   ```bash
   cd scrapy-project
   pip install -r requirements.txt
   ```

## Usage

1. Run the spider:
   ```bash
   scrapy crawl bookspider
   ```
2. The scraped data will be saved in a csv file named `bookdata.csv` by default.
