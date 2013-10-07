PNR API
======

We all hate [Indian Railways](http://indianrail.gov.in) for being sucky, and not providing a public API to query the PNR status of railway tickets. So, I thought I'd make my own when my favorite 3rd party API was down.

## Usage ##

As simple as it gets! Suppose your PNR is __6223797269__. Just do a ``GET`` at:

```
http://pnrapi.dfth.in/6223797269
```

And you'll get a JSON like this:

```
{
  "data": {
    "alight": {
      "code": "NDLS", 
      "name": "NEW DELHI"
    }, 
    "board": {
      "code": "JSME", 
      "name": "JASIDIH"
    }, 
    "chart_prepared": "CHART PREPARED", 
    "class": "SL", 
    "from": {
      "code": "JSME", 
      "name": "JASIDIH"
    }, 
    "passenger": [
      {
        "seat_number": "Can/Mod", 
        "status": "W/L 54,RLGN"
      }
    ], 
    "to": {
      "code": "NDLS", 
      "name": "NEW DELHI"
    }, 
    "train_name": "POORVA EXPRESS", 
    "train_number": "12303", 
    "travel_date": "5-10-2013"
  }, 
  "status": "OK"
}
```

Nice and easy!

### Status Codes ###

``OK`` when everything's alright.

``PNR FLUSHED / SERVICE UNAVAILABLE`` when either the PNR has been flushed/not generated yet, or the Indian Railways servers are having some nasty issues. Not my fault.

``ERROR`` when due to some mysterious reasons, I'm not able to fetch the result. But try again, and I'll try my best.

## Issues ##

Please feel free to file bugs/feature requests. Better still, fork it and get your hands dirty. :)