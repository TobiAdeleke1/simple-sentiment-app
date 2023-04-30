import unittest
from blobtext_client import BlobTextClient
from test_blobtextmodel import TextBlobSpacy,TextblobTestModel

class TestBlobTextClient(unittest.TestCase):
	def setUp(self):
		spacymodel = TextBlobSpacy().get_model()
		textblob = TextblobTestModel(spacymodel)
		
	
	def test_get_sentiment_tuple_for_empty_text(self):
		# model = BlobTextModel('eng')
		model = TextBlobSpacy().get_model()

		btc = BlobTextClient(model)
		sentiment = btc.get_sentiment("")
		self.assertIsInstance(sentiment, dict)
		# desired output {"polarity": .. , "subjectivity": ..,  }
	
	def test_get_sentiment_tuple_for_nonempty_text(self):
		# model = BlobTextModel('eng')
		model = TextBlobSpacy().get_model()
		btc = BlobTextClient(model)
		sentiment = btc.get_sentiment("I am happy about today")
		self.assertIsInstance(sentiment, dict)

	def test_get_polarity_for_empty_text(self):
		pass

	def test_get_polarity_for_nonempty_text(self):
		pass

	def test_get_subjectivity_for_empty_text(self):
		pass

	def test_get_subjectivity_for_nonempty_text(self):
		pass
    
	def test_get_ngram_for_empty_text(self):
		pass

	def test_get_ngram_for_nonempty_text(self):
		pass
	
