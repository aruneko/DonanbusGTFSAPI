from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import Stop

stop_namespace = Namespace('stops', description='バス停情報API')

stop = stop_namespace.model('Stop', {
    'id': fields.String(),
    'code': fields.String(),
    'name': fields.String(),
    'desc': fields.String(),
    'lat': fields.Float(),
    'lon': fields.Float(),
    'zone_id': fields.String(),
    'url': fields.String(),
    'location_type': fields.Integer(),
    'parent_statioin': fields.String(),
    'timezone': fields.String(),
    'wheelchair_boarding': fields.Integer(),
})


@stop_namespace.route('/')
class StopsList(Resource):
    @stop_namespace.marshal_list_with(stop)
    def get(self):
        return Stop.query.all()
