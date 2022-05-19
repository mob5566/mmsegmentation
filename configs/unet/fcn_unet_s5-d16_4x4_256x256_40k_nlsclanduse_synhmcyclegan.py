_base_ = 'fcn_unet_s5-d16_4x4_256x256_40k_nlsclanduse.py'

data = dict(
    train=dict(data_root='data/nlsclanduse.synhm_cyclegan', ),
    val=dict(data_root='data/nlsclanduse.2001', ),
    test=dict(data_root='data/nlsclanduse.2001', ),
)
