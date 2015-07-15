#,'/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',  
#'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3'

# Modified version for Windows
import serial  
import time  


    
def data(angle):
      
	try:    
		print "Trying to establish connection ..."
		arduino = serial.Serial('/dev/ttyACM0', 14400)
		print arduino.readline()
		time.sleep(1)
		print "Transferring data to Arduino (routine:data)... "
		val = str(angle)	
		val = val + '\n'
		print val
		arduino.write(val)
		
		print "echo:"
		print arduino.readline()
		arduino.close()
		time.sleep(1)
     	
	except:    
		print "Failed to send!"

	
alpha = 334
alphan = 3000
beta = 44
betan = 3000
time.sleep(1)
data(angle = alpha)
data(beta)
data("Rahul")
data("this")
data("Shit")
data("Worked!")









