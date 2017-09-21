# NOC Dashboard Server
By its own, the NOC Dashboard is capable of many things. But with this tentpole server, it can be capable of so much more! When installed and enabled, the following features become available to you...

* Receiving NWS Alerts (through a pass-through proxy)
* Busting through CORS headers [like a boss](https://www.youtube.com/watch?v=NisCkxU544c)
* Live Alerts for Systems, Network, and Weather (with many more to come)
* Advanced Statistics for Network

## Requirements
A server with Python 2.7+, pip and virtualenv is required.

If you want to run this through real hardware, a Gunicorn and WSGI binding for nginx is included in the repo. There are other ways to access this that you can find if you apply yourself.

## Installation
Clone this repo
```
#!shell
$ git clone git@bitbucket.org:internaldevck/noc_dashboard_server.git
```

Activate virtualenv
```
#!shell
$ source {VENV_FILE}
```

Install the required components
```
#!shell
$ pip install -r requirements.txt
```

Change your config settings (TODO)

And start the server
```
#!shell
$ python server.py
```

Once online, you can access it via http://127.0.0.1:4510 assuming you keep your default settings in order.

## Configuration
TBD

## Setting up Alerts
By default, the server will run through available sources for changes every minute, and send an Event Active to all connected clients when a change of the following nature occurs:

* For Services, a system monitored **enters a CRITICAL state** or **33% of the active services for a host default to a state besides NORMAL**.
* For Network, when an ntop-recovered feed confirms **no local address has shown a response for longer than 30 seconds**, or **the packet loss increases to over 50% of requests made over 10 seconds**.
* For Weather, **when an update from the NWS Alerts indicates an Emergency that meets the Event Level of WRN** [\[1\]](https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding#Event_codes)

By default all feeds will update when a change is detected on their source feeds. They are updated every 30 seconds by default (excluding weather, which is checked every 120 seconds). The settings, update periods, and thresholds can be configured by editing `settings.json`.

Existing records are kept in `cache` and are flushed out every hour. This is done with a fake cron, but you can always use the real thing like this:

```
#!shell
* * * * *
```

## Using the NWS Alert Proxy
The National Weather Service for some really stupid reasons imposes Access-Control-Allow-Origin headers on any requests made to the Alerts service. To access a JSON version of the latest alerts, simply send a GET request to `/alerts/weather/{{FIPSCODE}}`. The contents will look sorta like this:

```
#!javascript
{
  'example':9999
}
```

You can also request the original CAP-encoded XML by passing `?xml=1` in the URL string. But why would you want to do that?

## Libraries
The following Python libraries are used in this application:

* Flask
* Gevent
* Flask-SocketIO
* (A Python JSON library to be determined later on)
* BeautifulSoup
* WeatherAlerts
* Scapy

## Improvements? Suggestions
If you think there are improvements to be made, open up a ticket and make a pull request. There are some tasks open that may be worth covering.

I will attempt to address any new issues and PRs that are sent my way (bandwidth permitting). [Given how most programmers treat pull requests](http://www.urbandictionary.com/define.php?term=patches+are+welcome&defid=7833039), It's the least I can do.

## License
Licensed under the MIT License, like the NOC Dashboard. See LICENSE.md. Python libraries used are subject to their own separate licenses.