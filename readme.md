# install deps for following sci-py tutorials from Sentdex

Youtube: https://www.youtube.com/watch?v=rAdAVcS4aL0&index=4&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

```bash
sudo apt-get install python-tk

pip install --upgrade pip
pip install matplotlib
pip install numpy
sudo pip install scipy
sudo pip install scikit-learn
sudo pip install pandas
```

## Now, we will use iPython and jupyter

```bash
python3 -m pip install --upgrade pip
python3 -m pip install jupyter

python3 -m pip install matplotlib numpy scipy pandas seaborn sklearn

# natural language toolkit
python3 -m pip install nltk
```

Now, start the jupyter notebook server

```bash
jupyter notebook
```

## Natural language work

Note that nltk must download the corpus data. Call ```nltk.download()``` and grab all of the packages.

Make sure it is working like so:
```python
from nltk.corpus import stopwords

stopwords.words('english')
```

Stemming:
```python
from nlkt.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")
```
