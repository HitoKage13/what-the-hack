'''
Description
'''
from flask import Flask, request

# from werkzeug.exceptions import BadRequest

from main import queue_create, queue

from json import dumps

APP = Flask(__name__)

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
    return dumps(queue(name))

# @APP.route('/patient/create', methods=['POST'])
# def patient_create():
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

#     id = request.get_json()['id']
#     description = request.get_json()['description']
#     try:
#         main.make_request(id, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/patient/info', methods=['PUT'])
# def patient_info():

#     zid = request.get_json()['id']
#     description = request.get_json()['description']
#     try:
#         main.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/patient/status', methods=['PUT'])
# def patient_status():

#     zid = request.get_json()['id']
#     description = request.get_json()['description']
#     try:
#         main.make_request(zid, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/doctor/create', methods=['POST'])
# def doctor_create():

#     id = request.get_json()['id']
#     description = request.get_json()['description']
#     try:
#         main.make_request(id, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

# @APP.route('/help', methods=['POST'])
# def help():

#     id = request.get_json()['id']
#     description = request.get_json()['description']
#     try:
#         main.make_request(id, description)
#     except (KeyError,  ValueError):
#         raise BadRequest('')
#     return dumps({})

if __name__ == "__main__":
    APP.run(port=5050, debug=True)