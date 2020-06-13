'''
Description
'''
import random

DATA = {
    'doctors': [
        {'name': 'Jimmothy Lim', 'type': 'GP'},
        {'name': 'Tom Smith', 'type': 'Specialist'},
        {'name': 'Joanna Shim', 'type': 'Surgeon'}
    ],
    'queues': [
        {'name': 'GP', 'patients':[
            {
                'id': 1,
                'priority': 'Urgent',
                'name': 'Sandeep Das',
                'age': 1,
                'telephone': '0404983831',
                'emergency': '0405985831',
                'medicare': 337389012,
                'diseases': 'Diabetes',
            },
            {
                'id': 5,
                'priority': 'Urgent',
                'name': 'Claudine Jung',
                'age': 1,
                'telephone': '0498383123',
                'emergency': '0434373734',
                'medicare': 423423373,
                'diseases': 'Diabetes',
            },
        ]},
        {'name': 'Specialist', 'patients':[
            {
                'id': 3 ,
                'priority': 'Referred',
                'name': 'Haesun Shim',
                'age': 3,
                'telephone': '0451567567',
                'emergency': '0412367567',
                'medicare': 454345654,
                'diseases': 'Diabetes',
            },
            {
                'id': 7,
                'priority': 'Referred',
                'name': 'Tony Smith',
                'age': 3,
                'telephone': 567567,
                'emergency': 345345,
                'medicare': 567678,
                'diseases': 'Diabetes',
            }
        ]},
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