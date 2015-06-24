from cassandra.cluster import Cluster
from config import cassandra_cluster_ip, cassandra_default_keyspace
from difflib import SequenceMatcher
from flask.ext.restful import Resource
from fnmatch import fnmatch


class VSMResource(Resource):

    def __init__(self):
        cluster = Cluster([cassandra_cluster_ip])
        self.session = cluster.connect(cassandra_default_keyspace)
        self.get_all_info = self.session.prepare('SELECT * FROM vehicle_by_serial_number\
                                                 WHERE prefix = ?')

    def get(self, vsn):
        vsn_prefix = vsn[:4]
        vsn_remainder = vsn[4:]

        result_list = [(0, None, None)]

        results = self.session.execute(self.get_all_info, (vsn_prefix, ))

        for result in results:
            if fnmatch(vsn_remainder, result.remainder.replace('*', '?')):
                ratio = SequenceMatcher(None, result.remainder, vsn_remainder).quick_ratio()
                if ratio == result_list[0][0]:
                    # if the set has the correct max
                    result_list.append((ratio, result.serial_number, result.vehicle_trim,
                                       result.year, result.make, result.model, result.trim_name))
                elif ratio > result_list[0][0]:
                    # this number is the new max, start new count
                    result_list = [(ratio, result.serial_number, result.vehicle_trim,
                                    result.year, result.make, result.model, result.trim_name)]
        dict_list = []
        for result in result_list:
            dict_list.append({
                                'ratio': result[0],
                                'serial_number': result[1],
                                'vehicle_trim': result[2],
                                'year': result[3],
                                'make': result[4],
                                'model': result[5],
                                'trim_name': result[6]
                             })
        return dict_list
