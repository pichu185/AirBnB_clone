# AirBnB clone - The console

The console is the first part of the **AirBnB clone** project which aims to deploy a simple copy of the AirBnB website to cover all fundamental concepts of the higher level programming track.  

<br>

<div align=center>  
    <img  
    style="text-align:center"  
    src="https://raw.githubusercontent.com/coding-max/hbtn_config/main/assets/hbnb.png"  
    alt="holbertonbnb"/>  
</div>

<br>

## Overview

This first part of the project focuses on creating a command interpreter that allows to:  
- create the data model  
- manage (create, update and destroy) objects via a console  
- store and persist objects to a file (JSON file)  


## Files and Directories

**`/models`** directory constains all classes used for the project.  
[basemodel.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/base_model.py) file contains the base class (**BaseModel**) of all models in the project:  
- [user.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/user.py) - file contains the `User` class.  
- [state.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/state.py) - file contains the `State` class.  
- [city.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/city.py) - file contains the `City`class.  
- [amenity.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/amenity.py) - file contains the `Amenity` class.  
- [place.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/place.py) - file contains the `Place` class.  
- [review.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/review.py) - file contains the `Review` class.  

**`/models/engine`** directory contains the class that handles JASON serialization and deserialization.  
[file_storage.py](https://github.com/coding-max/AirBnB_clone/blob/main/models/engine/file_storage.py) - file contains `FileStorage` class.  

**`/tests`** directory contains all unit test cases for this project.  

[console.py](https://github.com/coding-max/AirBnB_clone/blob/main/console.py) the console contains the entry point of the command interpreter.  

<br>

```
|── console.py
├── models/
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   |── user.py
│   └── engine/
│       └── file_storage.py
└── tests/
    |── test_console.py
    └── test_models/
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        |── test_user.py
        └── test_engine/
            └── test_file_storage.py
```

## Environment and Execution

This project was interpreted/compiled and tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).  

To use the console you must have `pyhton3` installed and the repository cloned  
(`git clone git@github.com:coding-max/AirBnB_clone.git`).  

To start the console you only need to run `./console` in the root of the repository.  

The console works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) BaseModel.count()
0
(hbnb) create BaseModel
96589f6a-4856-4d3c-b9e4-3e8985f18bb8
(hbnb) create User
5acd7fb5-31b8-4193-8df4-f3353056b0b0
(hbnb) BaseModel.count()
1
(hbnb) BaseModel.destroy("96589f6a-4856-4d3c-b9e4-3e8985f18bb8")
(hbnb) BaseModel.count()
0
(hbnb) 
(hbnb) 
(hbnb) quit
$

```

## Authors

- [Maximiliano Pan](https://www.linkedin.com/in/maximilianopan/)  
- [Agustín Otegui]()  