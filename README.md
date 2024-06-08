# Web Scraping Projects

Welcome to my Web Scraping Projects repository. This repository contains various web scraping projects developed using Python and Scrapy. Each project is designed to scrape data from different websites and save it in a structured format.

## Table of Contents

- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Projects

1. **Crypto Prices Scraper**
   - Scrapes cryptocurrency prices from [crypto.com](https://crypto.com/price).
   - Saves data including name, price, 24-hour change, 24-hour volume, and market cap.

2. **Amazon Product Scraper**
   - Scrapes product details from Amazon.
   - Saves data including product name, price, rating, and reviews.

3. **Cars Listing Scraper**
   - Scrapes car listings from various car dealer websites.
   - Saves data including car model, price, year, and mileage.

## web_scraping_projects Structure
│
├── amazon/
│   ├── amazon/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── __init__.py
│   │       └── amazon_spider.py
│   ├── scrapy.cfg
│   └── output.csv
│


├── cars/
│   ├── cars/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── __init__.py
│   │       └── cars_spider.py
│   ├── scrapy.cfg
│   └── output.csv
│


├── crypto/
│   ├── crypto/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── __init__.py
│   │       └── crypto_spider.py
│   ├── scrapy.cfg
│   └── output.csv
│
├── requirements.txt
└── README.md
