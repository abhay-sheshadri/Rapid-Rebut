from flask import request, render_template, redirect, json
from app import app
from utils.infersent import get_infersent
from utils.query import is_rumor
from nltk.tokenize import sent_tokenize

@app.route("/", methods=["POST"])
def isrumor():
    """
    Endpoint for checking if a sentence is a rumor or not
    """
    # Get the sentences
    sentences = request.get_json()["sentences"]
    response = []
    vecs = get_infersent(sentences)
    for vec in vecs:
        response.append(is_rumor(vec))
    # return the answer
    return json.dumps(response)

@app.route("/tokenize", methods=["POST"])
def tokenize_endpoint():
    """
    Endpoint for tokenizing the contents of a page
    """
    text = request.get_json()["text"]
    se = text.split("\n")
    sents = []
    for s in se:
        sents += sent_tokenize(s)
    # Filter out undesirable answers
    def contains(sent):
        exclude = ["|", "@", "^"]
        for c in sent:
            if c in exclude:
                return True
        return False
    sents = [sent for sent in sents if len(sent) > 16 and not contains(sent)]
    # Return the answer
    return json.dumps(sents)
