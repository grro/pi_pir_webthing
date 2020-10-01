# pi_pir_webthing
A web connected PIR motion sensor on Raspberry Pi

This project provides a [webthing API](https://iot.mozilla.org/wot/) to a PIR motion sensor such as [descriped here](https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf).  

The pi_pir_webthing package exposes an http webthing endpoint which supports detecting motion via http. E.g. 
```
# webthing has been started on host 192.168.0.23

curl http://192.168.0.23:9544/properties 

{
   "time": false,
   "last_motion": "2020-09-28T08:04:02.330388"
}
```

Regarding the RaspberryPi/PIR sensor hardware setup and wiring please refer tutorials such as [How to Interface a PIR Motion Sensor With Raspberry Pi GPIO](https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio)

To install this software you may use [PIP](https://realpython.com/what-is-pip/) package manager such as shown below
```
sudo pip install pi_pir_webthing
```

After this installation you may start the webthing http endpoint inside your python code or via command line using
```
sudo pir --command listen --port 9544 --gpio 14
```
Here, the webthing API will be bind to the local port 9544 and be connected to the PIR pin using gpio 14

Alternatively to the *listen* command, you can use the *register* command to register and start the webthing service as systemd unit. 
By doing this the webthing service will be started automatically on boot. Starting the server manually using the *listen* command is no longer necessary. 
```
sudo pir --command register --port 9544 --gpio 14
```  