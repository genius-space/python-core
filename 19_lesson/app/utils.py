import os
import re

from PIL import Image, ImageOps
from app.schemas import ImageProcessingOptions


def process_image(file_location: str, options: ImageProcessingOptions):
    with Image.open(file_location) as img:
        if options.resize:
            match = re.match(r'(\d+)x(\d+)', options.resize)
            if match:
                width, height = map(int, match.groups())
                img = img.resize((width, height))

        if options.grayscale:
            img = ImageOps.grayscale(img)

        if options.flip:
            if options.flip == 'horizontal':
                img = ImageOps.mirror(img)
            elif options.flip == 'vertical':
                img = ImageOps.flip(img)

        if options.convert_to:
            file_location = f"{os.path.splitext(file_location)[0]}.{options.convert_to}"
            img.save(file_location, options.convert_to.upper())
        else:
            img.save(file_location)

    return file_location
