from flask_restplus import Api

from gtfs_api.apis.agency import agency_namespace
from gtfs_api.apis.fare_attributes import fare_attribute_namespace
from gtfs_api.apis.fare_rules import fare_rule_namespace
from gtfs_api.apis.routes import route_namespace
from gtfs_api.apis.stop_times import stop_time_namespace
from gtfs_api.apis.stops import stop_namespace
from gtfs_api.apis.trips import trip_namespace

api = Api(
    title='Donanbus GTFS API',
    version='1.0',
    description='道南バスの時刻表データをGTFS形式に沿って提供するAPI'
)

api.add_namespace(agency_namespace)
api.add_namespace(stop_namespace)
api.add_namespace(route_namespace)
api.add_namespace(trip_namespace)
api.add_namespace(fare_attribute_namespace)
api.add_namespace(fare_rule_namespace)
api.add_namespace(stop_time_namespace)
