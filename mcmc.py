import numpy as np

n_iterations = 200000 

x1_walk = empty((0)) #this is an empty list to keep all the steps
x1_0 = 8.0*((random.random())-0.5) #this is the initialization
x1_walk = append(x1_walk,x_0)
print x1_walk

x2_walk = empty((0)) #this is an empty list to keep all the steps
x2_0 = 8.0*((random.random())-0.5) #this is the initialization
x2_walk = append(x1_walk,x_0)


def nasty_function(x1, x2):
    x_0 = 3.0
    a = 0.01
    return exp((100(x2 - x1**2)**2 + (1 - x1)**2)/(-20)



for i in range(n_iterations):
    	#0.1 is the sigma in the normal distribution
	x1_prime = np.random.normal(x_walk[i], 0.1) 
	x2_prime = np.random.normal(x_walk[i], 0.1)

    	alpha = nasty_function(x1_prime, x2_prime)/nasty_function(x1_walk[i], x2_walk[i])
	
    	if(alpha=1.0):
        	x1_walk = append(x1_walk, x1_prime)
		x2_walk = append(x2_walk, x2_prime)
   	else:
       		beta = random.random()
        	if(beta<=alpha1):
            		x1_walk = append(x1_walk,x1_prime)
			x2_walk = append(x2_walk,x2_prime)
      		else:
            		x1_walk = append(x1_walk,x1_walk[i])
			x2_walk = append(x2_walk,x2_walk[i])

f = nasty_function(x1, x2)

norm = sum(f*(x1[1]-x1[0])*(x2[1)-x2[0])
plot(x1, x2, f/norm, linewidth=1, color='r')
count, bins, ignored = plt.hist(x_walk, 1000, normed=True)

#fig = figure(1, figsize=(9.5,6.5))
plt.xlabel('x1')
plt.ylabel('x2')
ax = axes()
ax.set_xlim([-4.0,4.0])
ax.set_ylim([0.0,2.0])


