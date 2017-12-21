from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import Agency

agency_namespace = Namespace('agency', description='事業者情報エンドポイント')

agency = agency_namespace.model('Agency', {
    'id': fields.String(required=True, description='事業者ID', example='1430001056880'),
    'name': fields.String(required=True, description='事業者名称', example='道南バス株式会社'),
    'url': fields.String(required=True, description='事業者URL', example='http://donanbus.co.jp/'),
    'timezone': fields.String(required=True, description='タイムゾーン', example='Asia/Tokyo'),
    'lang': fields.String(required=False, description='言語', example='ja'),
    'phone': fields.String(required=False, description='電話番号', example='0143-45-2131'),
    'fare_url': fields.String(required=False, description='オンラインチケット購入URL', example='http://bus.example.com/'),
    'email': fields.String(required=False, description='メールアドレス', example='bus@example.com')
})


@agency_namespace.route('/')
class AgencyList(Resource):
    @agency_namespace.marshal_list_with(agency)
    def get(self):
        """
        一覧取得
        """
        return Agency.query.all()


@agency_namespace.route('/<string:agency_id>')
class AgencyController(Resource):
    @agency_namespace.marshal_with(agency)
    def get(self, agency_id):
        """
        個別取得
        """
        return Agency.query.filter(Agency.id == agency_id).first()
