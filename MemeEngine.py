from PIL import Image, ImageDraw, ImageFont

import os
from time import time


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
        self.out_path = os.path.join(self.out_dir, f'tmp-{int(time())}.png')

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    def make_meme(self, img_path, text, author, width = 500) -> str:
        img = Image.open(img_path)
        # Resize the image:
        w, h = img.size
        r = width/w
        img = img.resize((width, int(r * h)), Image.NEAREST)

        # Put the text on top:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/FONTS/LilitaOne-Regular.ttf', size = 20)
        draw.text((10, 30), f'{text}\n- {author}', font = font, fill = 'white')

        img.save(self.out_path)
        print(f'[Info] Image Saved to {self.out_path}.')
        return self.out_path
