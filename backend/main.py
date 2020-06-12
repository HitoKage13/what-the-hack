'''
Description
'''

DATA = {
    'doctors': [
        {'name': 'Jimmothy', 'type': 'GP'},
        {'name': 'Tom', 'type': 'Specialist'},
        {'name': 'Joanna', 'type': 'Surgeon'}
    ],
    'queues': [
        {'name': 'GP', 'patients':[]},
        {'name': 'Specialist', 'patients':[]},
        {'name': 'Surgeon', 'patients':[]}
    ]
}
PATIENT_ID = 0

class Patient:
    def __init__(self, priority, name, age, telephone, emergency, medicare, diseases):
        self.id = PATIENT_ID
        self.priority = priority
        self.name = name
        self.age = age
        self.telephone = telephone
        self.emergency = emergency
        self.medicare = medicare
        self.diseases = diseases

def queue(name):
    for q in DATA['queues']:
        if q['name'] == name:
            return q
    raise Exception("Can't find queue")

def patient_create(priority, name, age, telephone, emergency, medicare, diseases):
    PATIENT_ID += 1
    new_patient = Patient(priority, name, age, telephone, emergency, medicare, diseases)
    for q in DATA['queues']:
        if q['name'] == 'GP':
            q['name'].append(new_patient)

def patient_move(id, prev_queue, to_here_queue):
    for q in DATA['queues']:
        if q['name'] == prev_queue:
            for patient in q['patients']:
                if patient[id] == id:
                    tmp = patient
    patient_delete(id, prev_queue)
    for q in DATA['queues']:
        if q['name'] == to_here_queue:
                q['patients'].append(tmp)
    
def patient_delete(id, prev_queue):
    for q in DATA['queues']:
        if q['name'] == prev_queue:
            for patient in q['patients']:
                if patient[id] == id:
                    q['name'].remove(patient)

def patient_info(id, info):
    for q in DATA['queues']:
        for patient in q['patients']:
            if patient[id] == id:
                patient.info = info  

def patient_status(id, status):
    for q in DATA['queues']:
        for p in q['patients']:
            if p['id'] == id:
                p['status'] = status
