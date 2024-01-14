0x0F. Python - Object-relational mapping
Python
OOP
SQL
MySQL
ORM
SQLAlchemy

# 0x0F. Python - Object-relational mapping


## Contents:open_file_folder:

- Project Description:newspaper:
- General Objectives:bulb:
- Instalation:wrench:
- Command Interpreter Description:computer:

	* How to start it
	* Commands and their usage
	* How to use it
	* examples

- Unittests:boom:
- Tasks:clipboard:
- Built with:hammer:
- Resources:books:
- Author:black_nib:

---

## Project Description:newspaper:

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

---

## General Objectives:bulb:

* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

---

## Instalation:wrench:

Follow the following instructions to get a copy of the program and run in your local machine.

* Clone the following repository.
```
https://github.com/PabloYepes27/holbertonschool-higher_level_programming.git
```

* Run the program
```
./file.py
```

---

## Tasks:clipboard:

### [0. Get all states](./0-select_states.py)
* Write a script that lists all states from the database hbtn_0e_0_usa:


### [1. Filter states](./1-filter_states.py)
* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:


### [2. Filter states by user input](./2-my_filter_states.py)
* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.


### [3. SQL Injection... ](./3-my_safe_filter_states.py)
* write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!


### [4. Cities by states ](./4-cities_by_state.py)
* Write a script that lists all cities from the database hbtn_0e_4_usa


### [5. All cities by state](./5-filter_cities.py)
* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa


### [6. First state model](./model_state.py)
* Write a python file that contains the class definition of a State and an instance Base = declarative_base():


### [7. All states via SQLAlchemy ](./7-model_state_fetch_all.py)
* Write a script that lists all State objects from the database hbtn_0e_6_usa


### [8. First state ](./8-model_state_fetch_first.py)
* Write a script that prints the first State object from the database hbtn_0e_6_usa


### [9. Contains `a` ](./9-model_state_filter_a.py)
* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa


### [10. Get a state ](./10-model_state_my_get.py)
* Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa


### [11. Add a new state](./11-model_state_insert.py)
* Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa


### [12. Update a state](./12-model_state_update_id_2.py)
* Write a script that changes the name of a State object from the database hbtn_0e_6_usa

### [13. Delete states](./13-model_state_delete_a.py)
* Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa


### [14. Cities in state](./14-model_city_fetch_by_state.py)
* Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.


### [15. City relationship](./100-relationship_states_cities.py)
* Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py


### [16. List relationship](./101-relationship_states_cities_list.py)
* Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa


### [17. From city](./102-relationship_cities_states_list.py)
* Write a script that lists all City objects from the database hbtn_0e_101_usa



---

## Built with:hammer:

Python
MySQL
MySQLdb
SQLAlchemy
Flask

---

## Resources:books:

* [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)
* [MySQLdb tutorial](http://www.mikusa.com/python-mysql-docs/index.html)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient-python)
* [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
* [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
* [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
* [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
* [SQLAlchemy ORM - Working with Joins](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm)
* [Basic Relationship Patterns](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)

---

## Author:black_nib:

* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)
