class TextBlobGenericModel:
    """
    Test Model for Spacy Textblob model
    """
    def __init__(self, model):
        self.model = model

    def return_textblob_doc(self, txtblob): # allows adding features
        self.blob = txtblob

    def __call__(self, text):
        # call model test dummy/double  
        return DocBlobTestDoubleModel(text, self.blob)

class DocBlobTestDoubleModel:
    """
    Test Double for Textblob Docs for relevant features
    """
    def __init__(self, sentence, blob):
        self.overallsentence = sentence
        self.sentimentlist = [BlobDouble(keywordtuple[0],
                                    keywordtuple[1],
                                    keywordtuple[2]) for keywordtuple in blob]
        self.overallpolarity = self.get_polarity() # equivalent to doc._.blob.polarity returns
        self.overallsubjectivity = self.get_subjectivity() # equivalent to doc._.blob.subjectivity returns

    def get_polarity(self):
        if self.sentiment_is_empty(self.sentimentlist):
            return 0.0
        else:
            polarity_list = [bd.keywordpolarity for bd in self.sentimentlist]
            return sum(polarity_list)/len(polarity_list)
    
    def get_subjectivity(self):
        if self.sentiment_is_empty(self.sentimentlist):
            return float(len(self.sentimentlist))
        else:
            subjectivity_list = [bd.keywordsubjectivity for bd in self.sentimentlist]
            return sum(subjectivity_list)/len(subjectivity_list)
    
    @staticmethod
    def sentiment_is_empty(test_list):
        return test_list == []
    
class BlobDouble:
    """
    Test Double for Sentiment output 
    """
    def __init__(self, keywordlist, keywordpolarity, keywordsubjectivity):
        self.keywordlist = keywordlist
        self.keywordpolarity = keywordpolarity
        self.keywordsubjectivity = keywordsubjectivity

    