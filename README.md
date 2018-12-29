A basic example of updating device shadow from Flask-based web API using boto3.

Prerequisites:
* You should have a thing named "mydevice" configured in AWS IoT.

Terminal 1 contains instructions for executing the code locally. When you want to access it externally,
unset `FLASK_ENV` so that debugger will be disabled, and execute `flask run` with `--port 80` as `root` user.

Terminal 2 contains examples for testing the web API with a specific device.

Terminal 1:
```bash
$ cd <project directory>
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r reqirements.txt
$ export AWS_DEFAULT_REGION=<region>
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

Terminal 2:
```bash
$ curl http://127.0.0.1:5000/devices/mydevice
{"state":{},"metadata":{},"version":1,"timestamp":1531833620}

$ curl --request POST --header 'Content-Type: application/json' --data '{"user_id": "alex", "contact_details": "test"}' http://127.0.0.1:5000/devices/mydevice
{"state":{"desired":{"alex":"test"}},"metadata":{"desired":{"alex":{"timestamp":1531835416}}},"version":3,"timestamp":1531835416}

$ curl http://127.0.0.1:5000/devices/mydevice
{"state":{"desired":{"alex":"test"},"delta":{"alex":"test"}},"metadata":{"desired":{"alex":{"timestamp":1531835416}}},"version":3,"timestamp":1531835444}
```
