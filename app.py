import json

import boto3
from flask import Flask, request


app = Flask(__name__)


@app.route('/devices/<device_id>', methods=['GET', 'POST'])
def manage_devices(device_id):
    client = boto3.client('iot-data')
    if request.method == 'GET':
        response = client.get_thing_shadow(thingName=device_id)
    else:
        user_data = request.get_json()
        state = {
            'state': {
                'desired': {
                    user_data['user_id']: user_data['contact_details']
                }
            }
        }
        response = client.update_thing_shadow(
            thingName=device_id, payload=json.dumps(state))
    return response['payload'].read()
