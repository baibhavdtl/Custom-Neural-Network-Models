import random 
dropout_rate = 0.5
example_output = [0.27,-1.03, 0.67, 0.99, 0.05, -0.37, -2.01, 1.13, -0.07, 0.73]
while True:
    index = random.randInt(0, len(example_output)-1)
    example_output[index] = 0
    dropped_out = 0
    for value in example_output:
        if value == 0:
            dropped_out+=1

        if dropped_out / len(example_output) >= dropout_rate:
            break
print(example_output)
