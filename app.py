from flask import Flask, request, jsonify, render_template
from fancify_text import (bold, reversed_, heavyCircled, smallCaps, curly, monospaced, italic, doubleStruck, 
                          superscript, upsideDown, 
                           script, fraktur, 
                           wide, boldItalic, boldSerif, 
                          italicSerif, boldItalicSerif, doubleStruck, 
                          squared, circled, parenthesized, boxed, blue, 
                          heavyCircled, currency, cool, magic, wiry)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/fancify', methods=['GET'])
def fancify():
    text = request.args.get('text', '')
    fancified_texts = {}
    if text:
        fancified_texts = {
            "Bold": bold(text),
            "Reversed": reversed_(text),
            "Heavy Circled": heavyCircled(text),
            "Small Caps": smallCaps(text),
            "Curly": curly(text),
            "Monospaced": monospaced(text),
            "Italic": italic(text),
            "Bold Italic": boldItalic(text),
            "Bold Serif": boldSerif(text),
            "Italic Serif": italicSerif(text),
            "Bold Italic Serif": boldItalicSerif(text),
            "Double Struck": doubleStruck(text),
            "Wide": wide(text),
            "Fraktur": fraktur(text),
            "Bold Fraktur": fraktur(text),  # assuming a function for bold Fraktur exists
            "Script": script(text),
            "Small Caps": smallCaps(text),
            "Squared": squared(text),
            "Circled": circled(text),
            "Parenthesized": parenthesized(text),
            "Boxed": boxed(text),
            "Blue": blue(text),
            "Heavy Circled": heavyCircled(text),
            "Currency": currency(text),
            "Cool": cool(text),
            "Magic": magic(text),
            "Wiry": wiry(text),
            "Upside Down": upsideDown(text),
            "Superscript": superscript(text),

        }
    return jsonify(fancified_texts)

if __name__ == '__main__':
    app.run(debug=True)
