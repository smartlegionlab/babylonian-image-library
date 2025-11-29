from dataclasses import dataclass


@dataclass
class ImageLibraryConfig:
    universe: str = "default"
    width: int = 1920
    height: int = 1080
    image_format: str = "PNG"
    quality: int = 95

    def __post_init__(self):
        if not isinstance(self.universe, str):
            raise ValueError("Universe must be a string")
        if self.width < 1 or self.height < 1:
            raise ValueError("Image dimensions must be positive")
        if self.quality < 1 or self.quality > 100:
            raise ValueError("Quality must be between 1 and 100")
