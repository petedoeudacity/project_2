import os
import random
import argparse

# @TODO Import your Ingestor and MemeEngine classes

from MemeEngine import MemeEngine

from QuoteEngine import Ingestor, DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor, QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            
            print(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--path')
    parser.add_argument('--body')
    parser.add_argument('--author')

    args = parser.parse_args()

    
    print(generate_meme(args.path, args.body, args.author))