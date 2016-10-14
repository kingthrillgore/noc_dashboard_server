# NOC Dashboard Server
By its own, the NOC Dashboard is capable of many things. But with this tentpole server, it can be capable of so much more! When installed and enabled, the following features become available to you...

* Receiving NWS Alerts (through a pass-through proxy)
* Live Alerts for Systems, Network, and Weather (with many more to come)
* Advanced Statistics for Network

## Requirements
A server with Python 2.7+, pip and virtualenv is required.

If you want to run this through real hardware, a Gunicorn and WSGI binding is included in the repo.

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

### Setting up Gunicorn
TBD

### Setting up WSGI w/ Apache
TBD

### Setting up WSGI w/ Nginx
TBD

### If all else fails: Forward Proxy w/ Apache2
Create a conf file with the following settings:

```
TBD
```
Restart Apache, and check if your changes work.

## Configuration
TBD

## Setting up Alerts
By default, the server will run through available sources for changes every minute, and send an Event Active to all connected clients when a change of the following nature occurs:

* For Services, a system monitored **enters a CRITICAL state** or **33% of the active services for a host default to a state besides NORMAL**.
* For Network, when an ntop-recovered feed confirms **no local address has shown a response for longer than 30 seconds**, or **the packet loss increases to over 50% of requests made over 10 seconds**.
* For Weather, **when an update from the NWS Alerts indicates an Emergency that meets the Event Level of WARN** [\[1\]](https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding#Event_codes)

## Using the NWS Alert Proxy
The National Weather Service for some really stupid reasons imposes Access-Control-Allow-Origin headers on any requests made to the Alerts service. To access a JSON version of the latest alerts, simply send a GET request to `/alerts/weather/{{FIPSCODE}}`. The contents will look sorta like this:

```json
{
  'example':9999
}
```

You can also request the original CAP-encoded XML by passing `?xml=1` in the URL string. But why would you want to do that?

I am legally required to inform you that EAS SAME codes are not used in this service. Not that it would matter anyways.

## Libraries
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