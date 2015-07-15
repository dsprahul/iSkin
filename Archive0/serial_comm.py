#,'/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',  
#'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3'

# Modified version for Windows
import serial  
import time  
try:
	print "Trying to establish connection ..."
	arduino = serial.Serial('/dev/ttyACM0', 9600)
	print arduino.readline()
	
except:
	print "Connect Arduino / change the index to something else"


    
def data(angle):
      
	try:    
		
		print "Transferring data to Arduino in 2s... "
		val = str(angle)	
		print val
		arduino.write(val)
		

		
     	
	except:    
		print "Failed to send!"

	
alphan = 3000
betan = 1000
alpha = 344
beta = 44
data(alpha)
data(alphan)
print "echo:"
print arduino.readline()
data(beta)
data(betan)
print "echo:"
print arduino.readline()


