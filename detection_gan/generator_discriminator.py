import torch
import numpy as np

class Generator(torch.nn.Module):
    def __init__(self, layer_sizes, output_size, scales_size):
        super(Generator, self).__init__()
        layer_sizes[0] = layer_sizes[0] + scales_size
        for idx, layer_dim in enumerate(layer_sizes):
            if idx == 0:
                continue
            setattr(self, f'linear_{idx}', torch.nn.Linear(layer_sizes[idx-1], layer_sizes[idx]))
        self.layer_sizes = layer_sizes
        self.input_size = layer_sizes[0]
        self.output_size = output_size
    
    def forward(self, x, scales):
        for idx, layer_dim in enumerate(self.layer_sizes[:-1]):
            if idx == 0:
                continue
            x = torch.nn.functional.relu(getattr(self, f'linear_{idx}')(x))
        x = torch.nn.functional.sigmoid(getattr(self, f'linear_{len(self.layer_sizes)}')(x))
        return x

class Discriminator(torch.nn.Module):
    def __init__(self, layer_sizes, output_size):
        layer_sizes[0] = layer_sizes[0] + scales_size
        super(Discriminator, self).__init__()
        for idx, layer_dim in enumerate(layer_sizes):
            if idx == 0:
                continue
            setattr(self, f'linear_{idx}', torch.nn.Linear(layer_sizes[idx-1], layer_sizes[idx]))
        self.layer_sizes = layer_sizes
        self.input_size = layer_sizes[0]
        self.output_size = output_size
    
    def forward(self, x, scales):
        for idx, layer_dim in enumerate(self.layer_sizes[:-1]):
            if idx == 0:
                continue
            x = torch.nn.functional.relu(getattr(self, f'linear_{idx}')(x))
        x = torch.nn.functional.sigmoid(getattr(self, f'linear_{len(self.layer_sizes)}')(x))
        return x