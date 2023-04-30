import unittest
from blobtext_client import BlobTextClient
# from test_blobtextmodel import TextBlobSpacy,TextblobTestModel

class TestBlobTextClient(unittest.TestCase):
    
	@unittest.skip("Still need to think on how to test")
	def test_get_textblob_class_for_empty_text(self):
		btc = BlobTextClient('eng_model')
		text_sentiment = btc.get_textblob("","") # empty string 
		self.assertIsInstance(text_sentiment, list)

	def test_get_sentiment_list_for_empty_text(self):
		btc = BlobTextClient('eng_model')
		text_sentiment = btc.get_sentiment("") # empty string 
		self.assertIsInstance(text_sentiment, list)
		# desired output {"polarity": .. , "subjectivity": ..,  }
	

	def test_get_subjectivity_float_for_empty_text(self):
		btc = BlobTextClient('eng_model')
		text_subjectivity = btc.get_subjectivity("")
		self.assertIsInstance(text_subjectivity, float)
	
	def test_get_polarity_float_for_empty_text(self):
		tbc = BlobTextClient('eng_model')
		text_polarity = tbc.get_polarity('') # empty string 
		self.assertIsInstance(text_polarity, float)
    
	def test_get_ngram_list_for_empty_text(self):
		tbc = BlobTextClient('eng_model')
		text_ngram = tbc.get_ngram("")
		self.assertIsInstance(text_ngram, list)

    
	# def test_get_sentiment_tuple_for_nonempty_text(self):
	# 	# model = BlobTextModel('eng')
	# 	model = TextBlobSpacy().get_model()
	# 	btc = BlobTextClient(model)
	# 	sentiment = btc.get_sentiment("I am happy about today")
	# 	self.assertIsInstance(sentiment, dict)

	# def test_get_polarity_for_empty_text(self):
	# 	pass

	# def test_get_polarity_for_nonempty_text(self):
	# 	pass

	# def test_get_subjectivity_for_empty_text(self):
	# 	pass

	# def test_get_subjectivity_for_nonempty_text(self):
	# 	pass
    
	# def test_get_ngram_for_empty_text(self):
	# 	pass

	# def test_get_ngram_for_nonempty_text(self):
	# 	pass
	

# from blobtext_client import BlobTextClient
# from test_blobtextmodel import TextBlobSpacy,TextblobTestModel
# class TestBlobTextClient(unittest.TestCase):
# 	# def setUp(self):
# 	# 	spacymodel = TextBlobSpacy().get_model()
# 	# 	textblob = TextblobTestModel(spacymodel)
		
	
# 	def test_get_sentiment_tuple_for_empty_text(self):
# 		# model = BlobTextModel('eng')
# 		model = TextBlobSpacy().get_model()

# 		btc = BlobTextClient(model)
# 		sentiment = btc.get_sentiment("")
# 		self.assertIsInstance(sentiment, dict)
# 		# desired output {"polarity": .. , "subjectivity": ..,  }
	
# 	def test_get_sentiment_tuple_for_nonempty_text(self):
# 		# model = BlobTextModel('eng')
# 		model = TextBlobSpacy().get_model()
# 		btc = BlobTextClient(model)
# 		sentiment = btc.get_sentiment("I am happy about today")
# 		self.assertIsInstance(sentiment, dict)

# 	def test_get_polarity_for_empty_text(self):
# 		pass

# 	def test_get_polarity_for_nonempty_text(self):
# 		pass

# 	def test_get_subjectivity_for_empty_text(self):
# 		pass

# 	def test_get_subjectivity_for_nonempty_text(self):
# 		pass
    
# 	def test_get_ngram_for_empty_text(self):
# 		pass

# 	def test_get_ngram_for_nonempty_text(self):
# 		pass
	