# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class NLSCLanduseDataset(CustomDataset):
    """NLSC Landuse dataset.

    Args:
        split (str): Split txt file for NLSC Landuse.
    """

    CLASSES = ('Background', 'Veg', 'GreenField', 'Woods', 'Ochard',
               'UplandField', 'PaddyField', 'Swamp', 'Sandbar', 'WaterBody',
               'Builtup')

    PALETTE = [[0xff, 0xff, 0xff], [0x56, 0xb8, 0x81], [0x34, 0x7c, 0x17],
               [0x25, 0x41, 0x17], [0xf1, 0xf0, 0x75], [0xf5, 0xde, 0xb3],
               [0xfb, 0xe7, 0xa1], [0x8a, 0x8a, 0xcb], [0xfb, 0xb0, 0x3b],
               [0x3b, 0xb2, 0xd0], [0xed, 0x64, 0x98]]

    def __init__(self, **kwargs):
        super(NLSCLanduseDataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', **kwargs)
