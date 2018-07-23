# Feuersoftware
A python lib for interaction with Feuersoftware programs

## Connect API

### Trigger an operation

Example for passsing an alarm to Connect with token read from default file (a file named token located right next to the script):

Token file:
```
QJYty4yyWSLGOZ58azhWyamsXcVmJXlHdOVdbC3Jf8czWcICuWzfMVBNDHJiUe5YJXokqlnAMTH0mccobJB4NrEdTedwJHeCoKh8An4hSuLHcfmoJYxjVP5QphoKfUJ1CFQ0fGlMhKVhjpVzDK7BJ8z8PNeByenbmb4SLHaKETlCJqm3nRJtqB2pzunrmMa5wgE9ZgpGq8aOrhT4ejwOtFyatmGdwwMcgzPuC4HUDPMOwevYhLcoyCb7LnwkYfxtKVTyOcO9m59pm5eJwpf6dU7MJwltHbZVNtQeN5hAvLjpGFq31PcNn6k2mG0Xm6vnZTQJBjw93cfnGpGeS49EOWYLnTuVLfuhlKQpHIQgihMmWEBqo3GkUL5H4kvfgc5T7zHOGvz11hHboBRPsbIBkgDHRPzlCEl7isTogKqvKPLLKH4bOfgPIEiML7RdLytDBMx6HPzztWPVOATJrCO84zEefntOWaeuJZ8IzIuxtaUiXDTIok3oJy2GNnhrI04L1XSXhMRZnrLpOmtD3FwCeVDcqiIRh5PBjY5ywVS2RynLasBf
```

Script:
```
from feuersoftware.connect import API

api = API()
api.set_api_token()
api.operation(
    start="2018-07-23T12:00:00", 
    keyword="Brand klein", 
    address="Musterstrasse 19, 12345 Entenhausen", 
    position=(47.421065, 10.985362), 
    facts="Eingeklemmte Person", 
    ric="12345", 
    properties=
        [
            {"key":"Melder", "value":"Hans Müller"},
            {"key":"Sontige Zusatzinfos", "value":"Nein"}
        ]
```

Example for passsing an alarm to Connect with token read from file:
```
from feuersoftware.connect import API

api = API()
api.set_api_token(tokenfile="/home/pi/token")
api.operation(
    start="2018-07-23T12:00:00", 
    keyword="Brand klein", 
    address="Musterstrasse 19, 12345 Entenhausen", 
    position=(47.421065, 10.985362), 
    facts="Eingeklemmte Person", 
    ric="12345", 
    properties=
        [
            {"key":"Melder", "value":"Hans Müller"},
            {"key":"Sontige Zusatzinfos", "value":"Nein"}
        ]
```

Example for passsing an alarm to Connect with token passed as a string:
```
from feuersoftware.connect import API

TOKEN = "QJYty4yyWSLGOZ58azhWyamsXcVmJXlHdOVdbC3Jf8czWcICuWzfMVBNDHJiUe5YJXokqlnAMTH0mccobJB4NrEdTedwJHeCoKh8An4hSuLHcfmoJYxjVP5QphoKfUJ1CFQ0fGlMhKVhjpVzDK7BJ8z8PNeByenbmb4SLHaKETlCJqm3nRJtqB2pzunrmMa5wgE9ZgpGq8aOrhT4ejwOtFyatmGdwwMcgzPuC4HUDPMOwevYhLcoyCb7LnwkYfxtKVTyOcO9m59pm5eJwpf6dU7MJwltHbZVNtQeN5hAvLjpGFq31PcNn6k2mG0Xm6vnZTQJBjw93cfnGpGeS49EOWYLnTuVLfuhlKQpHIQgihMmWEBqo3GkUL5H4kvfgc5T7zHOGvz11hHboBRPsbIBkgDHRPzlCEl7isTogKqvKPLLKH4bOfgPIEiML7RdLytDBMx6HPzztWPVOATJrCO84zEefntOWaeuJZ8IzIuxtaUiXDTIok3oJy2GNnhrI04L1XSXhMRZnrLpOmtD3FwCeVDcqiIRh5PBjY5ywVS2RynLasBf"

api = API()
api.set_api_token(token=TOKEN)
api.operation(
    start="2018-07-23T12:00:00", 
    keyword="Brand klein", 
    address="Musterstrasse 19, 12345 Entenhausen", 
    position=(47.421065, 10.985362), 
    facts="Eingeklemmte Person", 
    ric="12345", 
    properties=
        [
            {"key":"Melder", "value":"Hans Müller"},
            {"key":"Sontige Zusatzinfos", "value":"Nein"}
        ]
```

### Set a status

You can use the same methods for setting the API token as in the examples above.

Example for passsing a status to Connect with token read from file:
```
from feuersoftware.connect import API

api = API()
api.set_api_token(tokenfile="/home/pi/token")
api.status(
    radio="12345", 
    status=2, 
    position=(47.421065, 10.985362)
    )
```

