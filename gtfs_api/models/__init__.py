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
