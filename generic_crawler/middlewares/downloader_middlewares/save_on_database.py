import re
import logging
from ...services.DatabaseService import DatabaseService
from ...settings import TARGET_DIR

class SaveOnDatabaseMiddleware(object):
    def process_response(self, request, response, spider):
        database = DatabaseService.get_instance()
        label = TARGET_DIR.split('/')[-1]
        url = response.url
        html = response.body
        database.save_html(label=label, url=url, html=html)

        return response
