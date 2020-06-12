'''
Description
'''

DATA = {'doctors': [], 'queues': []}
PATIENT_ID = 0
class Patient:
    def __init__(self, name, age, telephone, emergency, medicare, diseases):
        self.id = PATIENT_ID
        self.name = name
        self.age = age
        self.telephone = telephone
        self.emergency = emergency
        self.medicare = medicare
        self.diseases = diseases

def queue(queue_name):
    for q in DATA['queues']:
        if q['queue_name'] == queue_name:
            return q
    raise Exception("Can't find queue")

def patient_create(name, age, telephone, emergency, medicare, diseases):
    PATIENT_ID += 1
    new_patient = Patient(name, age, telephone, emergency, medicare, diseases)
    

def patient_move(id, prev_queue, to_here_queue):
    for q in DATA['queues']:
        if q == prev_queue:
            for patient in q['patients']:
                if patient[id] == id:
                    tmp = patient
    patient_delete(id, prev_queue)
    for q in DATA['queues']:
        if q == to_here_queue:
                q['patients'].append(tmp)
    
def patient_delete(id, prev_queue):
    for q in DATA['queues']:
        if q == prev_queue:
            for patient in q['patients']:
                if patient[id] == id:
                    q.remove(patient)

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


if __name__ == "__main__":
    print(DATA)