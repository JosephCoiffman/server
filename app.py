from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)
db_connection = db.connect_to_database()
# Routes 

@app.route('/players_select')
def bsg_people():
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9208)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True)