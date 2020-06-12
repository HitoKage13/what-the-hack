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

# @APP.route('/patient/move', methods=['POST'])
# def patient_move():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/patient/delete', methods=['DELETE'])
# def patient_delete():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/patient/info', methods=['PUT'])
# def patient_info():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/patient/status', methods=['PUT'])
# def patient_status():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/doctor/create', methods=['POST'])
# def doctor_create():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/help', methods=['POST'])
# def help():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/status', methods=['GET'])
# def status():
#     '''
#     A route for
#     Params: {}
#     Raises: 
#     Returns: {}
#     '''
#     zid = request.get_json()['zid']
#     description = request.get_json()['description']
#     try:
#         helpr.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

if __name__ == "__main__":
    APP.run(port = 5050, debug=True)