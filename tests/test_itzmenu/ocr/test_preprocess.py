import io

import numpy as np
from PIL import Image

import itzmenu.ocr.preprocess as preprocess


class TestPreprocess:

    def test_apply_threshold(self, week_menu: bytes):
        @preprocess.apply_threshold
        def dummy_func(img: bytes) -> bytes:
            return img

        # Apply the apply_threshold decorator through the dummy function
        image = dummy_func(week_menu)

        # Load the image and convert it to a numpy array
        pimage = Image.open(io.BytesIO(image)).convert('L')
        image_np = np.array(pimage)

        # Check if it is a grayscale image
        assert len(image_np.shape) == 2

        tolerance = 20
        # Check if the image is thresholded correctly
        unique_colors = np.unique(image_np)
        black_range = range(0, tolerance + 1)
        white_range = range(255 - tolerance, 256)
        assert all(color in black_range or color in white_range for color in unique_colors)

    def test_crop_main_image_content(self, week_menu: bytes):
        @preprocess.crop_main_image_content
        def dummy_func(img: bytes) -> bytes:
            return img

        pimage_org = Image.open(io.BytesIO(week_menu))
        with_org, height_org = pimage_org.size

        # Apply the crop_main_image_content decorator through the dummy function
        image = dummy_func(week_menu)

        pimage_cropped = Image.open(io.BytesIO(image))
        with_cropped, height_cropped = pimage_cropped.size

        # Check if the image is cropped correctly
        assert with_org > with_cropped
        assert height_org > height_cropped
