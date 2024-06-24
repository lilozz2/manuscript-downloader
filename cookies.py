from pathlib import Path
import json
import requests

# to save cookies:
def save_cookies():
    session = requests.session()
    session.get("https://www.biblegateway.com")  # get some cookies
    print(session.cookies.get_dict())
    cookies = requests.utils.dict_from_cookiejar(session.cookies)  # turn cookiejar into dict
    Path("cookies.json").write_text(json.dumps(cookies))  # save them to file as JSON

# to retrieve cookies:
def retrieve_cookies():
    cookies = json.loads(Path("cookies.json").read_text())  # save them to file as JSON
    cookies = requests.utils.cookiejar_from_dict(cookies)  # turn dict to cookiejar
    return cookies

import http.cookiejar
import urllib.request

# Create a cookie jar object to hold the cookies
cookie_jar = http.cookiejar.CookieJar()

# Create an opener to handle cookies, redirects, etc.
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# Use the opener to fetch a web page that sets cookies
response = opener.open('https://www.biblegateway.com/passage/?search=2%20Samuel%201&version=KJV&interface=print')

# The cookie jar will automatically capture and store the cookies
print(cookie_jar.__dict__)
