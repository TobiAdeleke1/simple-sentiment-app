# import spacy

# from spacytextblob.spacytextblob import SpacyTextBlob

class BlobTextClient:
	def __init__(self, model):
		self.model = model
	
	def get_sentiment(self, sentence):
		# get a list of tuples, want to conver
		# e.g [(['word1','word2'],1.0, 1.0, None)] 
		# or [(['',''],1.0, 1.0, None), (['',''],-0.5, 1.0, None)] 
		blob_doc = self.model(sentence).sentimentlist
		sentiment = [
			        {"words":sentence_word.keywordlist,
	                "wordpolarity":sentence_word.keywordpolarity, 
					"wordsubjectivity":sentence_word.keywordsubjectivity}
					 for sentence_word in blob_doc]
		return {"sentimentwords":sentiment}
	
	def get_polarity(self, sentence):
		# expect a float between -1 and 1
		blob_doc = self.model(sentence)
		return blob_doc.overallpolarity
	
	def get_subjectivity(self, sentence):
		doc = self.model(sentence) # expect a float between 0 and 1
		return doc.overallsubjectivity

 

# class TextBlobSpacy:
#     def __init__(self, sentence):
#         self.sentence = sentence

#     def __call__(self):
# 	    return self.sentence
	 
