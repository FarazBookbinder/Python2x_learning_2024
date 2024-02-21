api_response = {
    "first_name": "Faraz",
    "age": 29,
    "last_name": "Binder",
    "email": "faraz@yopmail.com",
    "password": "Python@learning2x",
    "mobile number": 9898789809
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response["password"] = "Python@learning2x"
print(api_response)


for key, value in api_response.items():
    print(key, " => ", value)