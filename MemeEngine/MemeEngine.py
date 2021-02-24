"""Manipulate (load, resize) and draw text onto images."""
from PIL import Image, ImageDraw, ImageFont

import os
from time import time
from random import randrange


class MemeEngine:
    """
    Create a Postcard with an Inspiring Text on Top.

    Arguments:
        img_path {str} -- the file location for the input image.
        text {str} -- 
        author {str} -- 
        width {int} -- The pixel width value. Default=500.
    Returns:
        str -- the file path to the output image.
    """
    
    def __init__(self, output_dir):
        """Initialize with which directory to save the image in."""
        self.out_dir = output_dir

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    def make_meme(self, img_path, text, author, width = 500) -> str:
        """
        Generate the meme.
        
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
        height = int(r * h)
        img = img.resize((width, height), Image.NEAREST)

        # Put the text on top:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/FONTS/LilitaOne-Regular.ttf',
                                  size = 20)
        # Put the quote on a 'random' place on the image:
        row_text = randrange(30, height - 50)
        draw.text((50, row_text), text,
                  font = font, fill = 'white')
        draw.text((50, row_text + 20), f'- {author}',
                  font = font, fill = 'white')

        out_path  = os.path.join(self.out_dir, f'tmp-{time()}.png')
        img.save(out_path)
        print(f'[Info] Image Saved to {out_path}.')
        return out_path
