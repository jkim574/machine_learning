import numpy as np


def conv(inputs, filters, stride = 1):
    d_inputs = inputs.shape[1]
    d_filters = filters.shape[1]

    d_out = int((d_inputs - d_filters) / stride) + 1
    output_depths = filters.shape[0]
    output_shape = (output_depths, d_out, d_out)
   # print(output_shape)


    output = np.zeros(output_shape, dtype=int) 
#    print(output)
   # print(f"output: {output}")
  
#    print("inputs: \n", inputs)
#    print(inputs[:])
#    print(inputs[0, :3, 2:5]) 

#    print(inputs[0, 1:4, :3])
#    print(inputs[0, 1:4, 1:4])
#    print(inputs[0, 1:4, 2:5])
    
#    print(inputs[0, 2:5, :3])
#    print(inputs[0, 2:5, 1:4])
#    print(inputs[0, 2:5, 2:5])



    for i in range(d_filters): 
        curr_y = 0
        output_y = 0
        while curr_y + d_filters <= d_inputs:
            curr_x = 0
            output_x = 0
            while curr_x + d_filters <= d_inputs:
                output[i, output_x, output_y] = np.sum(inputs[:, curr_y:curr_y + d_filters, curr_x:curr_x + d_filters] * filters[i])
                curr_x += stride
                output_x += 1
            curr_y += stride
            output_y += stride
    
    conv_layer = output[0] + output[1] + output[2]
   # print(conv_layer)
    return conv_layer       
        
def max_pooling(inputs):
    size = 2
    stride = 2
    h, w = inputs.shape

    height = int((h - size) / stride) + 1
    width = int((w - size) / stride) + 1
   
#    print(inputs[:2, :2]) 
    output = np.zeros((height, width))
#    print(output)
#    print(inputs)
#    output[1, 0, 0] = np.max(inputs[:2, :2])
#    print(output)
   # print(inputs[:2, :2]) 
   # print(inputs[:2, 2:4])
   # print(inputs[2:4, 2:4])

#    print(inputs)    
#    print(inputs[:2, :2])
    curr_y = out_y = 0
    while curr_y + size <= h:
        curr_x = out_x = 0
        while curr_x + size <= w:
            output[out_y, out_x] = np.max(inputs[curr_y:curr_y + size, curr_x:curr_x + size])
            curr_x += stride
            out_x += 1
        curr_y += stride
        out_y += 1
#    print(output)
    return output

def fc(inputs):
    flatten_arr = inputs.flatten()
    fc_weight = [1, 2, 3, 4]
    output = np.dot(fc_weight, flatten_arr)

    return output 




def main():
    input_shape= (3, 5, 5)
    inputs = np.random.random(input_shape)
   # inputs = [10, 20, 30, 20, 10]
   # two_d_inputs = np.array([inputs, inputs, inputs, inputs, inputs])
   # three_d_inputs = np.array([two_d_inputs, two_d_inputs, two_d_inputs])
   # print(f"input: {inputs}")

    filter_shape = (3, 2, 2)
    filters = np.random.random(filter_shape)
   # print(f"filter: {filters}")

    conv_layer = conv(inputs, filters)
    max_pool = max_pooling(conv_layer)
    fc_layer = fc(max_pool)
    print(fc_layer)


if __name__ == "__main__":
    main()
