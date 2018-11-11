import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# 17, 18 are RIGHT motor
# 22, 23 are LEFT motor
GPIO.setup(17, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def forward():
	print('forward')
	GPIO.output(18,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
        GPIO.output(17,GPIO.HIGH)#forward
        GPIO.output(23,GPIO.HIGH)#forward
        time.sleep(3)
        GPIO.output(17, GPIO.LOW)#stop
        GPIO.output(23, GPIO.LOW)#stop
	time.sleep(0.5)

def backward():
	print('back')
        GPIO.output(17, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(3)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	time.sleep(0.5)

def tleft():
	print('left')
	GPIO.output(18,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(23,GPIO.LOW)
        GPIO.output(17,GPIO.HIGH) #LEFT
        time.sleep(3)
        GPIO.output(17, GPIO.LOW) #stop
	time.sleep(0.5)

def tright():
	print('right')
        GPIO.output(17,GPIO.LOW) 
	GPIO.output(18,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(23,GPIO.HIGH) #RIGHT
        time.sleep(3)
        GPIO.output(23,GPIO.LOW) #stop
	time.sleep(0.5)

def main():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
	n=raw_input("Enter the value \n1 = straight \n2 = Reverse \n3 = Left \n4 = Right\n")
	d=['1','2','3','4']
	p=[]
	while(n in d):
		print("work")
		p.extend(n)
		if(n=='1'):
			forward()
			time.sleep(0.25)
		        print('F')
		elif(n=='2'):
			backward()
	        	time.sleep(0.25)
			print('Rev')
		elif(n=='3'):
			tleft()
			time.sleep(0.25)
		        print('L')
		elif(n=='4'):
			tright()
			time.sleep(0.25)
			print('R')
		else:
			print('B')
			break;
		n=raw_input("Enter the value \n1 = straight \n2 = Reverse \n3 = Left \n4 = Right\n")
	print(p)
	GPIO.cleanup()
main()
GPIO.cleanup()
