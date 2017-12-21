from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import Stop

stop_namespace = Namespace('stops', description='バス停情報エンドポイント')

stop = stop_namespace.model('Stop', {
    'id': fields.String(required=True, description='バス停ID', example='0211_B'),
    'code': fields.String(description='バス停ナンバリング番号', example=''),
    'name': fields.String(required=True, description='バス停名称', example='東町ターミナル'),
    'desc': fields.String(description='バス亭付加情報', example='のりば1・2'),
    'lat': fields.Float(required=True, description='緯度', example='42.3444779'),
    'lon': fields.Float(required=True, description='経度', example='141.0296731'),
    'zone_id': fields.String(description='運賃エリアID', example='0211_B'),
    'url': fields.String(description='バス亭URL', example=''),
    'location_type': fields.Integer(description='バス停区分', example='0'),
    'parent_statioin': fields.String(description='親バス停情報', example=',0211'),
    'timezone': fields.String(description='タイムゾーン', example=None),
    'wheelchair_boarding': fields.Integer(description='車椅子情報', example=None),
})


@stop_namespace.route('/')
class StopsList(Resource):
    @stop_namespace.marshal_list_with(stop)
    def get(self):
        """
        バス停情報一覧
        """
        return Stop.query.all()


@stop_namespace.route('/<stop_id>')
class StopController(Resource):
    @stop_namespace.marshal_with(stop)
    def get(self, stop_id):
        """
        バス停情報詳細
        """
        return Stop.query.filter(Stop.id == stop_id).first_or_404()
