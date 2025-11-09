import requests
from jsonschema import validate
from shemas import update_method_shema, create_method_shema, register_method_shema, login_method_shema

def test_put_status_code_200():
    response = requests.put('https://reqres.in/api/users/2',
                             json={'job':'zion resident', 'name': 'morpheus'},
                             headers={'x-api-key': 'reqres-free-v1'})
    assert response.status_code == 200
    validate(response.json(), schema=update_method_shema)

def test_post_status_code_201_and_content_in_response():
    response = requests.post('https://reqres.in/api/users',
                             json={'job':'leader', 'name': 'morpheus'},
                             headers={'x-api-key': 'reqres-free-v1'})
    assert response.status_code == 201
    assert response.text != ''
    validate(response.json(), schema=create_method_shema)

def test_post_without_haders_should_return_error():
    response = requests.post('https://reqres.in/api/users',
                                json={'job': 'leader', 'name': 'morpheus', 'surname': 'morpheus'})
    assert response.status_code == 401
    assert response.text == '{"error":"Missing API key"}'

def test_delete_status_code_204_and_empty_content_in_response():
    response = requests.delete('https://reqres.in/api/users',
                             headers={'x-api-key': 'reqres-free-v1'})
    assert response.status_code == 204
    assert response.text == ''

def test_get_status_code_404():
    response = requests.get('https://reqres.in/api/users/23',
                            headers={'x-api-key': 'reqres-free-v1'})
    assert response.status_code == 404

def test_post_status_code_400():
    response = requests.post('https://reqres.in/api/register',
                             json={'email': 'sydney@fife'},
                             headers={'x-api-key': 'reqres-free-v1'})
    assert response.status_code == 400


def test_register_successful_shema():
    response = requests.post('https://reqres.in/api/register',
                             json={'email': 'eve.holt@reqres.in', 'password': 'pistol'},
                             headers={'x-api-key': 'reqres-free-v1'})
    validate(response.json(), schema=register_method_shema)

def test_login_successful_shema():
    response = requests.post('https://reqres.in/api/login',
                             json={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'},
                             headers={'x-api-key': 'reqres-free-v1'})
    validate(response.json(), schema=login_method_shema)