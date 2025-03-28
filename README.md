# Web Scraper with Translation

## Overview
This project is a web scraper that extracts news article details from **TribunNews** and translates the content into English using **Google Translate**.

## Features
- Scrapes the **title, date, author, and body** from a given news article URL.
- Translates the extracted content from Indonesian to English.
- Ensures accurate extraction of article content by refining the scraping logic.

## Requirements
Make sure you have **Python 3.x** installed. You also need the following dependencies:

```sh
pip install requests
pip install bs4
pip install googletrans==4.0.0-rc1
```

## Usage
1. Clone this repository or create a new Python script.
2. Install the required dependencies.
3. Update the `url` variable with the desired news article link.
4. Run the script:

```sh
python scraper.py
```

## Code Breakdown
- **Extracting Data:**
  - Uses `requests` to fetch the webpage.
  - Parses HTML using `BeautifulSoup`.
  - Retrieves article details (title, date, author, and content).
- **Translation:**
  - Uses `googletrans` to translate extracted content into English.
- **Refining Extraction:**
  - Improves accuracy by filtering out unnecessary text before translation.

## Example Output
```sh
Title: GoPay Supports the Eradication of Online Gambling in Indonesia Through Technology and Education
Date: August 7, 2024
Author: John Doe
Content: GoPay is actively involved in combating online gambling...
```

## Notes
- This script is designed for **TribunNews** and may require modifications for other websites.
- Google Translate API may have rate limits.
- If Google Translate does not work, try `pip install googletrans==4.0.0-rc1`.

## License
This project is open-source and free to use. Modify it as needed!
