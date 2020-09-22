from flask import Flask, render_template, request
from select_key_words import select_key_words
from get_images import get_images

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


@app.route('/a', methods=['GET', 'POST'])
def render_pic():
    text = request.form['text']
    print(text)
    key_words = select_key_words(text)
    list_of_all_img = []
    for word in key_words:
        list_of_img = get_images(word)
        for name in list_of_img:
            list_of_all_img.append(name)
    print(list_of_all_img)
    return render_template('test.html', list=list_of_all_img)


if __name__ == "__main__":
    app.run(debug=True)
