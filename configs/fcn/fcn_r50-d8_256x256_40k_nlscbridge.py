_base_ = [
    '../_base_/models/fcn_r50-d8.py', '../_base_/datasets/nlscbridge.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(
    pretrained='torchvision://resnet50',
    backbone=dict(type='ResNet'),
    decode_head=dict(
        num_classes=2,
        loss_decode=dict(
            _delete_=True, type='LovaszLoss', classes=[1], per_image=True)),
    auxiliary_head=dict(
        num_classes=2,
        loss_decode=dict(
            _delete_=True, type='LovaszLoss', classes=[1], per_image=True)))

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])

evaluation = dict(interval=400, metric='mFscore', pre_eval=True)
