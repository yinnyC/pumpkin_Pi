# Pumpkin Pi

## Webpage Demo -> [Link](https://pumpkin-pi.herokuapp.com/)

An interactive Jack-o-lantern powered by raspberry pi, that will play a spooky sound whenever it detects someone walks by and take a picture of whom it scares.
Later on, the picture will be uploaded onto a website, like a photo booth of the roller coaster.

## Instruction

1. Open two terminals and cd to the where the project file is
2. In one terminal, type in: \$python pumpkinPi.py
3. Then type : \$python app.py in another terminal
4. Enjoy the PumpkinPi and check your photo here: http://127.0.0.1:5000/

### Pumpkin Pi Photo Booth

![Index](./Resources/readme_imgs/index.gif)

### Send Picture to yourself

![sendPic](./Resources/readme_imgs/sendpic.gif)
_Enter your email and click 'Send'_

![email](./Resources/readme_imgs/email.png)
_Copy the URI Code_

![Paste](./Resources/readme_imgs/pasteOnBrowser.png)
_Paste the Code on a Browser_

![Result](./Resources/readme_imgs/result.png)
_There You Have It!_

## About the Hardware

### Equipment List

- Raspberry Pi 4
- Breadboard
- Breadboard wires
- HC-SR04 Ultrasonic Sensor
- Resistor 1k & 2k
- Picamera Module

I followed the tutorial form [here](https://pimylifeup.com/raspberry-pi-distance-sensor/),to wire the sensor up with the raspberry Pi
![Wiring](https://pi.lbbcdn.com/wp-content/uploads/2018/03/Distance-Sensor-Fritz-768x599.png)

## Product Features

- [x] Skateboard: Install the sensor(HC-SR04 Ultrasonic Sensor) and detect if someone walks by, then take a picture with the pi camera
- [x] Bike: Upload pictures and display them on a website
- [x] add feature: Allow user to send pictures to their email

<!-- ## Wire Frames

![Wireframe](./Resources/readme_imgs/Wireframe.jpg) -->

## Copyright

- All the sound effects are from [SoundBible.com](http://soundbible.com/)
- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
