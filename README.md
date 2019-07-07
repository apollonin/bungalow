# Bungalow Django API


## Setup

Install requirements
```
pip install -r requirements.txt
```

Load data to sqlite db

```
python manage.py parse_and_load_data challenge_data.csv
```


## API instructions

* run server 

```
python manage.py runserver
```

* check /schema enpoint to get all available APIs and json format

```
curl http://127.0.0.1:8000/houses/schema/?format=corejson
```