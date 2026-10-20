import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split

class CustomDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.tensor(features, dtype = torch.float32)
        self.labels = torch.tesnor(labels, dtype = torch.long)
    def __len__(self):
        return len(self.features)
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

class Model(nn.Module):
    def __init__(self,input_dim, output_dim, num_hidden_layers, neurons_per_layer):
        super().__init__()
        layers =[]
        for i in range(num_hidden_layers):
            layers.append(nn.Linear(input_dim, neurons_per_layer))
            layers.append(nn.BatchNorm1d(neurons_per_layer))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(0.3))
            input_dim = neurons_per_layer
        layers.append(nn.Linear(neurons_per_layer, output_dim))
        self.model = nn.Sequential(*layers)
    def forward(self, x):
        return self.model(x)


df = pd.read_csv("./sin_data.csv")
X = df["X"].values
y = df["y"].values
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
X_train = torch.tensor(X_train, dtype= torch.float32).unsqueeze(1)
y_train = torch.tensor(y_train, dtype= torch.float32).unsqueeze(1)
X_test = torch.tensor(X_test, dtype= torch.float32).unsqueeze(1)
y_test = torch.tensor(y_test, dtype= torch.float32).unsqueeze(1)

