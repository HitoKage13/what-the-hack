'''
Description
'''

DATA = {
    'doctors': [
        {'name': 'Jimmothy', 'type': 'GP'},
        {'name': 'Tom', 'type': 'Specialist'},
        {'name': 'Joanna', 'type': 'Surgeon'}}
    ],
    'queues': [
        {'name': 'GP', 'patients':[]},
        {'name': 'Specialist', 'patients':[]},
        {'name': 'Surgeon', 'patients':[]}
    ]
}

'''
class Patient:
    def __init__(self, name, age, telephone, emergency, medicare, diseases):
        self.name = name
        self.age = name
        self.telephone = name
        self.emergency = name
        self.medicare = name
        self.diseases = name
'''

# def return_data():
#     return DATA

# def return_destroy():
#     DATA['pop'] = "lil"
#     # DATA['queues'].append("hi")
#     return {"hi":"hi"}

# def queue(name):
#     for queue in DATA['queues']:
#         if queue['name'] == name:
#             return queue
#     raise Exception("Can't find queue")

# def patient_create(name):
#     new_patient = Patient(name, age, )
#     for queue in DATA['queues']:
#         if queue['name'] == name:
#             return queue
#     raise Exception("Can't find queue")

# if __name__ == "__main__":
#     print(DATA)

