## Car-Carrier ##
Simon Krieger
S-INF-18aL

## Setup ##
Clone the repository

### Python ###
Windows:
Download and install Python from [here](https://www.python.org/downloads/)

Linux:
Install Python 3
```
sudo apt install python3
```

Install Pip
```
sudo apt install python3-pip
```

### Virtualenv ###
Install Virtualenv
```
pip install virtualenv
```

Create Virtualenv
```
cd backend
virtualenv env
```

Activate Virtualenv

Windows:
```
.\env\scripts\activate
```

Linux:
```
source env/bin/activate
```

You should now see the “env” indicator at the beginning of your command prompt.

```
(env) prompt$
```

Deactivate Virtualenv
```
deactivate
```

### Packages ###
Install all required packages
```
pip install -r requirements.txt
```

## Run ##

The Virtualenv must be activated before executing the following commands 

Migrations

```
python backend/src/manage.py db init

python backend/src/manage.py db migrate

python backend/src/manage.py db upgrade
```

Run Python Application

```
python backend/src/app.py
```