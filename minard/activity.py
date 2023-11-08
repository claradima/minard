#from .db import engine
import db

def get_deck_activity(limit=25, offset=0):
    '''
    Return a dictionary of deck activity information
    '''
    conn = db.engine.connect()

    result = conn.execute("SELECT checkintime, checkouttime, checkinrun, "
                          "checkoutrun, firstname, lastname, reason FROM logbook "
                          "ORDER BY checkintime DESC LIMIT %s OFFSET %s", \
                          (limit,offset))

    if result is None:
        return None

    keys = result.keys()
    rows = result.fetchall()

    return [dict(zip(keys, row)) for row in rows]

