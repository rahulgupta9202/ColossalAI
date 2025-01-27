#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from pathlib import Path

train_data = dict(
    dataset=dict(
        type='CIFAR10Dataset',
        root=Path(os.environ['DATA']),
        download=True,
        transform_pipeline=[
            dict(type='RandomResizedCrop', size=224),
            dict(type='RandomHorizontalFlip'),
            dict(type='ToTensor'),
            dict(type='Normalize', mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ]
    ),
    dataloader=dict(
        batch_size=64,
        pin_memory=True,
        num_workers=4,
        sampler=dict(
            type='DataParallelSampler',
            shuffle=True,
        )
    )
)
