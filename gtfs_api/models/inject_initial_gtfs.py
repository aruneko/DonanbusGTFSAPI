from typing import List

from flask import Flask

from gtfs_api.models import Agency, db, Stop


def read_csv(file_name: str) -> List[List[str]]:
    with open('gtfs/' + file_name, 'r') as f:
        lines = f.readlines()[1:]
        return [line[:-1].split(',') for line in lines]


def add_agency(flask_app: Flask) -> None:
    with flask_app.app_context():
        if len(Agency.query.all()) == 0:
            agency_file = read_csv('agency.txt')
            agencies = [Agency(*agency) for agency in agency_file]
            for agency in agencies:
                db.session.add(agency)
            db.session.commit()


def add_stops(flask_app: Flask) -> None:
    with flask_app.app_context():
        if len(Stop.query.all()) == 0:
            stops_file = read_csv('stops.txt')
            stops = [Stop(*stop) for stop in stops_file]
            for stop in stops:
                db.session.add(stop)
            db.session.commit()


def init_db(flask_app: Flask) -> None:
    add_agency(flask_app)
    add_stops(flask_app)
