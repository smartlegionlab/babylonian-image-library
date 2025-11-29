import random
from pathlib import Path
from typing import Dict, Any

from PIL import Image

from babylonian_image_library.library.config import ImageLibraryConfig
from babylonian_image_library.library.coordinates import ImageCoordinates
from babylonian_image_library.library.generator import BabylonianImageGenerator


class BabylonianImageLibrary:

    def __init__(self, config: ImageLibraryConfig = None):
        self.config = config or ImageLibraryConfig()
        self.generator = BabylonianImageGenerator(self.config)
        self._library_path = self._get_library_path()

    def _get_library_path(self) -> Path:
        home = Path.home()
        library_path = home / "babylonian_image_library" / self.config.universe
        library_path.mkdir(parents=True, exist_ok=True)
        return library_path

    def get_image(self, coordinates: ImageCoordinates) -> Image.Image:
        return self.generator.generate_image(coordinates)

    def get_abstract_image(self, coordinates: ImageCoordinates) -> Image.Image:
        return self.generator.generate_abstract_image(coordinates)

    def get_gradient_image(self, coordinates: ImageCoordinates) -> Image.Image:
        return self.generator.generate_gradient_image(coordinates)

    def save_image(self, coordinates: ImageCoordinates, filename: str = None) -> str:
        if filename is None:
            filename = (f"image_{coordinates.floor}_{coordinates.room}_{coordinates.cabinet}_{coordinates.shelf}"
                        f"_{coordinates.book}_{coordinates.page}.{self.config.image_format.lower()}")

        image_path = self._library_path / filename
        image = self.get_image(coordinates)
        image.save(image_path, self.config.image_format, quality=self.config.quality)
        return str(image_path)

    def save_abstract_image(self, coordinates: ImageCoordinates, filename: str = None) -> str:
        if filename is None:
            filename = (f"abstract_{coordinates.floor}_{coordinates.room}_{coordinates.cabinet}_{coordinates.shelf}"
                        f"_{coordinates.book}_{coordinates.page}.{self.config.image_format.lower()}")

        image_path = self._library_path / filename
        image = self.get_abstract_image(coordinates)
        image.save(image_path, self.config.image_format, quality=self.config.quality)
        return str(image_path)

    def save_gradient_image(self, coordinates: ImageCoordinates, filename: str = None) -> str:
        if filename is None:
            filename = (f"gradient_{coordinates.floor}_{coordinates.room}_{coordinates.cabinet}_{coordinates.shelf}"
                        f"_{coordinates.book}_{coordinates.page}.{self.config.image_format.lower()}")

        image_path = self._library_path / filename
        image = self.get_gradient_image(coordinates)
        image.save(image_path, self.config.image_format, quality=self.config.quality)
        return str(image_path)

    def get_image_path(self, coordinates: ImageCoordinates) -> str:
        filename = (f"image_{coordinates.floor}_{coordinates.room}_{coordinates.cabinet}_{coordinates.shelf}"
                    f"_{coordinates.book}_{coordinates.page}.{self.config.image_format.lower()}")
        image_path = self._library_path / filename

        if not image_path.exists():
            self.save_image(coordinates, filename)

        return str(image_path)

    def generate_random_coordinates(self) -> ImageCoordinates:
        return ImageCoordinates(
            floor=random.randint(0, 100),
            room=random.randint(0, 50),
            cabinet=random.randint(0, 20),
            shelf=random.randint(0, 10),
            book=random.randint(0, 1000),
            page=random.randint(0, 500)
        )

    def get_library_info(self) -> Dict[str, Any]:
        image_files = list(self._library_path.glob(f"*.{self.config.image_format.lower()}"))

        return {
            'universe': self.config.universe,
            'library_path': str(self._library_path),
            'total_images': len(image_files),
            'image_format': self.config.image_format,
            'dimensions': f"{self.config.width}x{self.config.height}",
            'coordinates_system': "6-dimensional (floor, room, cabinet, shelf, book, page)"
        }

    def cleanup_library(self):
        for file in self._library_path.glob("*"):
            if file.is_file():
                file.unlink()


class SmartBabylonImageLibrary:

    def __init__(self, config: ImageLibraryConfig = None):
        self.config = config or ImageLibraryConfig()
        self.library = BabylonianImageLibrary(self.config)

    def get_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int) -> Image.Image:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.get_image(coordinates)

    def get_abstract_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int) -> Image.Image:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.get_abstract_image(coordinates)

    def get_gradient_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int) -> Image.Image:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.get_gradient_image(coordinates)

    def save_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int,
                   filename: str = None) -> str:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.save_image(coordinates, filename)

    def save_abstract_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int,
                            filename: str = None) -> str:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.save_abstract_image(coordinates, filename)

    def save_gradient_image(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int,
                            filename: str = None) -> str:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.save_gradient_image(coordinates, filename)

    def get_image_path(self, floor: int, room: int, cabinet: int, shelf: int, book: int, page: int) -> str:
        coordinates = ImageCoordinates(floor, room, cabinet, shelf, book, page)
        return self.library.get_image_path(coordinates)

    def generate_random_image(self) -> str:
        coordinates = self.library.generate_random_coordinates()
        return self.library.save_image(coordinates)

    def get_library_info(self) -> Dict[str, Any]:
        return self.library.get_library_info()
