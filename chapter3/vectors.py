vec_a = [1, 2, 3]
vec_b = [5, 6, 7]

def elementwise_multiplication(vec_a, vec_b):
    result = []
    assert(len(vec_a) == len(vec_b))
    for i in range(len(vec_a)):
        vec_result = vec_a[i] * vec_b[i]
        result.append(vec_result)
    return result

def vector_sum(vec_a):
    sum = 0
    for i in range(len(vec_a)):
        sum += vec_a[i]
    return sum


def elementwise_addition(vec_a, vec_b):
    result = []
    assert(len(vec_a) == len(vec_b))
    for i in range(len(vec_a)):
        vec_result = vec_a[i] + vec_b[i]
        result.append(vec_result)
    return result

def vector_average(vec_a):
    result = vector_sum(vec_a)/len(vec_a)
    return result


vec_multiplication = elementwise_multiplication(vec_a, vec_b)
vec__addition = elementwise_addition(vec_a, vec_b)
vec_sum = vector_sum(vec_a)
vec_average = vector_average(vec_a)

print(vec_multiplication)
print(vec__addition)
print(vec_sum)
print(vec_average)
