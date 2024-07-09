
import pytest
import uuid
import sqlite3
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from models.settings.db_connection_handler import db_connection_handler

def adapt_datetime(dt):
    return dt.isoformat()

sqlite3.register_adapter(datetime, adapt_datetime)
db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    start_date = datetime.strptime("02-01-2024", "%d-%m-%Y")
    end_date = start_date + timedelta(days=5)
    
    trips_infos = {
        "id": trip_id,    
        "destination": "Osasco",    
        "start_date": adapt_datetime(start_date),  
        "end_date": adapt_datetime(end_date),
        "owner_name": "Osvaldo",    
        "owner_email": "osvaldo@gmail.com"
    }
    
    trips_repository.create_trip(trips_infos)

@pytest.mark.skip(reason="Interação com o banco")    
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()   
    trips_repository = TripsRepository(conn)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason="Interação com o banco")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()   
    trips_repository = TripsRepository(conn)
    
    trips_repository.update_trip_status(trip_id)
