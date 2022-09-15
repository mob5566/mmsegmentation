_base_ = [
    '../_base_/models/lraspp_m-v3-d8.py', '../_base_/datasets/nlscbridge.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]

model = dict(
    pretrained='open-mmlab://contrib/mobilenet_v3_large',
    decode_head=dict(
        num_classes=2,
        loss_decode=dict(
            _delete_=True, type='LovaszLoss', classes=[1], per_image=True)))

# Re-config the data sampler.
data = dict(samples_per_gpu=4, workers_per_gpu=4)

runner = dict(type='IterBasedRunner', max_iters=320000)

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])

evaluation = dict(interval=400, metric='mFscore', pre_eval=True)
