from flask_restplus import fields, Namespace, Resource

from gtfs_api.models import FareRule

fare_rule_namespace = Namespace('fare_rule', description='料金に関するAPI')

fare_rule = fare_rule_namespace.model('FareRule', {
    'id': fields.String(required=True, description='', example=''),
    'route_id': fields.String(required=True, description='', example=''),
    'origin_id': fields.String(required=False, description='', example=''),
    'destination_id': fields.String(required=False, description='', example=''),
    'contains_id': fields.String(required=False, description='', example='')
})


@fare_rule_namespace.route('/<route_id>')
class FareRulesByRoute(Resource):
    @fare_rule_namespace.marshal_list_with(fare_rule)
    def get(self, route_id):
        return FareRule.query.filter(FareRule.route_id == route_id).all()


@fare_rule_namespace.route('/<route_id>/<origin_id>')
class FareRulesByRouteAndOrigin(Resource):
    @fare_rule_namespace.marshal_list_with(fare_rule)
    def get(self, route_id, origin_id):
        return FareRule.query\
            .filter(FareRule.route_id == route_id)\
            .filter(FareRule.origin_id == origin_id)\
            .all()


@fare_rule_namespace.route('/<route_id>/<origin_id>/<destination_id>')
class DestinationFareRule(Resource):
    @fare_rule_namespace.marshal_with(fare_rule)
    def get(self, route_id, origin_id, destination_id):
        return FareRule.query\
            .filter(FareRule.route_id == route_id)\
            .filter(FareRule.origin_id == origin_id)\
            .filter(FareRule.destination_id == destination_id)\
            .first_or_404()
