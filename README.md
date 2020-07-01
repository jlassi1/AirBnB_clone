#              AirBnB clone
## Synopsis:

        The HBNB project is an AirBnB cloning that will be executed on different levels till building an entire web application at the end of the year.
        On this level we will handle a part from the backend.

## Description:

### The main class:
        Write a class BaseModel that defines all common attributes/methods for other classes

### Public instance attributes: 
   <MENU>
       <LI> id: string - assign with an uuid when an instance is created:
        you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
        the goal is to have unique id for each BaseModel
        <LI>created_at: datetime - assign with the current datetime when an instance is created
        <LI>updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
   <MENU>

### Public instance methods:
<MENU>
    <LI>save(self): updates the public instance attribute updated_at with the current datetime
    <LI>to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instanc
<MENU>

### The console:
         create your data model
         manage (create, update, destroy, etc) objects via a console / command interpreter
         store and persist objects to a file (JSON file)

        The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
        The console will be a tool to validate this storage engine


### See the follow examples on the utility of the console:
how to call the console : 
ayari_imen@ayari:~/AirBnB_clone$ ./console.py 
(hbnb) 


(hbnb) all
["[BaseModel] (0d6a8a84-d01a-458f-b6cb-9bbcc9d5fefc) {'id': '0d6a8a84-d01a-458f-b6cb-9bbcc9d5fefc', 'created_at': datetime.datetime(2020, 7, 1, 15, 6, 9, 356015), 'updated_at': datetime.datetime(2020, 7, 1, 15, 6, 9, 356022), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (2895be14-a3c1-4f19-94e1-b3112a3a7ed4) {'id': '2895be14-a3c1-4f19-94e1-b3112a3a7ed4', 'created_at': datetime.datetime(2020, 7, 1, 15, 6, 10, 114481), 'updated_at': datetime.datetime(2020, 7, 1, 15, 6, 10, 114492), 'name': 'Holberton', 'my_number': 89}"
(hbnb) show

** class name missing **

(hbnb) create BaseModel


f94953ec-931f-4cf1-9f42-0acddd014cce

(hbnb) update BaseModel f94953ec-931f-4cf1-9f42-0acddd014cce

** attribute name missing **

(hbnb) update BaseModel f94953ec-931f-4cf1-9f42-0acddd014cce name

** value missing **




## Technologies Used:
         language: Python version 3.4.3.
         verified by the PEP8 version 1.7
         The console class HBNBCommand is based on the cmd python module
         JSON is to serialize and deserialize data
         Unittesting for testing


Contributors:
khawla Jlassi: https://github.com/jlassi1
Imene Ayari: https://github.com/Immaannn2222



## Release date: 
July 2nd, 2020 (enhancements loading...)
