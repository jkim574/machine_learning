import numpy as np
import math


def sigmoid(number):
    sig = 1 / (1 + math.exp(-number))
    return sig


def feed_forward(inputs, w1, w2):
    hidden_layer = np.dot(w1, inputs)
    print(f"hidden_layer: {hidden_layer}") 
    
    new_inputs = []
    for i in range(len(hidden_layer)):
        num = sigmoid(hidden_layer[i])
        new_inputs.append(num)

    print(f"activation value: {new_inputs}")   

    output_layer = np.dot(w2, new_inputs)
    return output_layer


def main():
    # 3 x 3 x 1 fully connected network consisting of input layer (3), layer1 (3), and output_layer (1)
    inputs = [10, 20, 30]
    layer1_weights = [[1,2,3], [4,5,6], [7,8,9]]
    output_layer_weights = [[11, 12, 13], [13, 14, 15]]
    predict = feed_forward(inputs, layer1_weights, output_layer_weights)
    
    print(predict)


if __name__ == "__main__":
    main()
