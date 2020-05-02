TikTok Video Scraper
===
Script ini merupakan pengembangan dari [Tiktok Scraper](https://github.com/joeyism/tiktok-scraper) yang dibikin Joeyism. Saya memperbaharui metode perpindahan video dan juga tidak lagi hanya menscrape username


Requirements
---
- Python 3
- selenium
- chromedriver/geckodriver
- python-requests

Installation
---
- `git clone https://github.com/lantip/ttscraper.git`
- `cd ttscraper`
- Jika belum punya pipenv, jalankan `pip install pipenv`
- Jalankan `pipenv install`

Usage
---
```
usage: python cli.py [-h] [--driver DRIVER] [--driver-type DRIVER_TYPE]
                      [--show-browser] [--delay DELAY] [--location LOCATION]
                      username
positional arguments:
  username              username tiktok atau tag

optional arguments:
  -h, --help            show this help message and exit
  --driver DRIVER       Driver location
  --driver-type DRIVER_TYPE
                        Type of driver (i.e. Chrome)
  --show-browser        Shows browser while scraping. Useful for debugging
  --delay DELAY         Number of seconds to delay between video downloading
  --location LOCATION   Location to store the files
  --tipe                tag atau username, defaultnya username
```

Thanks To
---
- Joeyism

Contoh
---
```
$ python cli.py kimnevri

$ python cli.py pahlawangardadepan --tipe=tag
```