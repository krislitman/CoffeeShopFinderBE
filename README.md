# Coffee Shop Finder

### Django API
==============

![Special_Agent_Dale_Cooper](https://media.giphy.com/media/26mkhIj7fJHjq0JMI/giphy.gif)

<!-- [![CircleCI](https://circleci.com/gh/krislitman/Song-Discovery.svg?style=shield)](https://circleci.com/gh/krislitman/Song-Discovery) -->

© Kris Litman ([LinkedIn](https://www.linkedin.com/in/kris-litman/)) 2021<br> (Creator)

Table of Contents
=================

* [Introduction](#introduction)
* [Key Features](#key_features)
* [Installation](#installation)
* [Running the Test Suite](#running_the_test_suite)
* [Built With](#built_with)
* [Versioning](#versioning)
* [Acknowledgements](#acknowledgements)


## Introduction

API for Coffee Finder application. Takes in data from the FE application via API request, creating Coffee Shop/Favorite Shop/User models in the database. Also can create Favorite Shops for a User with a rating from 1 to 10.

## Key Features
#### Endpoints
**`GET localhost:8000/api/v1/coffeeshops/`**
 - Returns all coffee shops in the database
 - Example Response:

```
  [
    {
        "id": 8,
        "name": "Link Coffee",
        "location": {
            "city": "Denver, CO"
        },
        "is_closed": false,
        "categories": [
            {
                "cool_spot": "true"
            }
        ],
```

**`GET localhost:8000/api/v1/favoriteshops/`**
 - Returns all favorite shop objects in database
 - Example Response:

```
 [
    {
        "id": 1,
        "coffeeshop": 8,
        "user": 1,
        "rating": 9
    },
```
## Installation

To receive a working copy of the application on your computer, first you will need to
fork and clone this repository.

Make sure have the package Poetry installed, and then run this command to
install dependencies:
```
$ Poetry Install
```
To run a local server, run this command from the root directory:
```
$ python3 manage.py runserver
```
Now you will be able to hit the API endpoints in your browser or Postman!

## Running the Test Suite
## Built With

<ul>
<li>
  Django
</li>
<li>
  Python3
</li>
<li>
  PostgreSQL
</li>
<li>
  Postman
</li>
<li>
  Poetry
</li>
<li>
  Python-Dotenv
</li>
</ul>

## Versioning

<ul>
<li>
  Python3 3.9.5
</li>
<li>
  Django 3.2.4
</li>
<li>

## Acknowledgements

- [Giphy](https://giphy.com/)
