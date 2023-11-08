#from .db import engine
import db

def golden_run_list():
    '''
    Return a list of run numbers for all gold runs
    '''
    conn = db,engine.connect()

    result = conn.execute("SELECT DISTINCT ON (run) run FROM evaluated_runs WHERE list = 1")
    rows = result.fetchall()

    gold_runs = [run[0] for run in rows]

    return gold_runs

