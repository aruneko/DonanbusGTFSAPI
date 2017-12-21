from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import Trip

trip_namespace = Namespace('trips', description='便情報エンドポイント')

trip = trip_namespace.model('Trip', {
    'route_id': fields.String(required=True, description='経路ID'),
    'service_id': fields.String(required=True, description='運行日ID'),
    'id': fields.String(required=True, description='便ID'),
    'headsign': fields.String(description='便行先'),
    'short_name': fields.String(description='便名称'),
    'direction_id': fields.Integer(description='上下区分'),
    'block_id': fields.String(description='便結合区分'),
    'shape_id': fields.String(description='描画ID'),
    'wheelchair_accessible': fields.Integer(description='車椅子利用区分'),
    'bikes_allowed': fields.Integer(description='自転車持ち込み区分'),
    'desc': fields.String(description='便情報'),
    'desc_symbol': fields.String(description='便記号'),
    'office_id': fields.String(description='営業所ID')
})


@trip_namespace.route('/')
class TripList(Resource):
    @trip_namespace.marshal_list_with(trip)
    def get(self):
        """
        便情報一覧
        """
        return Trip.query.all()


@trip_namespace.route('/<trip_id>')
class TripController(Resource):
    @trip_namespace.marshal_with(trip)
    def get(self, trip_id):
        """
        便情報詳細
        """
        return Trip.query.filter(Trip.id == trip_id).first_or_404()
