def deriv_cost_func(x, y, param):
    estimated_y = []
    n = len(x)
    summation = 0
    for i in range(n):
        new_y = param * x[i]
        estimated_y.append(new_y)
    
    for i in range(n):
        difference = estimated_y[i] - y[i]
        new_value = difference * x[i]
        summation = summation + new_value 
   #     squared_diff = difference ** 2 
    
    return summation

def gradient_descent(param, lr, loss):
    updated_param = param - (lr * loss)
    print("old_param: ", param)
    print("updated_param: ", updated_param)

    if updated_param == param:
#        print("old_param: ", param)
#        print("updated_param: ", updated_param)
        return updated_param
    else:
        new = gradient_descent(updated_param, lr, loss)
 

def main():
#    study_time = [3, 7, 1, 4, 4, 9, 2, 3, 13, 10]
#    score = [30, 70, 10, 40, 45, 80, 30, 35, 98, 92]
    study_time = [1, 3, 5, 7]
    score = [2, 10, 34, 99]
    param = 1
    learning_rate = 0.01
    
    loss = deriv_cost_func(study_time, score, param)
    min_param = gradient_descent(param, learning_rate, loss)

if __name__ == "__main__":
    main() 



