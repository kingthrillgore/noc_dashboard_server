# NOC Dashboard Server
By its own, the NOC Dashboard is capable of many things. But with this tentpole server, it can be capable of so much more! When installed and enabled, the following features become available to you...

* Receiving NWS Alerts (through a pass-through proxy)
* Live Alerts for Systems, Network, and Weather (with many more to come)
* Advanced Statistics for Network

## Requirements
A server with Python 2.7+, pip and virtualenv is required. If you want to run this through real hardware, a Gunicorn and mod\_WSGI binding is included in the repo.

## Installation
Clone this repo
```shell
$ git clone git@bitbucket.org:internaldevck/noc_dashboard_server.git
```

Activate virtualenv
```shell
$ source {VENV_FILE}
```

Install the required components
```shell
$ pip install -r requirements.txt
```

And start the server
```shell
$ python server.py -port 8080
```

## Configuration
TBD

## Components
The following Python libraries are used in this application:

* Flask
* Gevent
* Flask-SocketIO
* (A Python JSON library to be determined later on)
* BeautifulSoup
* WeatherAlerts
* Scapy

## License
Licensed under the MIT License, like the NOC Dashboard. See LICENSE.md. Python licenses used are subject to their own separate licenses.