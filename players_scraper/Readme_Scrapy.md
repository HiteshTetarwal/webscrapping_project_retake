# Scrapy Web Scraping Project

This project demonstrates web scraping using Scrapy, a powerful web crawling framework in Python. The project focuses on scraping players titles and authors from a website and saving the data to a CSV file.

## Installation

1. Clone the project repository:

```shell
git clone https://github.com/HiteshTetarwal/webscrapping_project
```

2. Install Scrapy and other required dependencies:

```shell
pip install scrapy
```

## Usage

1. Customize the Scrapy spider to match your scraping requirements. Open the `playerss_spider.py` file and modify the `start_urls`, CSS selectors, and file paths according to your target website and data storage preferences.

2. Run the Scrapy spider using the following command:

```shell
scrapy crawl playerss
```

3. Monitor the console output for progress updates. The spider will visit each page specified in the `start_urls` list, extract the players titles and authors using the defined CSS selectors, and save the data to the specified CSV file.

4. Once the spider finishes scraping all pages, the extracted data will be stored in the CSV file.

## Approach

1. The Scrapy spider is defined as a subclass of `scrapy.Spider`.

2. The spider's `name` attribute is set to `'playerss'`, which is used to identify the spider when running the scraping command.

3. The `start_urls` attribute is set to a list of URLs to be scraped. In this case, the URLs are generated dynamically using a range of page numbers.

4. The `parse` method is implemented to handle the parsing of each web page. It uses CSS selectors to locate the players titles and authors on the page.

5. The extracted data is stored in a CSV file using the `csv` module. Each row in the CSV file represents a players with its title and author.

6. The spider follows the next page link using `response.follow` to scrape the subsequent pages. This enables scraping multiple pages automatically.

7. The spider employs a logging mechanism to record the elapsed time for each page. This provides visibility into the time taken for scraping each page.

## Extensibility

The Scrapy project can be extended and customized to suit your specific scraping needs. You can modify the spider to extract additional information from the web page or save the data in a different format.