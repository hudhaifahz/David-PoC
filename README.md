# David Basic Control System PoC
Combines slider control with Radio buttons that specify the address of the Sabertooth motor controller.

Includes Python source to receive POSTs from PoC.html and set motor speed according to slider control.  Note that the RaspPi 3 normally uses the built-in UART for Bluetooth so you'll have to first disconnect it from this duty and also disable the console.  See http://raspberrypi.stackexchange.com/questions/45570/how-do-i-make-serial-work-on-the-raspberry-pi3 for instructions.
