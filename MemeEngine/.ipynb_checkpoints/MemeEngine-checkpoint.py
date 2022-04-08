from PIL import Image, ImageDraw
import random

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
            
        draw = ImageDraw.draw(img)
        draw.text((random.randint(img.size), random.randomint(img.size)),
                  text + author)
        
        # save the image
        
        img.save(output_dir)
        
        return output_dir
        
            