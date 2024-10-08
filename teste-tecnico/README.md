# To do List App

## Description

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

## Requirements

- **Setup the dev environment with docker**
  - Using docker-compose with as many volumes as it takes
- **Use Python’s Flask framework and any other library**
- **Use any SQL database**
- **Secure routes**
- **Write tests**

## How to Start

To start the application, simply run the following command in the terminal:

```bash
docker-compose up -d
```

| Método | Endpoint | Descrição                      |
|--------|----------|--------------------------------|
| GET    | /owner   | Returns the list of all owners |
| POST   | /owner   | Register a new owner           |
| GET    | /cars/:id | Returns all cars from one owner |
| POST   | /cars | Register a new car for owner   |




