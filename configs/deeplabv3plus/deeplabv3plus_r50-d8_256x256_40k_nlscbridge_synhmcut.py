_base_ = 'deeplabv3plus_r50-d8_256x256_40k_nlscbridge.py'

data = dict(
    train=dict(data_root='data/nlscbridge.synhm_cut', ),
    val=dict(data_root='data/nlscbridge.2001', ),
    test=dict(data_root='data/nlscbridge.2001', ),
)
