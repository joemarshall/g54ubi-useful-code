import grovepi
import grovelcd
import grove6axis
import grovenfctag

print "timestamp,button,temperature,ultrasound"
while True:
    button=grovepi.digitalRead(2)
    print(button)
    temperature=grovepi.analogRead(0)
    ultrasound=grovepi.ultrasonicRead(7)
    print time.time(),",",button,",",temperature,",",ultrasound


