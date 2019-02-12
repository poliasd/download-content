# A program downloading the content from a specific web site for further analysis.

Running the application:

```
pip install pipenv
pip install -r requirements.txt
python DownloadContent.py
```

The function download_site(url, level) contains the following parameters

1. url - the URL of a specific web site page 
2. level - the number of levels to download. 

#### Example
```
download_site https://www.cnn.com 2
```
