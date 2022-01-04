"""
GA: Solving Knapsack problem using Genetic Algorithm
Four items are there. The weights are 2,4,4,6 Kg., and associated values are
$ 4,10,12,3. The weight constraint is 8 Kg. 
The best result is 0,1,1,0 where the total value is $22
"""
import numpy as np

w = [2,4,4,6] # Weights
v = [4,10,12,3] # Values

weight = 8 # Constraint
col = 4 # Total number of items
row = 4 # Total number of individuals

print("The weights and values are: ")
print("Weights: ", w)
print("Values: ", v)

rand_pop = np.random.randint(0,2,(row,col)) 
rand_popTemp = np.random.randint(0,2,(row,col))

addZeros = np.zeros((row,4))
rand_pop = np.append(rand_pop, addZeros, axis=1)

# Main iteration starts from here
maxVal = 0
capIndividual = []
for itr in range(200): # Iterate the whole process
    print("\nIteration no:",itr+1)
        
    for i in range(4):
        sumWeight = sum(np.multiply(w, rand_pop[i,0:col])) # Total weight calculation
        rand_pop[i,col] = sumWeight
        sumValue = sum(np.multiply(v, rand_pop[i,0:col])) # Total value calculation
        
        if sumWeight>weight: # Constraint checking
            sumValue = 0
            rand_pop[i,col+1] = sumValue
            continue
        
        rand_pop[i,col+1] = sumValue
        
        if maxVal<sumValue:
            maxVal = sumValue
            capIndividual = rand_pop[i,0:col]
        
    print("The initial population: \n",rand_pop[:,0:col])
    
    # Fitness(i) calculation
    for i in range(row):
        rand_pop[i,col+2] = rand_pop[i,col+1]/np.average(rand_pop[:,col+1])
        rand_pop[i,col+3] = round(rand_pop[i,col+2])
        
    print("The weights & values of the individuals: \n", rand_pop[:,col:col+4].tolist())
    print("\nThe sum is: ",sum(rand_pop[:,col+1]))
    print("The average is: ",np.average(rand_pop[:,col+1]))

    # Next generation formation
    count = 0
    c = 0
    for i in range(row):
        noc = rand_pop[i,7]
        count +=noc
        if count>row:
            noc -=1
            
        for j in range(int(noc)):
            rand_popTemp[c] = rand_pop[i,0:col]
            c +=1
    rand_pop[:,0:col] = rand_popTemp
    
    print("\nThe next generation: \n",rand_pop[:,0:col])
    
    # Crossover starts 
    # Random selection of indices for crossover
    dup = np.array([])
    while 1:
        ranIndex = np.random.randint(low=0, high=row, size=2)
        u, c = np.unique(ranIndex, return_counts=True)
        dup = u[c > 1]
        if dup.size == 0:
            break
    print("Randomly two individuals are selected: ")
   
    c = 0
    for i in ranIndex:
        rand_popTemp[c] = rand_pop[i,0:col]
        c += 1
        
    k = np.random.randint(low=1, high=col, size=1) # Identification of crossover site randomly
    print("The crossite is: ",int(k))
    print("Before crossover: \n",rand_popTemp[0:2])
    
    a = []
    b =[]
    a = rand_popTemp[0,int(k):col].tolist()
    b = rand_popTemp[1,int(k):col].tolist()
    rand_popTemp[1,int(k):col] = a
    rand_popTemp[0,int(k):col] = b
    print("After crossover: \n",rand_popTemp[0:2])
    
    c = 0
    for i in ranIndex:
        rand_pop[i,0:col] = rand_popTemp[c]
        c += 1
    
    print("\nThe next generation after crossover: \n",rand_pop[:,0:col])
    
    # Mutation starts
    rand_r = int(np.random.randint(0,row,(1,1))) 
    rand_c = int(np.random.randint(0,col,(1,1))) 
    print("Position of the bit to mutate: [",rand_r,",",rand_c,"]")
    rand_pop[rand_r,rand_c] = 1-int(rand_pop[rand_r,rand_c])
    print("\nAfter mutation: \n",rand_pop[:,0:col])
    
    print("The individual is: ",capIndividual,"and the best value is",maxVal) 