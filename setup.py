#!/usr/bin/env python

from distutils.core import setup

import sys, os

sys.path.insert(0, os.path.join('src', 'CassandraLibrary'))


def main():
    setup(name='robotframework-cassandralibrary',
          description='Cassandra library for Robot Framework',
          author='Yong Joon Park',
          author_email='pyj1952@gmail.com',
          package_dir={'': 'src'},
          packages=['CassandraLibrary'],
          )


if __name__ == "__main__":
    main()
