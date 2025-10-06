Slowrun- ryhmätyö.

# Ohjeet käyttöön

## Virtuaaliympäristön luonti:

`python -m venv env`

## Virtuaaliympäristön aktivointi:

`env\scripts\activate`

## Projektin tarvittavien pakettien asentaminen:

`pip install -r requirements.txt`

## Djangon migraatioiden suorittaminen ja tietokannan luonti:

`python manage.py migrate`

## Djangon superkäyttäjän luonti:

`python manage.py createsuperuser`

## Neljän ennaltakirjoitetun uutisen luonti:

`python manage.py seed`

# Serverin käynnistyskomento:

`python manage.py runserver`

Sivusto avautuu osoitteessa http://localhost:8000

Admin paneeliin pääsee osoitteessa http://localhost:8000/admin
