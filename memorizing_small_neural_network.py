weight, goal_predict, input = (0.0, 0.8, 2)
alpha = 0.1
for interation in range(20):
    prediction = input * weight
    error = (prediction - goal_predict) ** 2
    derivative = input * (prediction - goal_predict)
    weight = weight - (alpha * derivative)
    print("error:" + str(error))
    print("prediction:" + str(prediction))
