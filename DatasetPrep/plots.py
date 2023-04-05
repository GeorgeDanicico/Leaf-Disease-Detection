from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import os
# read stats from file
# input_file = "/Volumes/PortableSSD/Thesis/results/17march_classes_inceptionv3"
# files = ['loss.txt', 'accuracy.txt', 'val_loss.txt', 'val_accuracy.txt']
# loss = []
# val_loss = []
# accuracy = []
# val_accuracy = []
# statistics = [loss, accuracy, val_loss, val_accuracy]
#
# for i in range(0, len(files)):
#     file_path = os.path.join(input_file, files[i])
#     print(file_path)
#     with open(file_path, 'r') as f:
#         while line := f.readline():
#             value = float(line)
#             statistics[i].append(value)


# # plot stats
# plt.subplot(212)
# plt.title('Loss')
# plt.plot(loss, label='train')
# plt.plot(val_loss, label='valid')
# plt.legend()
# plt.show()
#
# plt.subplot(212)
# plt.title('Accuracy')
# plt.plot(accuracy, label='train')
# plt.plot(val_accuracy, label='valid')
# plt.legend()
# plt.show()

# rectified linear function
def rectified(x):
    return max(0.0, x)

def sigmoid(x):
	return 1.0 / (1.0 + exp(-x))

def tanh(x):
 return (exp(x) - exp(-x)) / (exp(x) + exp(-x))


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


# define input data
inputs = [x for x in range(-10, 10)]
# calculate outputs
outputs = softmax(inputs)
# plot inputs vs outputs
plt.plot(inputs, outputs)
plt.show()