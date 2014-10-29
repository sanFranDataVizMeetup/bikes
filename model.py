from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Numeric
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

ENGINE = create_engine("sqlite:///bike.db", echo=False)
db_session = scoped_session(sessionmaker(bind=ENGINE,
                                         autocommit=False,
                                         autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()


class Incident(Base):
    __tablename__ = "incident"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_reported = Column(DateTime, nullable=False)
    date_incident = Column(DateTime, nullable=True)
    time_incident = Column(DateTime, nullable=True)
    latitude = Column(Numeric, nullable=True)
    longtitude = Column(Numeric, nullable=True)
    injury_severity = Column(Text, nullable=True)
    road_cond_slope = Column(Text, nullable=True)   # uphill/downhill
    road_cond_hazard = Column(Text, nullable=True)  # muni tracks/grill/manhole covers
    bike_path = Column(Boolean, nullable=True)
    riding_impaired = Column(Boolean, nullable=True)
    comments = Column(Text, nullable=True)


def main():

    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()
