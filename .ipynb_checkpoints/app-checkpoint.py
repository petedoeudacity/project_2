import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine

from QuoteEngine import Ingestor, DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # parse quote_files
    
    quotes = []
    
    for file in quote_files:
        quotes.append(Ingestor.parse(file)[0])
        
    quote = random.choice(quotes)
    
    images_path = "./_data/photos/dog/"

    # finding images in images_path
    
    imgs = []
    
    for file in os.listdir(images_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    
    # https://knowledge.udacity.com/questions/504424
    # https://knowledge.udacity.com/questions/614215
    # https://knowledge.udacity.com/questions/637910

    t_img = "./temp_img.jpg"
    
    img_url = request.form['image_url']
    img_content = requests.get(img_url,stream=True).content
    
    with open(t_img,'wb') as f:
        f.write(img_content)
        
    quote = request.form['quote']
    author = request.form['author']
    
    path = meme.make_meme(t_img, quote, author)

    os.remove(t_img)
    
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()