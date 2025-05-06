import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv_1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(8)
        )

        self.pool_1 = nn.MaxPool2d(2, 2)

        self.conv_2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=20, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(20)
        )

        self.pool_2 = nn.MaxPool2d(2, 2)

        self.conv_3 = nn.Sequential(
            nn.Conv2d(in_channels=20, out_channels=10, kernel_size=1, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(10)
        )

        self.pool_3 = nn.MaxPool2d(2, 2)

        self.conv_4 = nn.Sequential(
            nn.Conv2d(in_channels=10, out_channels=20, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(20)
        )

        self.conv_5 = nn.Sequential(
            nn.Conv2d(in_channels=20, out_channels=32, kernel_size=1, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(32)
        )

        self.conv_6 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=10, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(10)
        )

        self.conv_7 = nn.Sequential(
            nn.Conv2d(in_channels=10, out_channels=10, kernel_size=1, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(10)
        )

        self.conv_8 = nn.Sequential(
            nn.Conv2d(in_channels=10, out_channels=14, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(14)
        )

        self.conv_9 = nn.Sequential(
            nn.Conv2d(in_channels=14, out_channels=16, kernel_size=3, padding=0, bias=True),
            nn.ReLU(),
            nn.BatchNorm2d(16)
        )

        self.gap = nn.Sequential(nn.AvgPool2d(kernel_size=4))

        self.conv_out = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=2, kernel_size=4, padding=0, bias=True)
        )

    def forward(self, x):
        x = self.conv_out(self.gap(
                self.conv_9(self.conv_8(
                    self.conv_7(self.conv_6(
                        self.conv_5(self.conv_4(
                            self.pool_3(self.conv_3(
                                self.pool_2(self.conv_2(
                                    self.pool_1(self.conv_1(x))
                                ))
                            ))
                        ))
                    ))
                ))
            ))
        
        return F.log_softmax(x.view(-1, 2), dim=1)
    