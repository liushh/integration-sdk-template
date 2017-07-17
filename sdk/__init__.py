import jwt

def get_name():
    print('this function should return the name of this integration 07/17')

def get_available_fields():
    print('this function should return the name of this integration 07/17')

def get_functions():
    print('this function should return the name of this integration 07/17')

def encode(payload):
    encoded_payload = jwt.encode(payload, 'secret', algorithm='HS256').decode('ascii')
    print('encoded_payload = ', encoded_payload)
