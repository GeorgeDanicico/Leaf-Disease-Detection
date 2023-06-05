from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import os
# read stats from file
input_file = "/Volumes/PortableSSD/Thesis/USE_RESULTS/4june_simple_diseases"
files = ['loss.txt', 'accuracy.txt', 'val_loss.txt', 'val_accuracy.txt']
mtl_files = ["task_1_output_accuracy.txt", "task_1_output_loss.txt", "task_2_output_accuracy.txt", "task_2_output_loss.txt",
                  "val_task_1_output_accuracy.txt", "val_task_1_output_loss.txt", "val_task_2_output_accuracy.txt", "val_task_2_output_loss.txt"]
loss = []
val_loss = []
accuracy = []
val_accuracy = []
statistics = [loss, accuracy, val_loss, val_accuracy]

# task_1_output_accuracy = []
# task_1_output_loss=[]
# task_2_output_accuracy=[]
# task_2_output_loss=[]
# val_task_1_output_accuracy=[]
# val_task_2_output_accuracy=[]
# val_task_1_output_loss=[]
# val_task_2_output_loss=[]
#
# mtl_statistics = [task_1_output_accuracy, task_1_output_loss, task_2_output_accuracy, task_2_output_loss,
#                   val_task_1_output_accuracy, val_task_1_output_loss, val_task_2_output_accuracy, val_task_2_output_loss]

for i in range(0, len(files)):
    file_path = os.path.join(input_file, files[i])
    print(file_path)
    with open(file_path, 'r') as f:
        while line := f.readline():
            value = float(line)
            # mtl_statistics[i].append(value)
            statistics[i].append(value)

# for i in range(0, len(mtl_files)):
#     file_path = os.path.join(input_file, mtl_files[i])
#     print(file_path)
#     with open(file_path, 'r') as f:
#         while line := f.readline():
#             value = float(line)
#             mtl_statistics[i].append(value)

# plot stats
plt.subplot(212)
plt.title('Loss')
plt.plot(loss, label='train')
plt.plot(val_loss, label='valid')
plt.legend()
plt.show()

plt.subplot(212)
plt.title('Accuracy')
plt.plot(accuracy, label='train')
plt.plot(val_accuracy, label='valid')
plt.legend()
plt.show()

# plt.plot(task_1_output_loss, c='r',label='Task 1')
# plt.plot(task_2_output_loss, c='b',label='Task 2')
# plt.plot(val_task_1_output_loss, c='g',label='Valid Task 1')
# plt.plot(val_task_2_output_loss, c='y',label='Valid Task 2')
#
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()
#
# plt.plot(task_1_output_accuracy, c='r',label='Task 1')
# plt.plot(task_2_output_accuracy, c='b',label='Task 2')
# plt.plot(val_task_1_output_accuracy, c='g',label='Valid Task 1')
# plt.plot(val_task_2_output_accuracy, c='y',label='Valid Task 2')
#
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.show()