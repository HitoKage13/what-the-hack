'''
Description
'''

from flask import Flask, request

from werkzeug.exceptions import BadRequest

from main import queue_create

from json import dumps

APP = Flask(__name__)

@APP.route('/q', methods=['POST'])
def q():
    name = request.get_json()['name']
    return dumps({'hi': name})

@APP.route('/queue/create', methods=['POST'])
def queue_create_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    name = request.get_json()["name"]
    queue_create(name)
    return dumps({})

@APP.route('/queue', methods=['GET'])
def queue_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    name = request.args.get('name')
    dct = queue(name)
    return dumps({})

@APP.route('/patient/create', methods=['POST'])
def patient_create():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/patient/move', methods=['POST'])
def patient_move():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/patient/delete', methods=['DELETE'])
def patient_delete():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/patient/info', methods=['PUT'])
def patient_info():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/patient/status', methods=['PUT'])
def patient_status():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/doctor/create', methods=['POST'])
def doctor_create():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/help', methods=['POST'])
def help():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

@APP.route('/status', methods=['GET'])
def status():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    zid = request.get_json()['zid']
    description = request.get_json()['description']
    try:
        helpr.make_request(zid, description)
    except (KeyError,  ValueError):
        raise BadRequest('')
    return dumps({})

if __name__ == "__main__":
    APP.run(port = 5050, debug=True)