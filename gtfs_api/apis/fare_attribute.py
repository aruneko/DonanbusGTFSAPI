from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import FareAttribute

fare_attribute_namespace = Namespace('fare_attributes', description='料金属性に関するエンドポイント')

fare_attribute = fare_attribute_namespace.model('FareAttribute', {
    'id': fields.String(required=True, description='', example=''),
    'price': fields.Integer(required=True, description='料金', example=''),
    'currency_type': fields.String(required=True, description='通貨単位', example=''),
    'payment_method': fields.Integer(required=True, description='支払いタイミング', example=''),
    'transfers': fields.Integer(required=True, description='乗り換え', example=''),
    'transfer_duration': fields.Integer(required=False, description='乗り換え有効期限', example='')
})


@fare_attribute_namespace.route('/<fare_id>')
class FareAttributeController(Resource):
    @fare_attribute_namespace.marshal_with(fare_attribute)
    def get(self, fare_id):
        return FareAttribute.query.filter(FareAttribute.id == fare_id).first_or_404()
