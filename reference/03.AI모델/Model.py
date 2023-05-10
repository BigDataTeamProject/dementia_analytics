import torch
import torch.nn as nn
from torchvision.models import resnet101
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

class RRNN(nn.Module):
    def __init__(self, day_length, hidden_size, day_hidden_size):
        super(RRNN, self).__init__()
        self.lstm1 = nn.LSTM(4, day_hidden_size, num_layers=1, bias=True, batch_first=True,
                            dropout=0, bidirectional=True)
        self.lstm2 = nn.LSTM(44+2*day_hidden_size, hidden_size, num_layers=1, bias=True, batch_first=True,
                            dropout=0, bidirectional=True)
        self.fc = nn.Linear(2*hidden_size, 2)
        self.day_length = day_length
        self.day_hidden_size = day_hidden_size
        self.hidden_size = hidden_size
    def init_hidden(self, batch_size, hidden_size):
        return (Variable(torch.randn(2, batch_size, hidden_size)).cuda(),
                Variable(torch.randn(2, batch_size, hidden_size)).cuda())

    def forward(self, x, d_):
        input_storage = []
        for i in range(x.shape[1]):
            self.hidden = self.init_hidden(x.shape[0], self.day_hidden_size)
            x_day = x[:, i, :, :]
            x_day = torch.transpose(x_day, 1,2)
            x_day, h = self.lstm1(x_day, self.hidden)
            x_day = torch.split(x_day, self.day_hidden_size, dim=2)
            x_day = torch.cat([x_day[0][:, -1, :], x_day[1][:, 0, :]], dim=1)
            input_storage.append(x_day)
        f = torch.stack(input_storage, dim=1).squeeze(dim=2)
        mix_f = torch.cat([f, d_], dim=2)
        self.hidden = self.init_hidden(mix_f.shape[0], self.hidden_size)
        xx, h = self.lstm2(mix_f, self.hidden)
        xx = torch.split(xx, self.hidden_size, dim=2)
        xx = torch.cat([xx[0][:, -1, :], xx[1][:, 0, :]], dim=1)
        out = self.fc(xx)

        return out



