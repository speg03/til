# %%
import urllib.request

from bs4 import BeautifulSoup

# %%
url = "https://www.yodobashi.com/product-detail/100000001006328319/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

# %%
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    the_page: bytes = response.read()

# %%
html_doc = the_page.decode("utf-8")

# %%
soup = BeautifulSoup(html_doc, "html.parser")
sales_info = soup.find(id="productDetail").find_all("div", class_="salesInfo")
sales_info[0].get_text() if sales_info else "N/A"


# %%
def sales_info(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        the_page: bytes = response.read()

    html_doc = the_page.decode("utf-8")

    soup = BeautifulSoup(html_doc, "html.parser")
    sales_info = soup.find(id="productDetail").find_all("div", class_="salesInfo")

    return sales_info[0].get_text() if sales_info else "N/A"


# %%
sales_info("https://www.yodobashi.com/product-detail/100000001006328319/")
# => '予定数の販売を終了しました'

# %%
sales_info("https://www.yodobashi.com/product/100000001006319898/")
# => 'N/A'

# %%
sales_info("https://www.yodobashi.com/product-detail/100000001006345135/")
# => '販売を終了しました'
