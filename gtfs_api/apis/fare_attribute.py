from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import FareAttribute

fare_attribute_namespace = Namespace('fare_attributes', description='料金属性に関するエンドポイント')

fare_attribute = fare_attribute_namespace.model('FareAttribute', {
    'id': fields.String(required=True, description='運賃ID', example='k_210'),
    'price': fields.Integer(required=True, description='運賃', example='210'),
    'currency_type': fields.String(required=True, description='通貨単位', example='JPY'),
    'payment_method': fields.Integer(required=True, description='支払いタイミング', example='0'),
    'transfers': fields.Integer(required=True, description='乗り換え', example='0'),
    'transfer_duration': fields.Integer(required=False, description='乗り換え有効期限', example='')
})


@fare_attribute_namespace.route('/<fare_id>')
class FareAttributeController(Resource):
    @fare_attribute_namespace.marshal_with(fare_attribute)
    def get(self, fare_id):
        """
        料金属性詳細
        """
        return FareAttribute.query.filter(FareAttribute.id == fare_id).first_or_404()
