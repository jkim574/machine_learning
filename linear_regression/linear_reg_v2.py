import matplotlib.pyplot as plt


def train_model(x, y, weight, lr):
    
    n = len(x)
    summation = 0
    epoch = 1 
    loss = mean_square_error(weight, x, y, n)
    loss_list = []
    epoch_list = []
    loss_list.append(loss)
    epoch_list.append(epoch)
    print(f"Epoch: {epoch} loss: {loss}")
    for i in range(n):
        cost = (weight * x[i] - y[i]) * x[i]
        summation += cost
    gradient = summation / n 

    new_weight = weight - lr * gradient
    

#    print("weight: ", weight)
#    print("new_weight: ", new_weight)   

 
    while new_weight != weight:
        
        weight = new_weight
        summation = 0
        loss = mean_square_error(weight, x, y, n)
        for i in range(n):
            cost = (new_weight * x[i] - y[i]) * x[i]
            summation += cost
        epoch += 1
        loss_list.append(loss)
        epoch_list.append(epoch)
        print(f"Epoch: {epoch} loss: {loss}")
        gradient = summation / n
        new_weight = new_weight - lr * gradient
    
    plt.plot(epoch_list, loss_list)
    plt.show()
    return new_weight
    
#        print(weight)
#        print(new_weight)


def mean_square_error(weight, x, y, m):
    summation = 0
    for i in range(m):
        diff = (weight * x[i]) - y[i]
        square = diff ** 2
        summation += square
    
    mse = summation / (2 * m)
    return mse
    
    
 
"""
    for i in range(n):
        estimated_y_val = weight * x[i]
        estimated_y_list.append(estimated_y_val)

    for j in range(n):
        summation = summation + ((estimated_y_list[j] - y[j]) * x[j])
    gradient = summation / n
    new_weight = weight - lr * gradient



    while new_weight != weight:
        for i in range(n):
            summation = summation + ((new_weight * x[i] - y[i]) * x[i])
        gradient = summ / n
        new_weight = weight - lr * gradient    

"""

#    gradient = (estimated_y_list[i] - y[i]) * x[i]
#    new_weight = weight - (lr * gradient)    

#    return gradient 

#    updated_weight = weight - (lr * gradient)     
#    while updated_weight != weight:
#        for i in range(n):
#            gradient = ((estimated_y_list[i] - y[i]) * x[i]) / n

#        updated_weight =  

def inference(new_x, weight):
    output = weight * new_x
    return output


def main():
    x = [2, 4, 3, 7, 9, 1, 7, 8]
    y = [20, 38, 37, 67, 92, 20, 83, 93]
    weight = 3
    learning_rate = 0.001
    
    best_weight = train_model(x, y, weight, learning_rate) 
    print("best_weight is: ", best_weight)
    
#    y = 10.78x
    x_val = 10
    predict_y = inference(x_val, best_weight)
    print("if x is 10, then y is: ", predict_y)

    


if __name__ == "__main__":
    main()
