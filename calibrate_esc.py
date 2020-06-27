import pigpio

input('Start ESC in calibrate mode and press ENTER...')

pi = pigpio.pi()
pi.set_servo_pulsewidth(17, 1500)
print('Throtle set to mid position (neutral)')
input('Press the set button (one beep) then ENTER to proceed')

pi.set_servo_pulsewidth(17, 2000)
print('Throtle set to max position (full)')
input('Press the set button again (two beeps) then ENTER to proceed')

pi.set_servo_pulsewidth(17, 1000)
print('Throtle set to min position (break)')
input('Press the set button again (three beeps) then ENTER to proceed')

pi.write(17, 0)
pi.stop()