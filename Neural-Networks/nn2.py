"""
This is a 3-Neurons to 4-Outputs
number of outputs actually depends upon number of bias
"""

inputs = [2.3,1.2,4]
weights1= [3.4,-5.1,2.7]
weights2= [-4.3,1.5,-7.2]
weights3= [3.2,-2.1,0.4]
weights4= [-3,1,-7]
bias=[1,2,3,4]
output1= inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias[0]
output2= inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias[1]
output3= inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + bias[2]
output4= inputs[0] * weights4[0] + inputs[1] * weights4[1] + inputs[2] * weights4[2] + bias[3]
print(output1)
print(output2)
print(output3)
print(output4)

# OR
w=[weights1,weights2,weights3,weights4]
outputs=[]
for i in range(len(bias)):
    sum=0
    for j in range(len(inputs)):
        sum+=inputs[j]*w[i][j]
    outputs.append(sum+bias[i])
print(outputs)


