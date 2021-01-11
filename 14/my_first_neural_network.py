"""
Function: my first neural network
Coding: utf-8
Author: Sun Yuexin
Date: 2021/01/04
"""
import numpy as np

np.random.seed(1)
f = open("log.txt", mode="a+", encoding="utf-8")


def relu(x):
    return (x > 0) * x


def relu2deriv(output):
    return output > 0


street_lights = np.array([[1, 0, 1],
                          [0, 1, 1],
                          [0, 0, 1],
                          [1, 1, 1]])
walk_vs_stop = np.array([[1, 1, 0, 0]]).T

alpha = 0.2
hidden_size = 4
counter = 1

weight_0_1 = 2 * np.random.random((3, hidden_size)) - 1
weight_1_2 = 2 * np.random.random((hidden_size, 1)) - 1

for iteration in range(60):
    layer_2_error = 0
    for i in range(len(street_lights)):
        layer_0 = street_lights[i:i + 1]
        layer_1 = relu(np.dot(layer_0, weight_0_1))
        layer_2 = np.dot(layer_1, weight_1_2)
        f.write("%d" % i)
        f.write("\n" + "*" * 30 + "\n\n")
        f.write("weight_0_1:" + str(weight_0_1) + "\n")
        f.write("weight_1_2:" + str(weight_1_2) + "\n")
        f.write("light_status(layer_0):" + str(layer_0) + "\n")
        f.write("hidden_layer_non_relu(layer_1_n):" + str(np.dot(layer_0, weight_0_1)) + "\n")
        f.write("hidden_layer(layer_1):" + str(layer_1) + "\n")
        f.write("prediction_layer(layer_2):" + str(layer_2) + "\n")

        layer_2_error += np.sum((layer_2 - walk_vs_stop[i]) ** 2)
        f.write("layer_2_error_individual:" + str(((layer_2 - walk_vs_stop[i]) ** 2)) + "\n")
        f.write("layer_2_sum:" + str(layer_2_error) + "\n")

        layer_2_delta = layer_2 - walk_vs_stop[i:i + 1]
        layer_1_delta = layer_2_delta.dot(weight_1_2.T) * relu2deriv(layer_1)
        f.write("layer_2_delta：" + str(layer_2_delta) + "\n")
        f.write("weight_1_2.T：" + str(weight_1_2.T) + "\n")
        f.write("hidden_layer(layer_1):" + str(layer_1) + "\n")
        f.write("relu2deriv(layer_1): " + str(relu2deriv(layer_1)) + "\n")
        f.write("layer_1_delta: " + str(layer_1_delta) + "\n")

        weight_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
        weight_0_1 -= alpha * layer_0.T.dot(layer_1_delta)
        f.write("weight_1_2:" + str(weight_1_2) + "\n")
        f.write("weight_0_1:" + str(weight_0_1) + "\n")
        i += 1

    if iteration % 10 == 9:
        print("Error: " + str(layer_2_error))  
f.close()
