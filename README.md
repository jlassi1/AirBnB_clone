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
["[BaseModel] (0d6a8a84-d01a-458f-b6cb-9bbcc9d5fefc) {'id': '0d6a8a84-d01a-458f-b6cb-9bbcc9d5fefc', 'created_at': datetime.datetime(2020, 7, 1, 15, 6, 9, 356015), 'updated_at': datetime.datetime(2020, 7, 1, 15, 6, 9, 356022), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (2895be14-a3c1-4f19-94e1-b3112a3a7ed4) {'id': '2895be14-a3c1-4f19-94e1-b3112a3a7ed4', 'created_at': datetime.datetime(2020, 7, 1, 15, 6, 10, 114481), 'updated_at': datetime.datetime(2020, 7, 1, 15, 6, 10, 114492), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (e8e11646-5b23-4ef4-ac5b-a5a39cd243dd) {'id': 'e8e11646-5b23-4ef4-ac5b-a5a39cd243dd', 'created_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 637754), 'updated_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 637758), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (c32a1315-66a6-47a3-861e-f89f271a9b29) {'id': 'c32a1315-66a6-47a3-861e-f89f271a9b29', 'created_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 637912), 'updated_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 637914), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (e68530a0-dd20-47d0-82d7-107c3f254e4d) {'id': 'e68530a0-dd20-47d0-82d7-107c3f254e4d', 'created_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638151), 'updated_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638153), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (241dd255-bb49-4a81-a861-30b06d9545d5) {'id': '241dd255-bb49-4a81-a861-30b06d9545d5', 'created_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638276), 'updated_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638278), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (f915f096-6617-4e24-afc6-2b5a4bc91b6a) {'id': 'f915f096-6617-4e24-afc6-2b5a4bc91b6a', 'created_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638395), 'updated_at': datetime.datetime(2020, 7, 1, 15, 26, 34, 638397), 'name': 'Holberton', 'my_number': 89}"

show
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

## Contributors:
        khawla Jlassi: https://github.com/jlassi1
        Imene Ayari: https://github.com/Immaannn2222

        Relase date: July 2nd, 2020 (enhancements loading...)
