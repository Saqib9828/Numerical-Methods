import numpy as np
A = np.array([[4, -1, 1], [-1, 4, -2], [1, -2, 4]])
B = np.array([12, -1, 5])

x1= 0.0;x2 =0.0;x3 = 0.0;
count=0
while True:
	w = x1;  y= x2; z = x3;
	
	x1 = float((B[0]-A[0][1]*x2-A[0][2]*x3)/A[0][0])
	x2 = float((B[1]-A[1][0]*x1-A[1][2]*x3)/A[1][1])
	x3 = float((B[2]-A[2][0]*x1-A[2][1]*x2)/A[2][2])
	if(abs(w-x1)<0.1 and abs(y-x2)<0.1 and abs(z-x3)<0.1):
		print('Answers: {:0.3f},{:0.3f},{:0.3f}'.format(x1,x2,x3))
		break



