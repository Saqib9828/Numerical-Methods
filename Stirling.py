import numpy as np

def p_cal_gauss_forward(p, n): 

	temp = p; 
	for i in range(1, n): 
         if(i%2==1):
             temp * (p - i)
         else:
             temp * (p + i)
	return temp;

def p_cal_gauss_backward(p, n): 

	temp = p; 
	for i in range(1, n): 
         if(i%2==1):
             temp * (p + i)
         else:
             temp * (p - i)
	return temp; 

def fact(n): 
	f = 1 
	for i in range(2, n + 1): 
		f *= i
	return f 


n = 7; 
x = [ 1, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30 ]; 
	

y = [[0 for i in range(n)] 
		for j in range(n)]; 
y[0][0] = 2.7183; 
y[1][0] = 2.8577; 
y[2][0] = 3.0042;
y[3][0] = 3.1582;  
y[4][0] = 3.3201; 
y[5][0] = 3.4903; 
y[6][0] = 3.6693; 


for i in range(1, n): 
	for j in range(n - i): 
		y[j][i] = np.round((y[j + 1][i - 1] - y[j][i - 1]),4); 


for i in range(n): 
	print(x[i], end = "\t"); 
	for j in range(n - i): 
		print(y[i][j], end = "\t"); 
	print(""); 


value = 1.14; 


#sum = y[int(np.ceil(n/2))][0]; 
sum = y[int(n/2)][0]; 
p = (value - x[int(n/2)]) / (x[1] - x[0])
#print("a:",int(np.ceil(n/2)))
print(p)
for i in range(1,n):
    y_row_index_gauss_forward=int((n-i)/2)
    if(i%2==1):
        y_row_index_gauss_backward=int((n-i)/2)-1
        #print(y[int((n-i)/2)-1][i])
    else:
        y_row_index_gauss_backward=int((n-i)/2)
        #print(y[int((n-i)/2)][i])
    sum = sum + (
                     (
                        (p_cal_gauss_backward(p, i) + (p_cal_gauss_forward(p, i)))/2
                     )
                        * 
                    (
                        (y[y_row_index_gauss_backward][i] + y[y_row_index_gauss_forward][i])/2
                     )
                    
                ) / fact(i)

print("\nValue at", value, 
	"is", round(sum, 4)); 


