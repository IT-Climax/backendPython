from dev_config import DevConfig
from production import ProductionConfig


class Config:
    def __init__(self):
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()
