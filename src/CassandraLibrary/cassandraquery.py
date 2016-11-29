class CassandraQuery(object):
    """
    Query handles all the querying done by the Database Library. 
    """

    def query(self, selectStatement):
        """
        Uses the input `selectStatement` to query for the values that 
        """
        rows = self.session.execute(selectStatement)
        return rows
