from PIL import Image, ImageDraw, ImageFont

import os
from time import time
from random import randint


class MemeEngine:
    """Create a Postcard with an Inspiring Text on Top.

    Arguments:
        img_path {str} -- the file location for the input image.
        text {str} -- 
        author {str} -- 
        width {int} -- The pixel width value. Default=500.
    Returns:
        str -- the file path to the output image.
    """
    def __init__(self, output_dir):
        self.out_dir = output_dir
        # self.out_path = os.path.join(self.out_dir, f'tmp-{time()}.png')

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    def make_meme(self, img_path, text, author, width = 500) -> str:
        """
        Load the file.
        Transform image by resizing to a maximum width of 500px
        while maintaining the input aspect ratio.
        Add a caption to an image (string input)
        with a body and author to a random location on the image.
        Save the image/meme in `tmp` directory.

        Returns:
        The path to which the generated image is saved in.
        """
        img = Image.open(img_path)
        # Resize the image:
        w, h = img.size
        width = min(500, width)
        r = width/w
        img = img.resize((width, int(r * h)), Image.NEAREST)

        # Put the text on top:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/FONTS/LilitaOne-Regular.ttf', size = 30)
        draw.text((randint(10, w/4), randint(30, h/4)),
                   f'{text}\n- {author}', font = font, fill = 'white')

        out_path  = os.path.join(self.out_dir, f'tmp-{time()}.png')
        img.save(out_path)
        print(f'[Info] Image Saved to {out_path}.')
        return out_path
