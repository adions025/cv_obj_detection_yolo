"""
Settings class

Some settings parameters.
"""

import os


class Settings:
    PROJECT_NAME: str = "Object detection YoloV3"

    ROOT_DIR = os.path.abspath("../../")
    DEFAULT_DATA = os.path.join(ROOT_DIR, "data")


settings = Settings()
