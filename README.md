# AirBnB clone
This project completed at Holberton school replicates the AirBnB webapp.
<p align="center">
   <img src="https://i.imgur.com/JOhaZ5m.png"></p>
# Current Features

### Air_BnBClone/models

*module containing class files*
  - __BaseModel__ (models/base_model.py): model class containing attributes and methods to be inherited

##### subclasses of BaseModel

  - __User__ (models/user.py): additional class attributes: email, password, first_name, last_name
  - __State__ (models/state.py): additional class attributes: name
  - __City__ (models/city.py): additional class attributes: state_id, name
  - __Amenity__ (models/amenity.py): additional class attributes: name
  - __Place__ (models/place.py): additional class attributes: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
  - __Review__ (models/review.py): additional class attributes: place_id, user_id, text

### Air_BnBClone/console.py
*HBNBcommand is a subclass of python's cmd which, in the context of this project, can be used to:*
  - Create a new object (ex: a new User or a new Place)
  - Retrieve an object from a file, a database etc
  - Do operations on objects (count, compute stats, etc)
  - Update attributes of an object
  - Destroy an object
# Project Setup

### download repo
```sh
$ git clone https://github.com/Miuywu/AirBnB_clone/blob/master/console.py
$ cd AirBnB_clone
```
### Using the console
```sh
$ ./console.py
$ (HBNB)
$ (HBNB) quit
```
### Creating/Showing a file in console
```sh
$ ./console.py
$ (HBNB) create BaseModel
$ c3440b3c-f917-446d-9d4f-781d790e784a
$ (hbnb) show BaseModel c3440b3c-f917-446d-9d4f-781d790e784a
[BaseModel] (c3440b3c-f917-446d-9d4f-781d790e784a) {'id': 'c3440b3c-f917-446d-9d4f-781d790e784a', 'created_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586378), 'updated_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586392)}
$ (HBNB) quit
```

##### Console commands description and usage

 - __all__ [ModelName] (show all instances stored, optionally filtered by class)
 - __count__ ModelName (count number of instances of a model are stored)
 - __show__ ModelName InstanceId (show the JSON representation of a stored model instance)
 - __destroy__ ModelName InstanceId (delete a model instance from storage)
 - __update__ ModelName InstanceId AttributeName AttributeValue (update an attribute on a stored instance)


### Calling methods by model name
```sh
$ ./console.py
$ (hbnb) create BaseModel
$ c3440b3c-f917-446d-9d4f-781d790e784a
$ (hbnb) BaseModel.show("c3440b3c-f917-446d-9d4f-781d790e784a")
[BaseModel] (c3440b3c-f917-446d-9d4f-781d790e784a) {'id': 'c3440b3c-f917-446d-9d4f-781d790e784a', 'created_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586378), 'updated_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586392)}
$ (hbnb) BaseModel.update("c3440b3c-f917-446d-9d4f-781d790e784a", "z", 4)
$ (hbnb) BaseModel.show("c3440b3c-f917-446d-9d4f-781d790e784a")
[BaseModel] (c3440b3c-f917-446d-9d4f-781d790e784a) {'id': 'c3440b3c-f917-446d-9d4f-781d790e784a', 'created_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586378), 'updated_at': datetime.datetime(2019, 11, 14, 5, 59, 26, 586392), 'z': 4}
$ (hbnb) BaseModel.destroy("c3440b3c-f917-446d-9d4f-781d790e784a")
$ (hbnb) BaseModel.show("c3440b3c-f917-446d-9d4f-781d790e784a")
** no instance found **
$ (hbnb) quit
```
### Unit testing
*in AirBnB_clone/ directory, enter the following command to run our unit tests...*
```sh
$ python3 -m unittest discover tests/
$     ...
$ Ran 35 tests in 0.065s

OK
$
```
###### (11-13-2019)Current Authors: *[James Cook](https://github.com/benjamesian) and [Minh-Huy Vu](https://github.com/Miuywu)*
