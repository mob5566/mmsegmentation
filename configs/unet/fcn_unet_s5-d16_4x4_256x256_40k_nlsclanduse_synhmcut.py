_base_ = 'fcn_unet_s5-d16_4x4_256x256_40k_nlsclanduse.py'

model = dict(
    decode_head=dict(num_classes=11),
    auxiliary_head=dict(num_classes=11),
)

data = dict(
    train=dict(data_root='data/nlsclanduse.synhm_cut', ),
    val=dict(data_root='data/nlsclanduse.2001', ),
    test=dict(data_root='data/nlsclanduse.2001', ),
)
