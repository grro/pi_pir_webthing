# pi_pir_webthing
A web connected PIR motion sensor on Raspberry Pi

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a PIR motion sensor such as [descriped here](https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf).  

The pi_pir_webthing package exposes an http webthing endpoint which supports detecting motion via http. E.g. 
```
# webthing has been started on host 192.168.0.23

curl http://192.168.0.23:9544/properties 

{
   "motion": true,
   "last_motion": "2020-09-28T08:04:02.330388"
}
```

The RaspberryPi/PIR sensor hardware setup and wiring may look like [HC SR501 example](https://github.com/grro/pi_pir_webthing/blob/master/docs/layout.png). 
