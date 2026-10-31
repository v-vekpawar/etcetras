"""
This is Singled layer Neural network (PERCEPTRON)
Each Neuron has its own unique value,weight,bias
This is first program of neural networks, which explains the basic formulas for neural networks
Output = (Input x Weight) + Bias
"""

# 3 Neurons to 1 Output
inputs = [1.2, 3.2, 6.4]   # these are our 3 input neurons
weights = [3, 2, 5]        # these are weights assigned to each neuron
bias = 4                   # bias is added to the weighted sum

# Output Calculation (Weighted Sum + Bias)
output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias

print(output)

'''
Imagine this as a single-layer neural network
Here, n[i] are inputs[i] (i=0,1,2)

Number of weights = Number of input neurons
Bias will always be one as all three neurons are connected to one output neuron

Diagram:

n1
  \
    \
n2 --- output
    /
  /
n3
'''