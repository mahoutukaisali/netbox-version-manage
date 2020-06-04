# import functions from the flask library
from flask import Flask, jsonify, request, abort
import json

# create an app instance
app = Flask(__name__)

# create a devices resource
devices = [
    {
        "id": 0,
        "name": "NX-9K-1",
        "ip": "10.0.0.1"
    },
    {
        "id": 1,
        "name": "NX-9K-2",
        "ip": "10.0.0.2"
    }
]


# handle GET request
@app.route('/api/netbox/', methods=['GET'])
def get_devices():
    return jsonify({'tasks': devices})


# handle POST request
## Flask server should manage data in each service.
## so that Flask server has ip for posting netbox
@app.route('/api/netbox/', methods=['POST'])
def post_from_git():
    #  check required parameters
    # if doesn't have all required parameters, return 404 error
    if request.headers['Content-Type'] == 'application/json':
        return json.dumps(request.json)

    # generate device obj
    device = {
        "id": len(devices),
        "name": request.json['name'],
        "ip": request.json['ip']
    }

    ## generate obj from git to post netbox here
    ## it will be parsed json format by pyATS or Napalm



    ## Post to netbox from here





# main entry
if __name__ == '__main__':
    # run app when script is been execute
    # this will create a web server at port 8080, you can visit http://0.0.0.0:8080/
    app.run(host='0.0.0.0', port=5000, debug=True)