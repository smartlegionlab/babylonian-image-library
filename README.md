# Babylonian Image Library <sup>v0.1.4</sup>

***

[![PyPI Downloads](https://static.pepy.tech/badge/babylonian-image-library)](https://pepy.tech/projects/babylonian-image-library)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/babylonian-image-library)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/babylonian-image-library)](https://github.com/smartlegionlab/babylonian-image-library/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/babylonian-image-library)](https://github.com/smartlegionlab/babylonian-image-library/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/babylonian-image-library?label=pypi%20downloads)](https://pypi.org/project/babylonian-image-library/)
[![PyPI](https://img.shields.io/pypi/v/babylonian-image-library)](https://pypi.org/project/babylonian-image-library)
[![PyPI - Format](https://img.shields.io/pypi/format/babylonian-image-library)](https://pypi.org/project/babylonian-image-library)

***

Author and developer: ___A.A. Suvorov___

---

# Babylonian Image Library

The **Babylonian Image Library** is a Python library that generates unique images based on a given seed or address. 
The library uses SHA-256 hashing to create deterministic yet visually unique images. 
It also provides functionality to generate random addresses, which can be used to create random images.

## Features

- **Deterministic Image Generation**: Generate images based on a seed or address using SHA-256 hashing.
- **Random Address Generation**: Create random addresses in the format `RoomX:WallY:ShelfZ:VolumeA:BookB:PageC`.
- **Image Saving**: Save generated images to a file in PNG format.
- **Customizable Image Size**: Set custom width and height for the generated images.

## Installation

To use the Babylon Image Library, ensure you have the following dependencies installed:

- Python 3.x
- `Pillow` (PIL fork) for image manipulation.

```bash
pip install babylonian-image-library
```

## Usage

### Basic Example

```python
from babylonian_image_library import BabylonianImageLibrary

# Create an instance of the library
library = BabylonianImageLibrary(width=800, height=600)

# Generate a random address
random_address = library.generate_random_address()
print(f"Random address: {random_address}")

# Save the generated image to a file
library.save_image(random_address, "random_image.png")
print("The image has been saved to 'random_image.png'")
```

### Custom Seed

You can also generate an image using a custom seed:

```python
# Generate an image using a custom seed
from babylonian_image_library import BabylonianImageLibrary

# Create an instance of the library
library = BabylonianImageLibrary()
custom_seed = "MyCustomSeed123"
library.save_image(custom_seed, "custom_image.png")
print("The image has been saved to 'custom_image.png'")
```

### Image Generation Process

The image generation process works as follows:

1. The input seed (or address) is hashed using SHA-256.
2. The hash is used to generate RGB pixel values for the image.
3. If the hash is exhausted, it is rehashed to continue generating pixel values.
4. The resulting image is saved to a file.

### Random Address Format

The random address is generated in the following format:

```
RoomX:WallY:ShelfZ:VolumeA:BookB:PageC
```

Where:
- `X` is a random integer between 1 and 100.
- `Y` is a random integer between 1 and 6.
- `Z` is a random integer between 1 and 10.
- `A` is a random integer between 1 and 10.
- `B` is a random integer between 1 and 100.
- `C` is a random integer between 1 and 1000.

## API Reference

### `BabylonianImageLibrary(width=1920, height=1080)`

- **width**: The width of the generated image (default: 1920).
- **height**: The height of the generated image (default: 1080).

### Methods

- **`generate_image(seed)`**: Generates an image based on the provided seed.
- **`get_image(address)`**: Returns an image generated from the given address.
- **`save_image(address, filename="output.png")`**: Saves the generated image to a file.
- **`generate_random_address()`**: Generates a random address in the specified format.

## Example Output

Running the script will generate a random address and save the corresponding image to a file:

```
Random address: Room42:Wall3:Shelf7:Volume5:Book23:Page456
The image has been saved to 'random_image.png'

```

***

## Information for developers:

- `pip install setuptools twine wheel`
- `pip install build`
- `pip install --upgrade pip`
- `python -m build`
- `twine upload dist/*`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
