import torch
import torch.nn as nn
import torch.nn.functional as F


class LSTM(nn.Module):
    
    def __init__(self, input_size, rnn_size, num_layers, dropout):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.rnn_size = rnn_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size, rnn_size, num_layers, dropout=dropout)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(rnn_size, input_size)
    
    def forward(self, input, hidden):
        output, hidden = self.lstm(input, hidden)
        output = self.dropout(output)
        output = self.fc(output)
        return output, hidden

    def init_hidden(self, batch_size, device):
        return (torch.zeros(self.num_layers, batch_size, self.rnn_size).to(device),
                torch.zeros(self.num_layers, batch_size, self.rnn_size).to(device))
