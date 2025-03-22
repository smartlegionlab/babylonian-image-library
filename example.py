# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from babylonian_image_library import BabylonianImageLibrary


def main():
    library = BabylonianImageLibrary()

    random_address = library.generate_random_address()
    print(f"Random address: {random_address}")

    library.save_image(random_address, "random_image.png")
    print("The image has been saved to file. 'random_image.png'")


if __name__ == "__main__":
    main()
