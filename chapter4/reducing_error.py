#### reducing error
weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(8):

    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
