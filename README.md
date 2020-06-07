# Rapid Rebut
A google chrome extension that marks up rumors and conspiracy theories on websites.

## How to install
First, clone this repository.
  Rapid Rebut was made with Python 3.8.  It is recommended that you use Anaconda, a free open-source distribution of Python. 
Assuming that you have Anaconda installed, create a virtual environment:

```
conda create --name rumor
conda activate rumor
```

In the directory of the repository, install all the packages listed in the requirements.txt file into your virtual environment

```
conda install --force-reinstall -y -q --name rumor -c conda-forge --file requirements.txt
```

Also, install the punkt tokenizer
```
python
>>> import nltk
>>> nltk.download("punkt")
```

Clone this repository into the Rapid-Rebut folder (https://github.com/facebookresearch/InferSent).  Rename this folder to INF.  Create two folders inside it:
* Create a folder names `encoder` inside INF.  Download this file and place it inside the folder https://dl.fbaipublicfiles.com/infersent/infersent2.pkl.
* Create a folder names `fastText` inside INF.  Download this zip. https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip.  Place the file within it into the folder.

Finally, you need to install the extension:
1. On Google Chrome, hit the side menu and hover over More Tools. From there, click extensions
2. At the top right, turn developer mode on
3. Click Load unpacked at the top left
4. Choose the extension folder within Rapid-Rebut
5. Enable the extension

## Running the project
In order for the extension to work, you need to start up the flask server on your machine.  Run the `run.py` python file.  This will start up the Flask server.
To test to see if it works, go to this page (https://archive.fo/EjiAF).  The article's title should be highlighted in red within a few seconds of loading the page.

If you want to edit the shared database, you can run `admin.py`  This will allow you to insert or remove rumor documents from the MongoDB database.


