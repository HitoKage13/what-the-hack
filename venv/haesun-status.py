
WAITING_LIST = []

def make_request(zid, description):
    global WAITING_LIST

    if description is None:
        raise ValueError
    if description == "":
        raise ValueError
    # correspondoing student id is already inside the queue.
    for student in WAITING_LIST:
        if student['zid'] == zid:
            raise KeyError

    WAITING_LIST.append({'zid': zid, 'description': description, 'status': 'waiting'})


def queue():
    '''
    Used by tutors to view all the students in the queue in order.

    Returns:
      (list of dict) : A list of dictionaries where each dictionary has the keys
      { 'zid', 'description', 'status' }. These correspond to the student's ZID,
      the description of their problem, and the status of their request (either
      "waiting" or "receiving").
    '''
    global WAITING_LIST
    return WAITING_LIST

def remaining(zid):
    '''
    Used by students to see how many requests there are ahead of theirs in the
    queue that also have a "waiting" status.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the student does not have a request in the queue with a
      "waiting" status.

    Returns:
      (int) : The position as a number >= 0
    '''
    for student in queue():
        if student['zid'] == zid and student['status'] == 'receiving':
            raise KeyError
    for student in queue():
        if student['zid'] == zid:
            get_turn = queue().index(student)
            if queue()[0]['status'] == 'receiving':
                return get_turn - 1
    return get_turn

def help(zid):
    '''
    Used by tutors to indicate that a student is getting help with their
    request. It sets the status of the request to "receiving".

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the given student does not have a request with a "waiting"
      status.
    '''
    for student in queue():
        if student['zid'] == zid:
            if student['status'] != 'waiting':
                raise KeyError
            student['status'] = 'receiving'

def resolve(zid):
    '''
    Used by tutors to remove a request from the queue when it has been resolved.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the given student does not have a request in the queue with a
      "receiving" status.
    '''
    #global ID_TIME_PAIR
    for student in queue():
        if student['zid'] == zid:
            if student['zid'] == zid and student['status'] != 'receiving':
                raise KeyError
            queue().remove(student)
    # update ID_TIME_PAIR dictionary because they've got help

def cancel(zid):
    '''
    Used by students to remove their request from the queue in the event they
    solved the problem themselves before a tutor was a available to help them.

    Unlike resolve(), any requests that are cancelled are NOT counted towards
    the total number of requests the student has made in the session.

    Params:
      zid (str): The ZID of the student who made the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "waiting" status.
    '''
    for student in queue():
        if student['zid'] == zid:
            if student['status'] != 'waiting':
                raise KeyError
            queue().remove(student)

def revert(zid):
    '''
    Used by tutors in the event they cannot continuing helping the student. This
    function sets the status of student's request back to "waiting" so that
    another tutor can help them.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "receiving" status.
    '''
    for student in queue():
        if student['zid'] == zid:
            if student['status'] != 'receiving':
                raise KeyError
            student['status'] = 'waiting'

def reprioritise():
    '''
    Used by tutors toward the end of the help session to prioritize the students
    who have received the least help so far.

    The queue is rearranged so that if one student has made fewer non-cancelled
    requests than another student, they are ahead of them in the queue. The
    ordering is otherwise preserved; i.e. if a student has made the same number
    of requests as another student, but was ahead of them in the queue, after
    reprioritise() is called, they should still be ahead of them in the queue.
    '''
    #HINT: This function might be challenging to implement. You may wish to
    # leave it till after you test and implement the other functions.
    global WAITING_LIST

    # sorted(ID_TIME_PAIR, key = itemgetter(0))
    # print(ID_TIME_PAIR)


def end():
    '''
    Used by tutors at the end of the help session. All requests are removed from
    the queue and any records of previously resolved requests are wiped.
    '''
    global WAITING_LIST#, ID_TIME_PAIR
    WAITING_LIST = []
    #ID_TIME_PAIR = []
