_base_ = 'lraspp_m-v3-d8_256x256_320k_nlscbridge.py'

data = dict(
    train=dict(data_root='data/nlscbridge.synhm_cut', ),
    val=dict(data_root='data/nlscbridge.2001', ),
    test=dict(data_root='data/nlscbridge.2001', ),
)
