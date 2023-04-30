import spacy 
from collections import namedtuple

class TextblobTestModel:
    """
    Test Model for Spacy Textblob model
    """
    def __init__(self, model) -> None:
        self.model = model
    
    def returns_textblob(self,sentence):
        self.textblob = self.model(sentence)._.blob
    
    def __call__(self):
        return DocTextBlob(self.textblob)
    

class DocTextBlob:
    """
    Test model to get all the features of Textblob
    """
    # def __init__(self, sentence, textblob):
    def __init__(self,  textblob):
        self.textblob = textblob
        self.polarity = textblob.polarity
        self.subjectivity = textblob.subjectivity
        self.sentiment = textblob.sentiment_assessments.assessments
        self.ngram = textblob.ngrams()

    def get_polarity(self):
        return self.polarity 

    def get_subjectivity(self):
        return self.subjectivity
    
    def get_sentiment(self):
        return self.sentiment
    
    def get_ngram(self):
        return self.ngram
    
    # def get_sentence(self):
    #     return self.sentence
    
class TextBlobSpacy:
    def __init__(self):
        self.model = spacy.load("en_core_web_sm")
        self.model.add_pipe('spacytextblob')
    
    def get_model(self):
        return self.model
    
    # def get_blobmodel(self):
     #     doc = self.model._.blob
    #     return doc

