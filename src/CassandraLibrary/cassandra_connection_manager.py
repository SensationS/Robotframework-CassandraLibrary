from cassandra.cluster import Cluster


class CassandraConnection(object):
    """
    Connection Manager handles the connection & disconnection to the database.
    """

    def __init__(self):
        """
        Initializes cluster and session to None.
        """
        self.cluster = None
        self.session = None

    def connect_to_cassandra(self, keyspaceName, hostslist=''):
        """
        Connect to Cassandra host
        For example:
        | Connect To Casssandra | # connect to the cassandra |
        """
        hosts = hostslist.replace(' ', '').split(',')
        # print hosts
        self.cluster = Cluster(hosts)
        self.session = self.cluster.connect(keyspaceName)

    def disconnect_from_cassandra(self):
        """
        Disconnects from the database.
        
        For example:
        | Disconnect From Cassandra | # disconnects from current connection to the database | 
        """
        self.cluster.shutdown()
