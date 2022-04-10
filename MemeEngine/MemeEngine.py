from PIL import Image, ImageDraw, ImageFont
import random

import os

class MemeEngine:
    """Generate a meme -- output to filepath."""
    
    def __init__(self, output_dir):
        
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):

        # load an image
        img = Image.open(img_path)
        
        # resize the image if necessary
        width, height = img.size
        
        if width > 500:
            
            ratio = (width - 500) / width
            img = img.resize(500, heigh * ratio)
            
        # add quote to random location on image
        
        random_x_coordinate = random.randint(0, img.size[0])
        random_y_coordinate = random.randint(0, img.size[1])

            
        draw = ImageDraw.Draw(img)
        
        # setting the font 
        try:
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', 30)
        except Exception:
            raise OSError('Invalid font path')
            
        draw.multiline_text((random_x_coordinate, random_y_coordinate), f'{text}\n{author}', font=font, fill='blue')
        #draw.text((random_x_coordinate, random_y_coordinate), text, font=font, fill='blue')
        #draw.text((random_x_coordinate, random_y_coordinate), author, font=font, fill='blue')
        
        # save the image
        
        img_out_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 100000000)}.png')
        img.save(img_out_path)
    
        return img_out_path
        
            