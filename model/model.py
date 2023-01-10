import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms as transforms

from dataset import load_data

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


def train(train_dataset):

    # Split the dataset into training and validation sets
    train_size = int(0.8 * len(train_dataset))
    val_size = len(train_dataset) - train_size
    train_dataset, val_dataset = data.random_split(train_dataset, [train_size, val_size])

    # Define the data loaders for loading the training and validation sets in batches
    train_dataloader = data.DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_dataloader = data.DataLoader(val_dataset, batch_size=32, shuffle=True)

    # Initialize the model and optimizer
    model = LeafClassifier()
    optimizer = optim.Adam(model.parameters())

    # Define the loss function and the metric for evaluating the model
    loss_fn = nn.CrossEntropyLoss()
    metric = nn.Accuracy()

    num_epochs = 30
    # Train the model
    for epoch in range(num_epochs):
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

            # Compute the metric
            metric(outputs, labels)

        # Print the metric values for the epoch
        print(f"Epoch {epoch + 1}: {metric.get_metric()}")

        # Reset the metric for the next epoch
        metric.reset()


def main():
    plants_dataset, diseases_dataset = load_data()
    train(plants_dataset)
    train(diseases_dataset)


main()
