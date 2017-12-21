from flask_restplus import Namespace, fields, Resource

from gtfs_api.models import Route

route_namespace = Namespace('routes', description='経路情報エンドポイント')

route = route_namespace.model('Route', {
    'id': fields.String(required=True, description='経路ID', example='131700'),
    'agency_id': fields.String(required=True, description='事業者ID', example='1430001056880'),
    'short_name': fields.String(required=True, description='経路略称', example=''),
    'long_name': fields.String(
        required=True,
        description='経路名',
        example='6: ろう学校線 (室蘭ろう学校前〜工大〜高砂2丁目〜東室蘭駅西口〜東町ターミナル)'
    ),
    'desc': fields.String(required=False, description='経路情報', example=''),
    'type': fields.Integer(required=True, description='経路タイプ', example='3'),
    'url': fields.String(required=False, description='経路URL', example=''),
    'color': fields.String(required=False, description='経路色', example=''),
    'text_color': fields.String(required=False, description='経路文字色', example=''),
    'jp_parent_station_id': fields.String(required=False, description='親路線ID', example='')
})


@route_namespace.route('/')
class RouteList(Resource):
    @route_namespace.marshal_list_with(route)
    def get(self):
        """
        経路一覧
        """
        return Route.query.all()


@route_namespace.route('/<route_id>')
class RouteController(Resource):
    @route_namespace.marshal_with(route)
    def get(self, route_id):
        """
        経路情報詳細
        """
        return Route.query.filter(Route.id == route_id).first_or_404()
