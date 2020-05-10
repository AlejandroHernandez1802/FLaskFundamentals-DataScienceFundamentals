from flask import Flask
from datetime import datetime, date, time, timedelta
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def showActualTime():
    actualTime = datetime.now()
    actualTime={'Hour':actualTime.hour,'Minute': actualTime.minute, 'Seconds': actualTime.second, 'Date': [actualTime.year, actualTime.month, actualTime.day]}
    return jsonify(actualTime)


if __name__ == "__main__":
    app.run()
