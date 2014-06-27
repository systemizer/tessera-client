from tessera.model import *
import requests

class TesseraClient(object):
    def __init__(self, rooturi):
        if rooturi[-1] == '/':
            rooturi = rooturi[:-1]
        self.rooturi = rooturi

    def _get(self, path):
        return requests.get('{0}{1}'.format(self.rooturi, path)).json()

    def list_dashboards(self, tag=None):
        path = '/api/dashboard/'
        if tag:
            path = path + 'tagged/' + tag
        response = self._get(path)
        return response['dashboards']

    def list_tags(self):
        response = self._get('/api/tag/')
        return response['tags']

    def list_categories(self):
        response = self._get('/api/dashboard/category/')
        return response['categories']
