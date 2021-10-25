"""
Settings class

Some settings parameters.
"""

import os
import sys


class Settings:
    PROJECT_NAME: str = "Object detection YoloV3"

    ROOT_DIR = os.path.abspath("../../")
    DEFAULT_DATA = os.path.join(ROOT_DIR, "data")

    CONFIG_FILE = os.path.join(ROOT_DIR, "config.json")

    DATASET_TRAIN_VAL = os.path.join(DEFAULT_DATA, "dataset2")
    IMG_TRAIN_DIR = os.path.join(DATASET_TRAIN_VAL, "images_train")
    ANNOTS_TRAIN_DIR = os.path.join(DATASET_TRAIN_VAL, "annots_train")
    IMG_VAL_DIR = os.path.join(DATASET_TRAIN_VAL, "images_val")
    ANNOTS_VAL_DIR = os.path.join(DATASET_TRAIN_VAL, "annots_val")

    MODEL_VOC = os.path.join(ROOT_DIR, "voc.h5")


settings = Settings()
