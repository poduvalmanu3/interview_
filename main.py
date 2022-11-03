from flask import Flask, request, jsonify
from task import calc_oil, calc_gas, calc_brine
import sys


app = Flask(__name__)
port = 8080

if sys.argv.__len__() > 1:
    port = sys.argv[1]

@app.route('/')
def hello():
    return "Default page has been opened"

@app.route('/data')
def data():
    well_id = request.args.get('well')
    if well_id is not None:
        response = {
        "oil": str(calc_oil(well_id)),
        "gas": str(calc_gas(well_id)), 
        "brine": str(calc_brine(well_id))
        }
        return jsonify(response)
    else:
        return "Please provide well param in query"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
