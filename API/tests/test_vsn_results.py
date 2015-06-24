import os
import unittest
from flask.ext.testing import TestCase

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from app import app
from models.connect_to_cluster import Conn


class TestVsnResults(TestCase):

    def create_app(self):
        Conn()
        self.client = app.test_client()
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def query_vsn(self, vsn):
        result = self.client.get('/api/vsn/{0}'.format(vsn))
        return result

    def test_no_result(self):
        result = self.query_vsn('x')  # This should not match any VSN
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json), 0)

    def test_results(self):
        result = self.query_vsn('ZJTERV000000')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json), 1)
        self.assertEqual(result.json[0]['serial_number'],  "ZJTE*V000000")

    def test_not_include(self):
        lst = []
        results = self.query_vsn('ZJTERV000001')
        for result in results.json:
            lst.append(result['serial_number'])
        self.assertFalse("ZJTE*V000000" in lst)
        self.assertEqual(len(results.json), 5)

if __name__ == '__main__':
    unittest.main()
