_base_ = [
    '../_base_/models/fcn_r50-d8.py', '../_base_/datasets/nlsclanduse.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(num_classes=8), auxiliary_head=dict(num_classes=8))

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])
