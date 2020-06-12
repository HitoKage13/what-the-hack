'''
Description
'''

DATA = {'doctors': [], 'queues': []}

class Patient:
    def __init__(self, name, age, telephone, emergency, medicare, diseases):
        self.name = name
        self.age = name
        self.telephone = name
        self.emergency = name
        self.medicare = name
        self.diseases = name

def queue_create(name):
    '''
    Description:
    Params:
    Raises:
    '''
    global DATA
    DATA['queues'].append("bob")
    # queue = {'name': name, 'patients': []}
    # DATA['queues'].append(queue)

def queue(name):
    for queue in DATA['queues']:
        if queue['name'] == name:
            return queue
    raise Exception("Can't find queue")

def patient_create(name):
    new_patient = Patient(name, age, )
    for queue in DATA['queues']:
        if queue['name'] == name:
            return queue
    raise Exception("Can't find queue")

if __name__ == "__main__":
    print(DATA)

