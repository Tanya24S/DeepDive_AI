#Book-Machine Learning with python cookbook-Chris Albon (Oreilly)
#(This book covers all basic operations that we'll require in Ml workflow.)
#A few ML terms: Parameter-weights or coefficients learned through training, Hyperparamete- is a setting, or values set before the training of the model.
#Train- apply algo to data using numerical approaches such as gradient descent, Fit- apply algo to data using analytical approach.
#Difference between Numerical approach and analytical approach: Numerical- iterative algo to approximate solution(faster for larger dataset)
                                                               #Analytical-provide exact solution using mathematical formula or expression(fast for small datasets, computationally expensive and slow for large datasets).
#NumPy- it is basically used for handling data structures that are often used in python such as vectors, matrices and tensors.
#1.Creating a vector: NumPy's main structure is multidimensional array so to create vector we just create 1D array)
import numpy as np
vector_row= np.array([1,2,3]) #create vector as a row
vector_column= np.array([1], [2], [3]) #create vector as a column
