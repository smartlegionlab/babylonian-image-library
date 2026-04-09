# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2026, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from babylonian_image_library.library.config import ImageLibraryConfig
from babylonian_image_library.library.coordinates import ImageCoordinates
from babylonian_image_library.library.core import SmartBabylonImageLibrary


def main():
    print("=== Babylonian Image Library Demo ===\n")

    default_library = SmartBabylonImageLibrary()

    for i in range(3):
        image_path = default_library.generate_random_image()
        print(f"Generated image {i + 1}: {image_path}")

    custom_config = ImageLibraryConfig(
        universe="abstract_art",
        width=800,
        height=600,
        image_format="JPEG",
        quality=90
    )

    art_library = SmartBabylonImageLibrary(custom_config)

    coordinates = ImageCoordinates(1, 1, 1, 1, 1, 1)
    art_path = art_library.save_abstract_image(
        coordinates.floor, coordinates.room, coordinates.cabinet,
        coordinates.shelf, coordinates.book, coordinates.page,
        "masterpiece.jpg"
    )
    print(f"Abstract art saved: {art_path}")

    gradient_coordinates = ImageCoordinates(2, 3, 4, 5, 6, 7)
    gradient_path = art_library.save_abstract_image(
        gradient_coordinates.floor, gradient_coordinates.room, gradient_coordinates.cabinet,
        gradient_coordinates.shelf, gradient_coordinates.book, gradient_coordinates.page,
        "gradient_art.jpg"
    )
    print(f"Gradient art saved: {gradient_path}")

    print(f"\nDefault library info:")
    info = default_library.get_library_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

    print(f"\nArt library info:")
    art_info = art_library.get_library_info()
    for key, value in art_info.items():
        print(f"  {key}: {value}")

    print(f"\n=== Determinism Test ===")
    lib1 = SmartBabylonImageLibrary(ImageLibraryConfig(universe="test"))
    lib2 = SmartBabylonImageLibrary(ImageLibraryConfig(universe="test"))

    test_coordinates = ImageCoordinates(1, 2, 3, 4, 5, 6)
    path1 = lib1.save_image(
        test_coordinates.floor, test_coordinates.room, test_coordinates.cabinet,
        test_coordinates.shelf, test_coordinates.book, test_coordinates.page,
        "test1.png"
    )
    path2 = lib2.save_image(
        test_coordinates.floor, test_coordinates.room, test_coordinates.cabinet,
        test_coordinates.shelf, test_coordinates.book, test_coordinates.page,
        "test2.png"
    )

    print(f"Same universe, same coordinates:")
    print(f"Image 1: {path1}")
    print(f"Image 2: {path2}")
    print(f"Files should be identical: True")

    print(f"\n=== Multi-Universe Test ===")
    universe1_lib = SmartBabylonImageLibrary(ImageLibraryConfig(universe="universe_alpha"))
    universe2_lib = SmartBabylonImageLibrary(ImageLibraryConfig(universe="universe_beta"))

    same_coordinates = ImageCoordinates(5, 5, 5, 5, 5, 5)
    path_alpha = universe1_lib.save_image(
        same_coordinates.floor, same_coordinates.room, same_coordinates.cabinet,
        same_coordinates.shelf, same_coordinates.book, same_coordinates.page,
        "universe_alpha.png"
    )
    path_beta = universe2_lib.save_image(
        same_coordinates.floor, same_coordinates.room, same_coordinates.cabinet,
        same_coordinates.shelf, same_coordinates.book, same_coordinates.page,
        "universe_beta.png"
    )

    print(f"Different universes, same coordinates:")
    print(f"Universe Alpha: {path_alpha}")
    print(f"Universe Beta: {path_beta}")
    print(f"Files should be different: True")

    print(f"\n=== Coordinate Series Test ===")
    series_lib = SmartBabylonImageLibrary(ImageLibraryConfig(universe="coordinate_series"))

    for book_num in range(1, 4):
        for page_num in range(1, 3):
            coordinates = ImageCoordinates(1, 1, 1, 1, book_num, page_num)
            filename = f"book_{book_num}_page_{page_num}.png"
            path = series_lib.save_image(
                coordinates.floor, coordinates.room, coordinates.cabinet,
                coordinates.shelf, coordinates.book, coordinates.page,
                filename
            )
            print(f"Generated: {filename}: {path}")


if __name__ == "__main__":
    main()
