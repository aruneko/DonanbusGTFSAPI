from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import FareRule

fare_rule_namespace = Namespace('fare_rule', description='料金に関するエンドポイント')

fare_rule = fare_rule_namespace.model('FareRule', {
    'id': fields.String(required=True, description='運賃ID', example='k_210'),
    'route_id': fields.String(required=True, description='系統ID', example='131700'),
    'origin_id': fields.String(required=False, description='乗車地ゾーン', example='0189_A'),
    'destination_id': fields.String(required=False, description='降車地ゾーン', example='0371_A'),
    'contains_id': fields.String(required=False, description='通過ゾーン', example='')
})


@fare_rule_namespace.route('/<route_id>')
class FareRulesByRoute(Resource):
    @fare_rule_namespace.marshal_list_with(fare_rule)
    def get(self, route_id):
        """
        ルート毎の料金一覧
        """
        return FareRule.query.filter(FareRule.route_id == route_id).all()


@fare_rule_namespace.route('/<route_id>/<origin_id>')
class FareRulesByRouteAndOrigin(Resource):
    @fare_rule_namespace.marshal_list_with(fare_rule)
    def get(self, route_id, origin_id):
        """
        乗車地からの料金一覧
        """
        return FareRule.query\
            .filter(FareRule.route_id == route_id)\
            .filter(FareRule.origin_id == origin_id)\
            .all()


@fare_rule_namespace.route('/<route_id>/<origin_id>/<destination_id>')
class DestinationFareRule(Resource):
    @fare_rule_namespace.marshal_with(fare_rule)
    def get(self, route_id, origin_id, destination_id):
        """
        乗車地から降車地までの料金
        """
        return FareRule.query\
            .filter(FareRule.route_id == route_id)\
            .filter(FareRule.origin_id == origin_id)\
            .filter(FareRule.destination_id == destination_id)\
            .first_or_404()
