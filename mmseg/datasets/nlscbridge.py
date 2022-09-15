# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class NLSCBridgeDataset(CustomDataset):
    """NLSC Bridge dataset.

    Args:
        split (str): Split txt file for NLSC Landuse.
    """

    CLASSES = ('Background', 'Bridge')

    PALETTE = [[0x00, 0x00, 0x00], [0xff, 0xff, 0xff]]

    def __init__(self, **kwargs):
        super(NLSCBridgeDataset, self).__init__(
            img_suffix='.png', seg_map_suffix='.png', **kwargs)
