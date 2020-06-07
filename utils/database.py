import mongoengine
import utils.infersent as infer
import numpy as np
from params import *

alias_core = "core"
db = "rumor_db"
db_uri = "mongodb+srv://rumor_detector:<password>@rumordetection-jrn9s.mongodb.net/<dbname>?retryWrites=true&w=majority".replace("<password>", PASS).replace("<dbname>", db)
mongoengine.connect(alias=alias_core, db=db, host=db_uri)

class Rumor(mongoengine.Document):

    rumor_text = mongoengine.StringField(required=True)
    truth_text = mongoengine.StringField(required=True)
    source_link = mongoengine.StringField(required=True)

    rumor_vector = mongoengine.ListField(required=True)

    meta = {
        "db_alias": "core",
        "collection": "rumors"
    }

def find_rumor(rumor):
    """
    Returns the rumor object with the corresponding rumor
    """
    r = Rumor.objects(rumor_text=rumor).first()
    return r


def add_rumor(rumor, truth, link, vec=None):
    """
    Adds a rumor to the mongodb
    """
    # Check if rumor exists
    if find_rumor(rumor):
        return
    # Create rumor
    r = Rumor()
    r.rumor_text = rumor
    r.truth_text = truth
    r.source_link = link
    if vec is None:
        vec = infer.get_infersent(rumor)[0].tolist()
    r.rumor_vector = vec
    r.save()


def add_rumors(rumors, truths, links):
    """
    Takes in three arrays.
    Adds them to database if they are not already in the database
    """
    vecs = infer.get_infersent(rumors)
    # Create rumors
    for i in range(len(rumors)):
        add_rumor(rumors[i], truths[i], links[i], vecs[i].tolist())


def delete_rumor(rumor):
    """
    Deletes a rumor document from our database
    """
    r = find_rumor(rumor)
    r.delete()

def delete_rumors(rumor_list):
    """
    Delete multiple rumors
    """
    for rumor in rumor_list:
        delete_rumor(rumor)

def get_lists():
    """
    Get all the data in the database
    """
    rumors = []; truths = []; links = []; vecs = []
    for rumor in Rumor.objects:
        rumors.append(rumor.rumor_text)
        truths.append(rumor.truth_text)
        links.append(rumor.source_link)
        vecs.append(rumor.rumor_vector)
    return rumors, truths, links, np.array(vecs)

def text_search(substring, max=5):
    """
    Returns the result of a text search in the database.
    Gives at most max rumors in response.
    """
    c = Rumor.objects.search_text(substring)
    rs = []
    for i in range(min(max, len(c))):
        rs.append(c[i])
    return rs

def insert_from_file(file_path):
    """
    Adds all the rumors from a file to the MongoDB database
    """
    rumors = []; truths = []; links = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            parts = line.rstrip().split("|")
            rumors.append(parts[0])
            truths.append(parts[1])
            links.append(parts[2])
    add_rumors(rumors, truths, links)
        