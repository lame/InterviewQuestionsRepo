import os
import unittest
from flask.ext.testing import TestCase

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from app import app
from models.connect_to_cluster import Conn
from models.vehicle_by_serial_number import VehicleBySerialNumber
from utils.data.csv_reader import CSVReader


class TestVsnResults(TestCase):

    def create_app(self):
        Conn()
        self.client = app.test_client()
        return app

    def setUp(self):
        vsn = [['ABCD*V000000', '000001', '2015', 'Test1', 'test1', 'Premium Package'],
               ['ABCD*V******', '000002', '2015', 'Test2', 'test2', 'Pleb Package'],
               ['ABCD*V******', '000003', '2015', 'Test3', 'test3', 'Limited Sahara Durango']]
        for row in vsn:
            CSVReader.populate_vehicle_by_serial_number(None, row)

    def tearDown(self):
        VehicleBySerialNumber(prefix='ABCD', remainder='*V000000', vehicle_trim='000001').delete()
        VehicleBySerialNumber(prefix='ABCD', remainder='*V******', vehicle_trim='000002').delete()
        VehicleBySerialNumber(prefix='ABCD', remainder='*V******', vehicle_trim='000003').delete()

    def query_vsn(self, vsn):
        result = self.client.get('/api/vsn/{0}'.format(vsn))
        return result

    def test_no_result(self):
        result = self.query_vsn('x')  # This should not match any VSN
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json), 0)

    def test_results(self):
        result = self.query_vsn('ABCDEV000000')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json), 1)
        self.assertEqual(result.json[0]['serial_number'],  'ABCD*V000000')
        self.assertEqual(result.json[0]['vehicle_trim'], 1)
        self.assertEqual(result.json[0]['year'], 2015)
        self.assertEqual(result.json[0]['make'], 'Test1')
        self.assertEqual(result.json[0]['model'], 'test1')
        self.assertEqual(result.json[0]['trim_name'], 'Premium Package')

    def test_not_include(self):
        lst = []
        results = self.query_vsn('ABCDEV000001')

        for result in results.json:
            lst.append(result['serial_number'])

        self.assertFalse("ABCD*V000000" in lst)
        self.assertEqual(len(results.json), 2)
        self.assertEqual(results.json[0]['serial_number'],  'ABCD*V******')
        self.assertEqual(results.json[1]['serial_number'],  'ABCD*V******')

if __name__ == '__main__':
    unittest.main()
