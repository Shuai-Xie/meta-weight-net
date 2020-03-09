import torch.nn as nn
from net.meta_modules import MetaModule, MetaLinear
from utils import load_model


class VNet(MetaModule):
    def __init__(self, input, hidden1, output):
        super(VNet, self).__init__()
        self.linear1 = MetaLinear(input, hidden1)
        self.relu1 = nn.ReLU(inplace=True)
        self.linear2 = MetaLinear(hidden1, output)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu1(x)
        out = self.linear2(x)
        return out.sigmoid_()


def load_vnet(ckpt_path):
    vnet = VNet(1, 100, 1).cuda()
    vnet = load_model(vnet, ckpt_path=ckpt_path)
    return vnet
