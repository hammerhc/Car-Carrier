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

### Packages ###
Install all required packages
```
pip install -r requirements.txt
```

## Run ##

Run the Docker-Container
```
docker-compose -f docker/docker-compose.yml up -d 
```

The Virtualenv must be activated before executing the following commands 

Migrations

```
python src/manage.py db init

python src/manage.py db migrate

python src/manage.py db upgrade
```

Run Python Application

```
python src/app.py
```

Open your Browser on following site:

```
http://localhost:5000/
```
