import random
import os
import requests
from flask import Flask, render_template, abort, request, url_for


from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   #'./_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

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
    # Get the user input
    img_url = request.form['image_url']
    quote = QuoteModel(request.form['body'], request.form['author'])
    # Save the image temporarily for generating a meme out of it.
    r = requests.get(img_url)
    path_tmp = './tmp/posted-image.png'
    with open(path_tmp, 'wb') as f:
	    f.write(r.content)
    
    # Generate a meme based on user input.
    path = meme.make_meme(path_tmp, quote.body, quote.author)
    # path = url_for('static', filename="out/" + path)
    
    # Remove the temporary saved image:
    os.remove(path_tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
