import json




#methos that return 5 attributes
def method_five_attributes(event, context):
    body = {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "city": "New York",
        "country": "USA"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


def method_ten_attributes(event, context):
    body= {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "city": "New York",
        "country": "USA",
        "phone": "+1 123-456-7890",
        "gender": "Male",
        "occupation": "Software Engineer",
        "company": "Tech Corp",
        "hobby": "Reading"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

