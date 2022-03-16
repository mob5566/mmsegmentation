_base_ = './fcn_r50-d8_256x256_40k_nlsclanduse.py'
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(type='ResNet', depth=101)
)
