# -*- coding: utf-8 -*-
"""
    Normal settings file for Eve.

    Differently from a configuration file for an Eve application backed by Mongo
    we need to define the schema using the registerSchema decorator.

"""
from eve.io.sql.decorators import registerSchema
from tables import People, Invoices

registerSchema('people')(People)
registerSchema('invoices')(Invoices)

SQLALCHEMY_DATABASE_URI = 'sqlite://'

# The following two lines will output the SQL statements executed by SQLAlchemy. Useful while debugging
# and in development. Turned off by default
# --------
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

DEBUG = True

# The default schema is generated by the decorator
DOMAIN = {
    'people': People._eve_schema['people'],
    'invoices': Invoices._eve_schema['invoices']
    }

# but you can always customize it:
DOMAIN['people'].update({
    'item_title': 'person',
    'additional_lookup': {
        'url': '[0-9]+',
        'field': 'id'
        },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE']
    })
