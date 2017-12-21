from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import StopTime, Stop

stop_time_namespace = Namespace('stop_time', description='通過時間に関するエンドポイント')

stop_time = stop_time_namespace.model('StopTime', {
    'trip_id': fields.String(require=True, description='', example=''),
    'arrival_time': fields.String(require=True, description='', example=''),
    'departure_time': fields.String(require=True, description='', example=''),
    'stop_id': fields.String(require=True, description='', example=''),
    'sequence': fields.Integer(require=True, description='', example=''),
    'headsign': fields.String(require=False, description='', example=''),
    'pickup_type': fields.Integer(require=False, description='', example=''),
    'drop_off_type': fields.Integer(require=False, description='', example=''),
    'shape_dist_traveled': fields.Float(require=False, description='', example=''),
    'timepoint': fields.Integer(require=False, description='', example='')
})


@stop_time_namespace.route('/<origin_stop_id>/<dest_stop_id>')
class SearchTrip(Resource):
    @stop_time_namespace.marshal_list_with(stop_time)
    def get(self, origin_stop_id, dest_stop_id):
        origin_stop_ids = [stop.id for stop in Stop.query.filter(Stop.parent_station == origin_stop_id).all()]
        origin_stop_times = StopTime.query.filter(StopTime.stop_id.in_(origin_stop_ids)).all()
        origin_trip_ids = [origin_stop_time.trip_id for origin_stop_time in origin_stop_times]

        dest_stop_ids = [stop.id for stop in Stop.query.filter(Stop.parent_station == dest_stop_id).all()]
        dest_stop_times = StopTime.query.filter(StopTime.stop_id.in_(dest_stop_ids)).all()
        dest_trip_ids = [dest_stop_time.trip_id for dest_stop_time in dest_stop_times]
        return origin_stop_times
