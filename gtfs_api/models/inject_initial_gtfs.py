from typing import List

from flask import Flask

from gtfs_api.models import Agency, db, Stop, Route


def read_csv(file_name: str) -> List[List[str]]:
    with open('gtfs/' + file_name, 'r') as f:
        lines = f.readlines()[1:]
        return [line[:-1].split(',') for line in lines]


def add_agency(flask_app: Flask) -> None:
    with flask_app.app_context():
        if Agency.query.count() == 0:
            agency_file = read_csv('agency.txt')
            agencies = [Agency(*agency) for agency in agency_file]
            for agency in agencies:
                db.session.add(agency)
            db.session.commit()


def add_stops(flask_app: Flask) -> None:
    with flask_app.app_context():
        if Stop.query.count() == 0:
            stops_file = read_csv('stops.txt')
            stops = [Stop(*stop) for stop in stops_file]
            for stop in stops:
                db.session.add(stop)
            db.session.commit()


def add_routes(flask_app: Flask) -> None:
    with flask_app.app_context():
        if Route.query.count() == 0:
            routes_file = read_csv('routes.txt')
            routes = [Route(*route) for route in routes_file]
            for route in routes:
                db.session.add(route)
            db.session.commit()


def init_db(flask_app: Flask) -> None:
    add_agency(flask_app)
    add_stops(flask_app)
    add_routes(flask_app)
