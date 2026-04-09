# Babylonian Image Library <sup>v1.0.1</sup>

A deterministic infinite image library generator inspired by Borges' 'The Library of Babel'. Generate unique, deterministic images based on coordinate systems without storing image data.

---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/babylonian-image-library)](https://github.com/smartlegionlab/babylonian-image-library/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/babylonian-image-library)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/babylonian-image-library)](https://github.com/smartlegionlab/babylonian-image-library/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/babylonian-image-library?style=social)](https://github.com/smartlegionlab/babylonian-image-library/)
[![PyPI Downloads](https://static.pepy.tech/badge/babylonian-image-library)](https://pepy.tech/projects/babylonian-image-library)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/babylonian-image-library?label=pypi%20downloads)](https://pypi.org/project/babylonian-image-library/)
[![PyPI](https://img.shields.io/pypi/v/babylonian-image-library)](https://pypi.org/project/babylonian-image-library)
[![PyPI - Format](https://img.shields.io/pypi/format/babylonian-image-library)](https://pypi.org/project/babylonian-image-library)

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/babylonian-image-library/blob/master/DISCLAIMER.md)

---

## Project Status: Research & Development

**IMPORTANT DISCLAIMER**: This project is currently in active research and development phase. It is provided as-is for academic and experimental purposes only. No guarantees of stability, security, or fitness for any particular purpose are provided. Users assume all risks associated with usage.

---

## Version Information

### Current Version: 1.0.1 (New Modular Architecture)

**Complete rewrite with breaking changes** - this version introduces a completely new architecture inspired by the Smart Babylon Library:

- **Multi-Universe Support** - Isolated image libraries with different configurations
- **6D Coordinate System** - Floor, room, cabinet, shelf, book, page coordinates
- **Deterministic Generation** - Same coordinates always produce the same image
- **Home Directory Storage** - Organized storage in `~/babylonian_image_library/`
- **Multiple Image Types** - Standard and abstract image generation
- **Configurable Settings** - Custom dimensions, formats, and quality
- **Modular Architecture** - Clean separation with config, coordinates, core, and generator modules

### Legacy Version: 0.1.4 (Deprecated)

**Version `0.1.4` and earlier are no longer supported.** The previous monolithic architecture has been completely replaced by the new modular system.

**Key breaking changes from 0.1.4 to 1.0.1:**
- **New import paths**: `from babylonian_image_library import SmartBabylonImageLibrary`
- **Different coordinate system**: 6D coordinates instead of address strings
- **Modular structure**: Separate config, coordinates, core, and generator modules
- **Multi-universe support**: Isolated libraries with different configurations
- **Home directory storage**: Automatic organization in user's home folder
- **Enhanced API**: Object-oriented interface with better type safety

---

## Related Research Publications

This library implements concepts from our published research:

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural shift from data protection to data non-existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological shift from data transmission to synchronous state discovery  
- **[Deterministic Game Engine](https://doi.org/10.5281/zenodo.17383447)** - Practical implementation validating the theoretical paradigms
- **[Position-Candidate-Hypothesis (PCH) Paradigm](https://doi.org/10.5281/zenodo.17614888)** - A New Research Direction for NP-Complete Problems

## Features

- **Deterministic Image Generation**: Same coordinates always produce the same image
- **Infinite Image Library**: Virtually unlimited images through coordinate system
- **Zero Image Storage**: Images generated on-demand, only metadata stored
- **Multi-Universe Support**: Isolated libraries with different configurations
- **Home Directory Storage**: Automatic organization in user's home directory
- **Configurable**: Custom image dimensions, formats, and quality
- **Abstract Art Generation**: Algorithmic abstract image creation
- **Modular Design**: Clean, maintainable architecture

## Installation

```bash
pip install babylonian-image-library
```

## Quick Start

```python
from babylonian_image_library import SmartBabylonImageLibrary

# Create library instance
library = SmartBabylonImageLibrary()

# Generate a random image
image_path = library.generate_random_image()
print(f"Image saved: {image_path}")

# Get specific image by coordinates
image = library.get_image(floor=1, room=3, cabinet=2, shelf=5, book=42, page=1)
image.save("specific_image.png")
```

## Architecture

The library follows a modular architecture:

```
babylonian_image_library/
├── library/
│   ├── config.py      # ImageLibraryConfig
│   ├── coordinates.py # ImageCoordinates  
│   ├── core.py        # BabylonianImageLibrary, SmartBabylonImageLibrary
│   └── generator.py   # BabylonianImageGenerator
```

## Coordinate System

Each image is located using 6-dimensional coordinates:
- `floor`: Library floor (0-100)
- `room`: Room number (0-50)  
- `cabinet`: Cabinet number (0-20)
- `shelf`: Shelf number (0-10)
- `book`: Book number (0-1000)
- `page`: Page number (0-500)

## Configuration

```python
from babylonian_image_library import SmartBabylonImageLibrary, ImageLibraryConfig

# Custom configuration
config = ImageLibraryConfig(
    universe="abstract_art",    # Universe name
    width=800,                  # Image width
    height=600,                 # Image height
    image_format="JPEG",        # PNG, JPEG, etc.
    quality=90                  # JPEG quality (1-100)
)

library = SmartBabylonImageLibrary(config)
```

## Migration Guide from 0.1.4 to 1.0.1

### Before (0.1.4):
```python
from babylonian_image_library import BabylonianImageLibrary

library = BabylonianImageLibrary()
address = library.generate_random_address()  # "Room42:Wall3:Shelf7:Volume5:Book23:Page456"
library.save_image(address, "image.png")
```

### After (1.0.1):
```python
from babylonian_image_library import SmartBabylonImageLibrary

library = SmartBabylonImageLibrary()
image_path = library.generate_random_image()  # Automatically generates coordinates
# Or use specific coordinates:
image = library.get_image(floor=1, room=3, cabinet=2, shelf=5, book=42, page=1)
```

## Multi-Universe Support

```python
from babylonian_image_library import SmartBabylonImageLibrary, ImageLibraryConfig

# Different universes - different images
fantasy_config = ImageLibraryConfig(universe="middle_earth")
scifi_config = ImageLibraryConfig(universe="andromeda_galaxy")

fantasy_library = SmartBabylonImageLibrary(fantasy_config)
scifi_library = SmartBabylonImageLibrary(scifi_config)

# Same coordinates, different images
fantasy_image = fantasy_library.get_image(1, 1, 1, 1, 1, 1)
scifi_image = scifi_library.get_image(1, 1, 1, 1, 1, 1)
```

## API Reference

### SmartBabylonImageLibrary

Main library interface:

- `get_image(floor, room, cabinet, shelf, book, page)` - Get image by coordinates
- `get_abstract_image(floor, room, cabinet, shelf, book, page)` - Get abstract image
- `save_image(floor, room, cabinet, shelf, book, page, filename)` - Save image to file
- `save_abstract_image(floor, room, cabinet, shelf, book, page, filename)` - Save abstract image
- `generate_random_image()` - Generate and save random image
- `get_library_info()` - Get library information

### ImageLibraryConfig

Configuration class:

- `universe` - Universe name (default: "default")
- `width` - Image width (default: 1920)
- `height` - Image height (default: 1080) 
- `image_format` - Image format (default: "PNG")
- `quality` - JPEG quality (default: 95)

### ImageCoordinates

Coordinate class:

- `floor, room, cabinet, shelf, book, page` - Coordinate components
- `seed` - Combined seed string for generation
- `to_dict()` - Convert to dictionary
- `to_json()` - Convert to JSON string

## Examples

### Basic Usage

```python
from babylonian_image_library import SmartBabylonImageLibrary

library = SmartBabylonImageLibrary()

# Generate multiple random images
for i in range(5):
    path = library.generate_random_image()
    print(f"Generated: {path}")

# Get library information
info = library.get_library_info()
print(f"Library location: {info['library_path']}")
print(f"Total images: {info['total_images']}")
```

### Working with Coordinates

```python
from babylonian_image_library import ImageCoordinates

# Create specific coordinates
coords = ImageCoordinates(floor=5, room=10, cabinet=3, shelf=2, book=150, page=42)
print(f"Coordinates: {coords}")
print(f"Seed: {coords.seed}")

# Use coordinates with library
image = library.get_image(coords.floor, coords.room, coords.cabinet, 
                         coords.shelf, coords.book, coords.page)
```

### Advanced Usage

```python
from babylonian_image_library import SmartBabylonImageLibrary, ImageLibraryConfig

# Create specialized universe for digital art
art_config = ImageLibraryConfig(
    universe="digital_art",
    width=1024,
    height=768,
    image_format="PNG"
)

art_library = SmartBabylonImageLibrary(art_config)

# Generate a series of abstract artworks
for i in range(10):
    art_library.save_abstract_image(1, 1, 1, 1, i, 0, f"artwork_{i}.png")
```

## Storage Location

Images are automatically stored in:
- Linux/Mac: `~/babylonian_image_library/{universe}/`
- Windows: `C:\Users\{username}\babylonian_image_library\{universe}\`

## Deterministic Behavior

Image generation is deterministic based on coordinates and universe:

```python
# Same coordinates = same image
library1 = SmartBabylonImageLibrary(ImageLibraryConfig(universe="test"))
library2 = SmartBabylonImageLibrary(ImageLibraryConfig(universe="test"))

image1 = library1.get_image(1, 1, 1, 1, 1, 1)
image2 = library2.get_image(1, 1, 1, 1, 1, 1)

# Images will be identical
```

**RESEARCH STATUS**: This implementation is part of ongoing research into deterministic systems and pointer-based architectures. It should not be used in production environments or for any critical applications.

## License

[BSD 3-Clause License](https://github.com/smartlegionlab/babylonian-image-library/blob/master/LICENSE)
Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab/)
