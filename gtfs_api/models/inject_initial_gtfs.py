from typing import List

from flask import Flask

from gtfs_api.models import Agency, db, Stop, Route, Calendar, CalendarDate, Shape, Office, Trip


def read_csv(file_name: str) -> List[List[str]]:
    with open('gtfs/' + file_name, 'r') as f:
        lines = f.readlines()[1:]
        return [line[:-1].split(',') for line in lines]


def add_data(flask_app: Flask, gtfs_obj, file_name: str) -> None:
    with flask_app.app_context():
        if gtfs_obj.query.count() == 0:
            file = read_csv(file_name)
            data = [gtfs_obj(*line) for line in file]
            for datum in data:
                db.session.add(datum)
            db.session.commit()


def init_db(flask_app: Flask) -> None:
    add_data(flask_app, Agency, 'agency.txt')
    add_data(flask_app, Stop, 'stops.txt')
    add_data(flask_app, Route, 'routes.txt')
    add_data(flask_app, Calendar, 'calendar.txt')
    add_data(flask_app, CalendarDate, 'calendar_dates.txt')
    add_data(flask_app, Shape, 'shapes.txt')
    add_data(flask_app, Office, 'office_jp.txt')
    add_data(flask_app, Trip, 'trips.txt')
