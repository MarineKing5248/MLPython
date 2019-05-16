# 1) An Empty Network
weight = 0.1
alpha = 0.01

def neural_network(input, weight):
    prediction = input * weight
    return prediction

# 2) PREDICT: Making A Prediction And Evaluating Error

number_of_toes = [8.5]
win_or_lose_binary = [1] # (won!!!)

input = number_of_toes[0]
goal_pred = win_or_lose_binary[0]

pred = neural_network(input,weight)
error = (pred - goal_pred) ** 2

# 3) COMPARE: Calculating "Node Delta" and Putting it on the Output Node

delta = pred - goal_pred

# 4) LEARN: Calculating "Weight Delta" and Putting it on the Weight

weight_delta = input * delta

# 5) LEARN: Updating the Weight

alpha = 0.01 # fixed before training
weight -= weight_delta * alpha


#### reducing error
weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(8):

    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
