import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])

# tran_set = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=True)
# test_set = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True)

# img, target = test_set[0]
# img.show()

tran_set = torchvision.datasets.CIFAR10(root='./dataset', train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root='./dataset', train=False, transform=dataset_transform, download=True)

writer = SummaryWriter("logs")
for i in range(10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)
writer.close()
