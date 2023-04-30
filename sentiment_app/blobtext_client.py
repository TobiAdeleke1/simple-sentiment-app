import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob

class BlobTextClient:
	def __init__(self, model):
		self.model = model
	
	def set_textblobdoc(self, sentence):
		self.doc = self.model(sentence)._.blob
	
	def get_sentiment(self):
		return self.doc.sentiment
	
	def get_polarity(self):
		return self.doc.polarity
	
	def get_subjectivity(self):
		return self.doc.subjectivity
	
	def get_ngram(self):
	    return self.doc.ngram
	

class TextBlobSpacy:
    def __init__(self):
        self.model = spacy.load("en_core_web_sm")
        self.model.add_pipe('spacytextblob')
    
    def get_model(self):
        return self.model

        
