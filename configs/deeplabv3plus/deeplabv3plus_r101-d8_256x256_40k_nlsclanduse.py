_base_ = './deeplabv3plus_r50-d8_256x256_40k_nlsclanduse.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
