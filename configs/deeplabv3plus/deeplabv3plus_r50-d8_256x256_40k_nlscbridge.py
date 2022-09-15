_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/nlscbridge.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(
        num_classes=2,
        loss_decode=dict(
            _delete_=True, type='LovaszLoss', classes=[1], per_image=True)),
    auxiliary_head=dict(
        num_classes=2,
        loss_decode=dict(
            _delete_=True, type='LovaszLoss', classes=[1], per_image=True)))
# optimizer = dict(type='SGD', lr=0.004, momentum=0.9, weight_decay=0.0001)

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])

evaluation = dict(interval=400, metric='mFscore', pre_eval=True)
