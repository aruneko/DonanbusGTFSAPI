from flask_restplus import Api

from gtfs_api.apis.agency import agency_namespace
from gtfs_api.apis.routes import route_namespace
from gtfs_api.apis.stops import stop_namespace

api = Api(
    title='Donanbus GTFS API',
    version='1.0',
    description='道南バスの時刻表データをGTFS形式に沿って提供するAPI'
)

api.add_namespace(agency_namespace)
api.add_namespace(stop_namespace)
api.add_namespace(route_namespace)
