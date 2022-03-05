# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class NLSCLanduseDataset(CustomDataset):
    """NLSC Landuse dataset.

    Args:
        split (str): Split txt file for NLSC Landuse.
    """

    CLASSES = ('background', 'build', 'builtup', 'lake', 'orchard', 'sandbar',
               'swamp', 'veg', 'watrcrs')

    PALETTE = [[0x40, 0x40, 0x40], [0xee, 0xee, 0xee], [0xed, 0x64, 0x98],
               [0x38, 0x87, 0xbe], [0xf1, 0xf0, 0x75], [0xfb, 0xb0, 0x3b],
               [0x3b, 0xb2, 0xd0], [0x56, 0xb8, 0x81], [0x28, 0x35, 0x3d]]

    def __init__(self, **kwargs):
        super(NLSCLanduseDataset, self).__init__(
            img_suffix='.webp', seg_map_suffix='.png', **kwargs)
