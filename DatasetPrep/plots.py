import matplotlib.pyplot as plt
import os
# read stats from file
input_file = "/Volumes/PortableSSD/Thesis/results/17march_classes_inceptionv3"
files = ['loss.txt', 'accuracy.txt', 'val_loss.txt', 'val_accuracy.txt']
loss = []
val_loss = []
accuracy = []
val_accuracy = []
statistics = [loss, accuracy, val_loss, val_accuracy]

for i in range(0, len(files)):
    file_path = os.path.join(input_file, files[i])
    print(file_path)
    with open(file_path, 'r') as f:
        while line := f.readline():
            value = float(line)
            statistics[i].append(value)


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