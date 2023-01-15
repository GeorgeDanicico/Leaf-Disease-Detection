import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms as transforms

from dataset import load_data

global model
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


class LeafClassifier(nn.Module):
    def __init__(self, output_classes_count):
        self.output_classes_count = output_classes_count
        super(LeafClassifier, self).__init__()

        # Define the convolutional layers
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        # Define the fully connected layers
        self.fc1 = nn.Linear(128, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 64)

        # Define the final classification layer
        self.classifier = nn.Linear(64, output_classes_count)

    def forward(self, x):
        x = self.conv1(x)
        x = nn.ReLU(x)
        x = nn.MaxPool2d(x)

        x = self.conv2(x)
        x = nn.ReLU(x)
        x = nn.MaxPool2d(x)

        x = self.conv3(x)
        x = nn.ReLU(x)
        x = nn.MaxPool2d(x)

        # Flatten the output of the convolutional layers
        x = x.view(x.size(0), -1)

        x = self.fc1(x)
        x = nn.ReLU(x)

        x = self.fc2(x)
        x = nn.ReLU(x)

        x = self.fc3(x)
        x = nn.ReLU(x)

        x = self.fc4(x)
        x = nn.ReLU(x)

        # Apply the final classification layer
        x = self.classifier(x)

        return x


def test(valid_dataset):
    model.eval()
    valid_dataloader = data.DataLoader(valid_dataset, batch_size=32, shuffle=True)

    correct = 0
    total = 0
    for inputs, labels in valid_dataloader:
        valid_input, valid_label = inputs.to(device), labels.to(device)
        output = model(valid_input)
        _, predicted = torch.max(output.data, 1)
        total += valid_label.size(0)
        correct += (predicted == valid_label).sum().item()

    print('Test Acc: {:.2f}%'.format(100 * correct / total))


def train(train_dataset):

    # Define the data loader for loading the training set in batches
    train_dataloader = data.DataLoader(train_dataset, batch_size=32, shuffle=True)

    # Initialize the model and optimizer
    optimizer = optim.Adam(model.parameters())

    # Define the loss function and the metric for evaluating the model
    loss_fn = nn.CrossEntropyLoss()
    metric = nn.Accuracy()

    train_acc = 0.0
    train_loss = 0.0
    num_epochs = 30
    # Train the model
    for epoch in range(num_epochs):
        model.train()
        for inputs, labels in train_dataloader:
            # Move the input and label tensors to the correct device
            inputs = inputs.to(device)
            labels = labels.to(device)

            # Zero out the gradients from the previous iteration
            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)
            loss = loss_fn(outputs, labels)

            # Backward pass
            loss.backward()

            # Update the model parameters
            optimizer.step()

            train_loss += loss.cpu().data.item() * inputs.size(0)
            _, prediction = torch.max(outputs.data, 1)
            train_acc += torch.sum(prediction == labels.data)

            # Compute the metric
            metric(outputs, labels)

        # Print the metric values for the epoch
        print(f"Epoch {epoch + 1}: {metric.get_metric()}")

        # Reset the metric for the next epoch
        metric.reset()


def main():
    global model
    plants_dataset, diseases_dataset = load_data('/Volumes/PortableSSD/dataset/plants/plants/train')
    valid_plants_dataset, valid_disease_dataset = load_data('/Volumes/PortableSSD/dataset/plants/plants/valid')
    model = LeafClassifier(len(plants_dataset))
    train(plants_dataset)
    test(valid_plants_dataset)
    train(diseases_dataset)
    test(diseases_dataset)


main()
