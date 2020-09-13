# rcpi-controller
Control your RC car with Xbox360 controller and Raspberry PI

## Installation
1. Install [pigpio](http://abyz.me.uk/rpi/pigpio/download.html).
2. Add [xbox360controller](https://pypi.org/project/xbox360controller/) library to your python enviroment.
3. Run pigpio daemon, it's nessessary for the script to run.  
**To start the pigpio daemon:**  
```sudo pigpiod```  
**To stop the pigpio daemon:**  
```sudo killal pigpiod```  

## Calibration
There's a video about calibrating your ESC with a standard RC remote:  
https://www.youtube.com/watch?v=MiKeYJnYjxU  

To calibrate your ESC to work properly with your Xbox 360 controller run the 
[calibrate_esc.py](https://github.com/alexkobal/rcpi-controller/blob/master/calibrate_esc.py) script and follow the instructions.

## Running the controller
1. Ensure that the controller is connected to your Raspberry PI.
2. Ensure that pigpio daemon is running.
3. Start the [run_rcpi_controller.py]() script

## Controlls
RT: Move forward  
LT: Move backward  
Left Joystick: Turn  
Xbox: Reset  
Back: Reset throttle  
Hat Up/Down: Movement throttle  
Hat Left/Right: Turn throttle
