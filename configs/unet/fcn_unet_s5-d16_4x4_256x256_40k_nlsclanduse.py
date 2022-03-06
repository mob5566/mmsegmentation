_base_ = [
    '../_base_/models/fcn_unet_s5-d16.py', '../_base_/datasets/nlsclanduse.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]

model = dict(
    decode_head=dict(num_classes=9),
    auxiliary_head=dict(num_classes=9)
)

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)
