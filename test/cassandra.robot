*** Settings ***
Library           CassandraLibrary
Library           csvlibrary.py

*** Test Cases ***
Test1
    CassandraLibrary.Connect To Cassandra    test_keyspace    127.0.0.1
    @{res}    CassandraLibrary.Query    Select * from test_keyspace.test_table_ex1;
    LOG MANY    @{res}
    Write CSV File    ${CURDIR}/cassandra_test_keyspace    @{res}
    CassandraLibrary.Disconnect From Cassandra

Test2
    CassandraLibrary.Connect To Cassandra    test_keyspace    127.0.0.1
    @{res}    CassandraLibrary.Query    CREATE TABLE test_keyspace.test_table_ex1 (code text, location text, sequence text, description text,PRIMARY KEY (code, location));
    @{res}    CassandraLibrary.Query    INSERT INTO test_keyspace.test_table_ex1 (code, location, sequence, description ) VALUES ('N1', 'Seoul', 'first', 'AA');
    @{res}    CassandraLibrary.Query    INSERT INTO test_keyspace.test_table_ex1 (code, location, sequence, description ) VALUES ('N1', 'Gangnam', 'second', 'BB');
    @{res}    CassandraLibrary.Query    INSERT INTO test_keyspace.test_table_ex1 (code, location, sequence, description ) VALUES ('N2', 'Seongnam', 'third', 'CC');
    @{res}    CassandraLibrary.Query    INSERT INTO test_keyspace.test_table_ex1 (code, location, sequence, description ) VALUES ('N2', 'Pangyo', 'fourth', 'DD');
    @{res}    CassandraLibrary.Query    INSERT INTO test_keyspace.test_table_ex1 (code, location, sequence, description ) VALUES ('N2', 'Jungja', 'fifth', 'EE');
    @{res}    CassandraLibrary.Query    Select * from test_keyspace.test_table_ex1;
    CassandraLibrary.Disconnect From Cassandra
    Write CSV File    ${CURDIR}/cassandra_test_keyspace    @{res}
    log many    @{res}
