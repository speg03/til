# %%
import urllib.request

# %%
url = "https://www.yodobashi.com/product-detail/100000001006328319/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

# %%
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    the_page: bytes = response.read()

# %%
html = the_page.decode("utf-8")
html
