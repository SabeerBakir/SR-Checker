from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def sr_get(battletag):
    battletag = battletag.replace("#", "-")
    link = "https://playoverwatch.com/en-gb/career/pc/" + battletag
    content = simple_get(link)
    temp = str(content)
    searchObj1 = re.search(r'<div class="u-align-center h5">\d\d\d\d</div>', temp)
    searchObj2 = re.search(r'<p class="NotificationBar-text">THIS PROFILE IS CURRENTLY PRIVATE</p>', temp)
    searchObj3 = re.search(r'<h1 class="u-align-center">Profile Not Found</h1>', temp)


def battlefly_battletags(link):
    content = simple_get(link)
    temp = str(content)
    print(temp)


battlefly_battletags("https://battlefy.com/teams/5ba2bd21c19c1c0564d99643")
