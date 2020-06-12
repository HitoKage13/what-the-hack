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
        {'name': 'GP', 'patients': [
            {
                'id': 5,
                'priority': 'Emergency',
                'name': 'Bob',
                'age': 1,
                'telephone': 98383,
                'emergency': 373734,
                'medicare': 3373,
                'diseases': 'Diabetes',
            },
            {
                'id': 3,
                'priority': 'Non-Urgent',
                'name': 'Tony',
                'age': 3,
                'telephone': 567567,
                'emergency': 345345,
                'medicare': 567678,
                'diseases': 'Diabetes',
            }
        ]},
        {'name': 'Specialist', 'patients': []},
        {'name': 'Surgeon', 'patients': []}
    ]
}

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
    for q in DATA['queues']:
        if q['name'] == name:
            return q
    raise Exception("Can't find queue")

def patient_create(name):
    new_patient = Patient(name, age, )
    for queue in DATA['queues']:
        if queue['name'] == name:
            return queue
    raise Exception("Can't find queue")

if __name__ == "__main__":
    print(DATA)

