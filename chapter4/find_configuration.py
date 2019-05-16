# 1) An Empty Network
weight = 0.1
lr = 0.01

def neural_network(input, weight):
    prediction = input * weight
    return prediction

# 2) PREDICT: Making A Prediction And Evaluating Error

number_of_toes = [8.5]
win_or_lose_binary = [1] #(won!!!)

input = number_of_toes[0]
true = win_or_lose_binary[0]

pred = neural_network(input, weight)
error = (pred - true) ** 2
print(error)

# the end of the day, learning is really about one thing, adjusting our knob_weight either up or down so that our error reduces.

# 3) COMPARE: Making A Prediction With a *Higher* Weight And Evaluating Error

weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_lose_binary = [1] #(won!!!)

input = number_of_toes[0]
true = win_or_lose_binary[0]

lr = 0.01
p_up = neural_network(input,weight+lr)
e_up = (p_up - true) ** 2
print(e_up)

# 4) COMPARE: Making A Prediction With a *Lower* Weight And Evaluating Error

weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_lose_binary = [1] #(won!!!)

input = number_of_toes[0]
true = win_or_lose_binary[0]

lr = 0.01
p_dn = neural_network(input,weight-lr)
e_dn = (p_dn - true) ** 2
print(e_dn)

# This reveals what learning in neural networks really is. It's a search problem.
