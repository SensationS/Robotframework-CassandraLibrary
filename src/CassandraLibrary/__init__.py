from cassandraquery import CassandraQuery
from cassandra_connection_manager import CassandraConnection

from version import VERSION


class CassandraLibrary(CassandraConnection, CassandraQuery):
    """
    Cassandra Library contains utilities meant for Robot Framework's usage.
    
    This can allow you to query your Cassadnra database after an action has been made to verify the results.
    References:
    
     + Cassandra driver 3.00 Documentation - http://datastax.github.io/python-driver/index.html
     
    Example Usage:
        | Connect To Cassandra | host | port |

    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
