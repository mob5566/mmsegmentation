_base_ = [
    '../_base_/models/fcn_unet_s5-d16.py', '../_base_/datasets/nlsclanduse.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]

model = dict(
    decode_head=dict(num_classes=8),
    auxiliary_head=dict(num_classes=8),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole')
)

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])
