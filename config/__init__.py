"""
Config initialization and Python 3.14+ compatibility patches for Django.
"""
import sys

# PyMySQL setup for MySQL without mysqlclient C library
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

# Python 3.14+ compatibility patch for Django Context.__copy__
if sys.version_info >= (3, 14):
    from django.template import context as django_context

    def _python314_context_copy(self):
        duplicate = object.__new__(self.__class__)
        duplicate.__dict__.update(self.__dict__)
        duplicate.dicts = self.dicts[:]
        return duplicate

    django_context.Context.__copy__ = _python314_context_copy
