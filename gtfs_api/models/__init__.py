from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, String, Float, Integer, ForeignKey

db = SQLAlchemy()


def test(f, val):
    if val == "":
        return None
    else:
        return f(val)


class Agency(db.Model):
    __tablename__ = 'agency'
    id = Column(String(13), nullable=False, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    timezone = Column(Text, nullable=False)
    lang = Column(Text, nullable=True)
    phone = Column(Text, nullable=True)
    fare_url = Column(Text, nullable=True)
    email = Column(Text, nullable=True)

    def __init__(self, id, name, url, timezone, lang, phone, fare_url, email) -> None:
        self.id = id
        self.name = name
        self.url = url
        self.timezone = timezone
        self.lang = test(str, lang)
        self.phone = test(str, phone)
        self.fare_url = test(str, fare_url)
        self.email = test(str, email)


class Stop(db.Model):
    __tablename__ = 'stops'
    id = Column(String(16), nullable=False, primary_key=True)
    code = Column(Text, nullable=True)
    name = Column(Text, nullable=False)
    desc = Column(Text, nullable=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    zone_id = Column(Text, nullable=True)
    url = Column(Text, nullable=True)
    location_type = Column(Integer, nullable=True)
    parent_station = Column(Text, nullable=True)
    timezone = Column(Text, nullable=True)
    wheelchair_boarding = Column(Integer, nullable=True)

    def __init__(self, id, code, name, desc, lat, lon, zone_id, url,
                 location_type, parent_station, timezone, wheelchair_boarding):
        self.id = id
        self.code = test(str, code)
        self.name = name
        self.desc = test(str, desc)
        self.lat = float(lat)
        self.lon = float(lon)
        self.zone_id = test(str, zone_id)
        self.url = test(str, url)
        self.location_type = test(int, location_type)
        self.parent_station = test(str, parent_station)
        self.timezone = test(str, timezone)
        self.wheelchair_boarding = test(int, wheelchair_boarding)


class Route(db.Model):
    __tablename__ = 'routes'
    id = Column(String(16), nullable=False, primary_key=True)
    agency_id = Column(String(13), ForeignKey('agency.id'), nullable=False)
    short_name = Column(Text, nullable=False)
    long_name = Column(Text, nullable=False)
    desc = Column(Text, nullable=True)
    type = Column(Integer, nullable=False)
    url = Column(Text, nullable=True)
    color = Column(Text, nullable=True)
    text_color = Column(Text, nullable=True)
    jp_parent_route_id = Column(Text, nullable=True)

    def __init__(self, id, agency_id, short_name, long_name, desc, type, url, color, text_color, jp_parent_route_id):
        self.id = id
        self.agency_id = agency_id
        self.short_name = short_name
        self.long_name = long_name
        self.desc = test(str, desc)
        self.type = test(int, type)
        self.url = test(str, url)
        self.color = test(str, color)
        self.text_color = test(str, text_color)
        self.jp_parent_route_id = test(str, jp_parent_route_id)


class Calendar(db.Model):
    __tablename__ = 'calendar'
    service_id = Column(String(16), nullable=False, primary_key=True)
    monday = Column(Integer, nullable=False)
    tuesday = Column(Integer, nullable=False)
    wednesday = Column(Integer, nullable=False)
    thursday = Column(Integer, nullable=False)
    friday = Column(Integer, nullable=False)
    saturday = Column(Integer, nullable=False)
    sunday = Column(Integer, nullable=False)
    start_date = Column(String(8), nullable=False)
    end_date = Column(String(8), nullable=False)

    def __init__(self, service_id, monday, tuesday, wednesday,
                 thursday, friday, saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = int(monday)
        self.tuesday = int(tuesday)
        self.wednesday = int(wednesday)
        self.thursday = int(thursday)
        self.friday = int(friday)
        self.saturday = int(saturday)
        self.sunday = int(sunday)
        self.start_date = start_date
        self.end_date = end_date


class CalendarDate(db.Model):
    __tablename__ = 'calendar_dates'
    service_id = Column(String(16), ForeignKey('calendar.service_id'), nullable=False, primary_key=True)
    date = Column(String(8), nullable=False, primary_key=True)
    exception_type = Column(Integer, nullable=False)

    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = int(exception_type)


class Shape(db.Model):
    __tablename__ = 'shapes'
    id = Column(String(16), nullable=False, primary_key=True)
    pt_lat = Column(Float, nullable=False)
    pt_lon = Column(Float, nullable=False)
    pt_sequence = Column(Integer, nullable=False, primary_key=True)
    dist_traveled = Column(Float, nullable=True)

    def __init__(self, id, lat, lon, sequence, dist_traveled):
        self.id = id
        self.pt_lat = float(lat)
        self.pt_lon = float(lon)
        self.pt_sequence = int(sequence)
        self.dist_traveled = test(float, dist_traveled)


class Office(db.Model):
    __tablename__ = 'office'
    id = Column(String(32), nullable=False, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text, nullable=True)
    phone = Column(Text, nullable=True)

    def __init__(self, id, name, url, phone):
        self.id = id
        self.name = name
        self.url = url
        self.phone = phone


class Trip(db.Model):
    __tablename__ = 'trips'
    route_id = Column(String(16), ForeignKey('routes.id'), nullable=False)
    service_id = Column(String(16), ForeignKey('calendar.service_id'), nullable=False)
    id = Column(String(32), nullable=False, primary_key=True)
    headsign = Column(Text, nullable=True)
    short_name = Column(Text, nullable=True)
    direction_id = Column(Integer, nullable=True)
    block_id = Column(Text, nullable=True)
    shape_id = Column(String(16), ForeignKey('shapes.id'), nullable=True)
    wheelchair_accessible = Column(Integer, nullable=True)
    bikes_allowed = Column(Integer, nullable=True)
    desc = Column(Text, nullable=True)
    desc_symbol = Column(Text, nullable=True)
    office_id = Column(String(32), nullable=True)

    def __init__(self, route_id, service_id, id, headsign, short_name, direction_id, block_id,
                 shape_id, wheelchair_accessible, bikes_allowed, desc, desc_symbol, office_id):
        self.route_id = route_id
        self.service_id = service_id
        self.id = id
        self.headsign = test(str, headsign)
        self.short_name = test(str, short_name)
        self.direction_id = test(int, direction_id)
        self.block_id = test(str, block_id)
        self.shape_id = test(str, shape_id)
        self.wheelchair_accessible = test(int, wheelchair_accessible)
        self.bikes_allowed = test(int, bikes_allowed)
        self.desc = test(str, desc)
        self.desc_symbol = test(str, desc_symbol)
        self.office_id = test(str, office_id)
