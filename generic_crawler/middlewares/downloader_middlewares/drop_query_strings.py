import re
import logging
from urllib.parse import urljoin, urlparse
from ...settings import TARGET_DIR

def remove_query_strings(url):
    return urljoin(url, urlparse(url).path)

class DropQueryStringsMiddleware(object):
    def process_request(self, request, spider):
        original_url = request.url
        new_url = remove_query_strings(original_url)
        if original_url == new_url:
            return None
        with open("/".join([TARGET_DIR, 'url_with_query_strings.txt']), 'a+') as file:
            file.write("{}\n".format(request.url))
        return request.replace(url=new_url)