import instana
import mysql.connector

from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

@app.route('/insert')
def insertData():
    data = request.args.get('data')
    print(data)
    
    mydb = mysql.connector.connect(
        host="54.180.25.66",
        user="shpark",
        passwd="shpark",
        database="sctest",
        use_pure=True
    )
    try:
        mycursor = mydb.cursor(prepared=True)

        sql = "insert into test (name) values (%s)"

        val = (data)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        return "message"
    except mysql.connector.Error as error :
        print("Failed to update record to database: {}".format(error))
        mydb.rollback()
        return "message failed"

    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
            print("MySQL connection is closed")
    
@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return json_response(time=now)


@app.route('/increment_value', methods=['POST'])
def increment_value():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        value = int(data['value'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(value=value + 1)


@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')