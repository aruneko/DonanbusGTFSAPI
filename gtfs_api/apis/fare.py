from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import FareAttribute, FareRule

fare_namespace = Namespace('fare', description='料金に関するAPI')

fare_rule = fare_namespace.models('FareRule', {
    'id': fields.String(required=True, description='', example=''),
    'route_id': fields.String(required=True, description='', example=''),
    'origin_id': fields.String(required=False, description='', example=''),
    'destination_id': fields.String(required=False, description='', example=''),
    'contains_id': fields.String(required=False, description='', example='')
})

fare_attribute = fare_namespace.models('FareAttribute', {
    'id': fields.String(required=True, description='', example=''),
    'price': fields.Integer(required=True, description='', example=''),
    'currency_type': fields.String(required=True, description='', example=''),
    'payment_method': fields.Integer(required=True, description='', example=''),
    'transfers': fields.Integer(required=True, description='', example=''),
    'transfer_duration': fields.Integer(required=False, description='', example='')
})