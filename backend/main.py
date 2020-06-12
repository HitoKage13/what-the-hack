'''
Description
'''
import random

DATA = {
    'doctors': [
        {'name': 'Jimmothy', 'type': 'GP'},
        {'name': 'Tom', 'type': 'Specialist'},
        {'name': 'Joanna', 'type': 'Surgeon'}
    ],
    'queues': [
        {'name': 'GP', 'patients':[
            {
                'id': 5,
                'priority': 'Urgent',
                'name': 'Bob',
                'age': 1,
                'telephone': 98383,
                'emergency': 373734,
                'medicare': 3373,
                'diseases': 'Diabetes',
            },
            {
                'id': 3,
                'priority': 'Referred',
                'name': 'Tony',
                'age': 3,
                'telephone': 567567,
                'emergency': 345345,
                'medicare': 567678,
                'diseases': 'Diabetes',
            }
        ]},
        {'name': 'Specialist', 'patients':[]},
        {'name': 'Surgeon', 'patients':[]}
    ]
}

def new_patient(priority, name, age, telephone, emergency, medicare, diseases):
    return {
        'id': random.randint(1, 10000000),
        'priority': priority,
        'name': name,
        'age': age,
        'telephone': telephone,
        'emergency': emergency,
        'medicare': medicare,
        'diseases': diseases,
    }

def return_data():
    return DATA

def queue(name):
    for q in DATA['queues']:
        if q['name'] == name:
            return q
    raise Exception("Can't find queue")

def patient_create(priority, name, age, telephone, emergency, medicare, diseases):
    new_guy = new_patient(priority, name, age, telephone, emergency, medicare, diseases)
    for q in DATA['queues']:
        if q['name'] == 'GP':
            q['patients'].append(new_guy)

def patient_move(id, prev_queue, to_here_queue):
    for q in DATA['queues']:
        if q['name'] == prev_queue:
            for patient in q['patients']:
                if patient['id'] == id:
                    tmp = patient
    patient_delete(id, prev_queue)
    for q in DATA['queues']:
        if q['name'] == to_here_queue:
                q['patients'].append(tmp)
    
def patient_delete(id, prev_queue):
    for q in DATA['queues']:
        if q['name'] == prev_queue:
            for patient in q['patients']:
                if patient['id'] == id:
                    q['patients'].remove(patient)

def patient_info(id, info):
    for q in DATA['queues']:
        for patient in q['patients']:
            if patient['id'] == id:
                patient['info'] = info

def patient_status(id, status):
    for q in DATA['queues']:
        for p in q['patients']:
            if p['id'] == id:
                p['status'] = status