import spacy

# from spacytextblob.spacytextblob import SpacyTextBlob

class BlobTextClient:
	def __init__(self, model):
		self.model = model
	
	def set_textblobdoc(self, sentence):
		self.doc = self.model(sentence)._.blob
	
	def get_textblob(self, sentence, blob_model):
		# self.doc = self.model(sentence)._.blob
		return blob_model(sentence)
	    
	def get_sentiment(self, sentence):
		# expect a list of tuples
		# e.g [(['word1','word2'],1.0, 1.0, None)] 
		# or [(['',''],1.0, 1.0, None), (['',''],-0.5, 1.0, None)] 
		return []
	
	def get_polarity(self, sentence):
		# expect a float between 0 and 1
		return float(0.0)
	
	def get_subjectivity(self, sentence):
		# expect a float between 0 and 1
		return float(0.0)
	
	def get_ngram(self, sentence):
	    # expect like [WordList(['I', 'am', 'very']),
		# WordList(['but', 'sad', 'about']), WordList(['sad', 'about', 'yesterday'])]
	    return []

class TextBlobSpacy:
    def __init__(self, sentence):
        self.sentence = sentence

    def __call__(self):
	    return self.sentence
	 


# import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob

# class BlobTextClient:
# 	def __init__(self, model):
# 		self.model = model
	
# 	def set_textblobdoc(self, sentence):
# 		self.doc = self.model(sentence)._.blob
	
# 	def get_sentiment(self):
# 		return self.doc.sentiment
	
# 	def get_polarity(self):
# 		return self.doc.polarity
	
# 	def get_subjectivity(self):
# 		return self.doc.subjectivity
	
# 	def get_ngram(self):
# 	    return self.doc.ngram
# class TextBlobSpacy:
#     def __init__(self):
#         self.model = spacy.load("en_core_web_sm")
#         self.model.add_pipe('spacytextblob')
    
#     def get_model(self):
#         return self.model

        
