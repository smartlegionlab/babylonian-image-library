import hashlib
import math
import random

from PIL import Image

from babylonian_image_library.library.config import ImageLibraryConfig
from babylonian_image_library.library.coordinates import ImageCoordinates


class BabylonianImageGenerator:

    def __init__(self, config: ImageLibraryConfig):
        self.config = config

    def _get_deterministic_random(self, seed: str) -> random.Random:
        full_seed = f"{self.config.universe}:{seed}"
        seed_hash = hashlib.sha256(full_seed.encode()).hexdigest()
        return random.Random(int(seed_hash, 16))

    def generate_image(self, coordinates: ImageCoordinates) -> Image.Image:
        image = Image.new("RGB", (self.config.width, self.config.height))
        pixels = image.load()

        for y in range(self.config.height):
            for x in range(self.config.width):
                pixel_seed = f"{coordinates.seed}:{x}:{y}"
                pixel_hash = hashlib.sha256(pixel_seed.encode()).hexdigest()

                r = int(pixel_hash[0:2], 16) % 256
                g = int(pixel_hash[2:4], 16) % 256
                b = int(pixel_hash[4:6], 16) % 256

                pixels[x, y] = (r, g, b)

        return image

    def generate_abstract_image(self, coordinates: ImageCoordinates) -> Image.Image:
        random_gen = self._get_deterministic_random(coordinates.seed)
        image = Image.new("RGB", (self.config.width, self.config.height))
        pixels = image.load()

        base_seed = hashlib.sha256(coordinates.seed.encode()).hexdigest()
        base_r = int(base_seed[0:2], 16) % 256
        base_g = int(base_seed[2:4], 16) % 256
        base_b = int(base_seed[4:6], 16) % 256

        for y in range(self.config.height):
            for x in range(self.config.width):
                noise_x = random_gen.randint(-50, 50)
                noise_y = random_gen.randint(-50, 50)

                pattern_x = int(128 * (0.5 + 0.5 * math.sin(x * 0.1 + noise_x * 0.01)))
                pattern_y = int(128 * (0.5 + 0.5 * math.sin(y * 0.1 + noise_y * 0.01)))

                r = (base_r + pattern_x) % 256
                g = (base_g + pattern_y) % 256
                b = (base_b + (pattern_x + pattern_y) // 2) % 256

                pixels[x, y] = (r, g, b)

        return image

    def generate_gradient_image(self, coordinates: ImageCoordinates) -> Image.Image:
        random_gen = self._get_deterministic_random(coordinates.seed)
        image = Image.new("RGB", (self.config.width, self.config.height))
        pixels = image.load()

        color1_seed = hashlib.sha256(f"{coordinates.seed}:color1".encode()).hexdigest()
        color2_seed = hashlib.sha256(f"{coordinates.seed}:color2".encode()).hexdigest()

        r1 = int(color1_seed[0:2], 16) % 256
        g1 = int(color1_seed[2:4], 16) % 256
        b1 = int(color1_seed[4:6], 16) % 256

        r2 = int(color2_seed[0:2], 16) % 256
        g2 = int(color2_seed[2:4], 16) % 256
        b2 = int(color2_seed[4:6], 16) % 256

        gradient_type = random_gen.choice(["horizontal", "vertical", "diagonal", "radial"])

        for y in range(self.config.height):
            for x in range(self.config.width):
                if gradient_type == "horizontal":
                    t = x / self.config.width
                elif gradient_type == "vertical":
                    t = y / self.config.height
                elif gradient_type == "diagonal":
                    t = (x + y) / (self.config.width + self.config.height)
                else:
                    center_x, center_y = self.config.width / 2, self.config.height / 2
                    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                    max_distance = math.sqrt(center_x ** 2 + center_y ** 2)
                    t = distance / max_distance

                noise = random_gen.uniform(-0.1, 0.1)
                t = max(0, min(1, t + noise))

                r = int(r1 + (r2 - r1) * t) % 256
                g = int(g1 + (g2 - g1) * t) % 256
                b = int(b1 + (b2 - b1) * t) % 256

                pixels[x, y] = (r, g, b)

        return image
