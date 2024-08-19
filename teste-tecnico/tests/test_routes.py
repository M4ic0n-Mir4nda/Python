import json

from models.car import CarColor, CarModel, Car
from models.owner import Owner


def test_enum_color_values_correct():
    assert CarColor.blue.value == 'blue'
    assert CarColor.yellow.value == 'yellow'
    assert CarColor.gray.value == 'gray'


def test_enum_color_values_incorrect():
    assert CarColor.blue.value != 'gray'
    assert CarColor.yellow.value != 'blue'
    assert CarColor.gray.value != 'yellow'


def test_num_model_values_correct():
    assert CarModel.sedan.value == 'sedan'
    assert CarModel.hatch.value == 'hatch'
    assert CarModel.convertible.value == 'convertible'


def test_num_model_values_incorrect():
    assert CarModel.sedan.value != 'convertible'
    assert CarModel.hatch.value != 'sedan'
    assert CarModel.convertible.value != 'hatch'


def test_get_status_code_owners(client):
    response = client.get('/owner')
    assert response.status_code == 200


def test_create_owner(client):
    response = client.post('/owner', json={'name': 'Alice'})
    assert response.status_code == 201

    data = json.loads(response.data)
    assert data['name'] == 'Alice'
    assert Owner.query.filter_by(name='Alice').first() is not None


def test_create_owner_no_name(client):
    response = client.post('/owner', json={'error': 'Maicon'})
    assert response.status_code == 402
    assert response.json['message'] == 'Field name must be not null.'


def test_create_car_for_owner(client):
    client.post('/owner', json={'name': 'Maicon'})
    owner = Owner.query.filter_by(name='Maicon').first()

    response = client.post('/cars', json={
        'color': 'yellow',
        'model': 'sedan',
        'id_owner': owner.id
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['color'] == 'yellow'
    assert data['model'] == 'sedan'
    assert Car.query.filter_by(id_owner=owner.id).count() == 1


def test_not_found_owner(client):
    response = client.post('/cars', json={
        'color': 'yellow',
        'model': 'sedan',
        'id_owner': 1
    })

    assert response.status_code == 404
    assert response.json["message"] == "Owner not found. Car cannot exist without an owner."


def test_create_car_with_incorrect_color(client):
    client.post('/owner', json={'name': 'Maicon'})
    owner = Owner.query.filter_by(name='Maicon').first()

    response = client.post('/cars', json={
        'color': 'red',
        'model': 'sedan',
        'id_owner': owner.id
    })

    assert response.status_code == 402


def test_create_car_with_incorrect_model(client):
    client.post('/owner', json={'name': 'Maicon'})
    owner = Owner.query.filter_by(name='Maicon').first()

    response = client.post('/cars', json={
        'color': 'yellow',
        'model': 'conversivel',
        'id_owner': owner.id
    })

    assert response.status_code == 402


def test_create_three_cars_for_owner(client):
    client.post('/owner', json={'name': 'Maicon'})
    owner = Owner.query.filter_by(name='Maicon').first()

    response_car1 = client.post('/cars', json={
        'color': 'yellow',
        'model': 'sedan',
        'id_owner': owner.id
    })
    assert response_car1.status_code == 201

    response_car2 = client.post('/cars', json={
        'color': 'blue',
        'model': 'convertible',
        'id_owner': owner.id
    })
    assert response_car2.status_code == 201

    response_car3 = client.post('/cars', json={
        'color': 'gray',
        'model': 'hatch',
        'id_owner': owner.id
    })
    assert response_car3.status_code == 201

    response_car4 = client.post('/cars', json={
        'color': 'gray',
        'model': 'sedan',
        'id_owner': owner.id
    })
    assert response_car4.status_code == 402
    assert response_car4.json["message"] == "You can only have up to 3 cars."

    assert Car.query.filter_by(id_owner=owner.id).count() == 3

    get_response = client.get(f'/cars/{owner.id}')
    assert get_response.status_code == 200

    if get_response.status_code == 200:
        data = json.loads(get_response.data)
        assert len(data) == 3
