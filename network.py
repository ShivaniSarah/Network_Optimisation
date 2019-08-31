# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Network _Optimisation.csv')

# Implementing UCB
import math
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward
    


temp = sums_of_rewards

my_list = []

for i in range(len(sums_of_rewards)):
    ind = sums_of_rewards.index(max(temp))
    my_list.append(ind)
    temp[ind] = -1

my_list.reverse()

print("Nodes in increasing order of congestion",my_list)

# Python program to print all paths from a source to destination. 
   
from collections import defaultdict 


score=[]  
#This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices
        self.count = 0
        self.list=[]
     
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def send(self,path1):
        sum=0
        
        for i in path1:
           for j in my_list:
              if( i==j):
                 z=my_list.index(j)
                 sum=sum+z+1
        return(sum)
          
    def printAllPathsUtil(self, u, d, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
        
        # If current vertex is same as destination, then print 
        # current path[] 
        if u ==d: 
            print(self.count+1," ",
            path)
            m=self.send(path)
            score.append(m)
            self.count += 1
            
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d,visited, path) 
        

# Create a graph given in the above diagram 
g = Graph(10) 
g.addEdge(0,1)
g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,0)
g.addEdge(0,3)
g.addEdge(3,0)
g.addEdge(1,4)
g.addEdge(4,1)
g.addEdge(2,4)
g.addEdge(4,2)
g.addEdge(2,5)
g.addEdge(5,2)
g.addEdge(3,5)
g.addEdge(5,3)
g.addEdge(4,6)
g.addEdge(6,4)
g.addEdge(4,7)
g.addEdge(7,4)
g.addEdge(5,7)
g.addEdge(7,5)
g.addEdge(5,8)
g.addEdge(8,5)
g.addEdge(6,9)
g.addEdge(9,6)
g.addEdge(7,9)
g.addEdge(9,7)
g.addEdge(8,9)
g.addEdge(9,8)

s = 0 ; d = 9
print ("Following are all different paths from %d to %d :" %(s, d)) 
g.printAllPaths(s, d)
 
print("Total possible paths =",g.count)
print(score)
print("Optimal path is:",score.index(min(score))+1)


