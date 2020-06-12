'''
Description
'''
from flask import Flask, request
from werkzeug.exceptions import BadRequest
from main import return_data, queue, patient_create, patient_delete, \
    patient_info, patient_move, patient_status
from json import dumps

APP = Flask(__name__)

@APP.route('/return/data', methods=['GET'])
def return_data_route():
    return dumps(return_data())

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
    return dumps(dct)

@APP.route('/patient/create', methods=['POST'])
def patient_create_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    priority = request.get_json()['priority']
    name = request.get_json()['name']
    age = request.get_json()['age']
    telephone = request.get_json()['telephone']
    emergency = request.get_json()['emergency']
    medicare = request.get_json()['medicare']
    diseases = request.get_json()['diseases']
    patient_create(priority, name, age, telephone, emergency, medicare, diseases)
    return dumps({})

@APP.route('/patient/move', methods=['PUT'])
def patient_move_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    id = request.get_json()['id']
    prev_queue = request.get_json()['prev_queue']
    to_here_queue = request.get_json()['to_here_queue']
    patient_move(id, prev_queue, to_here_queue)
    return dumps({})

@APP.route('/patient/delete', methods=['DELETE'])
def patient_delete_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    id = request.get_json()['id']
    prev_queue = request.get_json()['prev_queue']
    patient_delete(id, prev_queue)
    return dumps({})

@APP.route('/patient/info', methods=['POST'])
def patient_info_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    id = request.get_json()['id']
    info = request.get_json()['info']
    patient_info(id, info)
    return dumps({})

@APP.route('/patient/status', methods=['POST'])
def patient_status_route():
    '''
    A route for
    Params: {}
    Raises: 
    Returns: {}
    '''
    id = request.get_json()['id']
    status = request.get_json()['status']
    patient_status(id, status)
    return dumps({})

if __name__ == "__main__":
    APP.run(port = 5050, debug=True)