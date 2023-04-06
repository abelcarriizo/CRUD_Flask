## Flask SQLAlchemy CRUD

This project is a CRUD application using flask and mysql using SQLAlchemy

### Manual Installation

##### Requirements

* Python3
* MariaDB

##### Steps
before run the app you must create the following environnment variables:

```
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DATABASE=
MYSQL_HOST=
MYSQL_PORT=
```

```
git clone https://github.com/abelcarriizo/CRUD_Flask.git
cd CRUD_Flask
pip install virtualenv
python3 -m venv venv
. ./venv/source/bin/activate
pip install -r requirements.txt
python index.py
```