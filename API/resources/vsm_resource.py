from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from config import cassandra_cluster_ip, cassandra_default_keyspace
from difflib import SequenceMatcher
from flask.ext.restful import Resource
from models.vsn_lookup import VSNLookup


class VSMResource(Resource):

    def __init__(self):
        cluster = Cluster([cassandra_cluster_ip])
        self.session = cluster.connect(cassandra_default_keyspace)
        self.get_vsn = self.session.prepare('SELECT remainder, vehicle_trim, serial_number\
                                            FROM vsn_lookup WHERE prefix=?')

    def get(self, vsn):
        vsn_prefix = vsn[:4]
        vsn_remainder = vsn[4:]

        results = self.session.execute(self.get_vsn, (vsn_prefix, ))

        return [(result.serial_number, result.vehicle_trim, SequenceMatcher(None, result.remainder, vsn_remainder).quick_ratio()) for result in results]
