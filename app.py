from flask import Flask, render_template, json
import os
import database.db_connector as db
import simplejson as json
import decimal



# Configuration
app = Flask(__name__)
db_connection = db.connect_to_database()
# Routes
#  
@app.route('/')
def hello():
    return "hello"

@app.route('/league_histories')
def legue_histories():
    query = "SELECT * FROM league_histories;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

@app.route('/coaches')
def coaches():
    query = "SELECT * FROM coaches;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

@app.route('/players')
def players():
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

@app.route('/coach_team_relations')
def coach_team_relations():
    query = "SELECT * FROM coach_team_relations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

@app.route('/player_team_relations')
def player_team_relations():
    query = "SELECT * FROM player_team_relations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

@app.route('/seasons')
def seasons():
    query = "SELECT * FROM seasons;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results





# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 21098)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True)