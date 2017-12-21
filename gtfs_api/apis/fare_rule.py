from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import FareRule

fare_attr_namespace = Namespace('fare_attr', description='')
fare_rule_namespace = Namespace('fare_rule', description='料金に関するAPI')

fare_attribute = fare_attr_namespace.model('FareAttribute', {
    'id': fields.String(required=True, description='', example=''),
    'price': fields.Integer(required=True, description='料金', example=''),
    'currency_type': fields.String(required=True, description='通貨単位', example=''),
    'payment_method': fields.Integer(required=True, description='支払いタイミング', example=''),
    'transfers': fields.Integer(required=True, description='乗り換え', example=''),
    'transfer_duration': fields.Integer(required=False, description='乗り換え有効期限', example='')
})

fare_rule = fare_rule_namespace.model('FareRule', {
    'attribute': fields.Nested(fare_attribute),
    'route_id': fields.String(required=True, description='', example=''),
    'origin_id': fields.String(required=False, description='', example=''),
    'destination_id': fields.String(required=False, description='', example=''),
    'contains_id': fields.String(required=False, description='', example='')
})


@fare_rule_namespace.route('/<route_id>')
class Fare(Resource):
    @fare_rule_namespace.marshal_list_with(fare_rule)
    def get(self, route_id):
        return FareRule.query.filter(FareRule.route_id == route_id).all()
