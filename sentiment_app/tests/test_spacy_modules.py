import unittest
from blobtext_client import BlobTextClient
from test_blobtextmodel import TextBlobGenericModel

class TestBlobTextClient(unittest.TestCase):
    
	def test_get_empty_sentiment_dict_for_empty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		modeltestdouble.return_textblob_doc([])
		btc = BlobTextClient(modeltestdouble)
		text_sentiment = btc.get_sentiment("") # empty string 
		self.assertIsInstance(text_sentiment, dict)
		
	def test_get_empty_sentiment_dict_for_nonempty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		modeltestdouble.return_textblob_doc([])
		btc = BlobTextClient(modeltestdouble)
		text_sentiment = btc.get_sentiment("Not interested much in thinks today") # nonempty string 
		self.assertIsInstance(text_sentiment, dict)
    
	def test_get_non_empty_sentiment_for_nonempty_text(self):
		"""
		Serialise output of testblob is serialise to expected dict
		"""
		modeltestdouble = TextBlobGenericModel('eng_model')
		sentimentlist = [(['ultimate','finally'], 0.0, 1.0,None),   # example of sentiment anaylsis from textblob
		                 (['able'], 0.5, 0.625, None),
						 (['fearful'], -0.9, 1.0,None) ]
		modeltestdouble.return_textblob_doc(sentimentlist)
		
		expected_result = {"sentimentwords": [
			                                {"words":['ultimate','finally'], "wordpolarity":0.0, "wordsubjectivity":1.0},
							                {"words":['able'], "wordpolarity":0.5, "wordsubjectivity":0.625},
				                            {"words":['fearful'], "wordpolarity":-0.9, "wordsubjectivity":1.0}
											]}
		btc = BlobTextClient(modeltestdouble)
		result = btc.get_sentiment('....')
		self.assertListEqual(result["sentimentwords"],expected_result["sentimentwords"])
	
	def test_get_subjectivity_float_for_empty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		modeltestdouble.return_textblob_doc('')
		btc = BlobTextClient(modeltestdouble)
		text_subjectivity = btc.get_subjectivity("")
		self.assertIsInstance(text_subjectivity, float)

	def test_get_subjectivity_float_for_nonempty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		sentimentlist = [(['ultimate','finally'], 0.0, 1.0,None),   # example of sentiment anaylsis from textblob
		                 (['able'], 0.5, 0.625, None),
						 (['fearful'], -0.9, 1.0, None)]
		modeltestdouble.return_textblob_doc(sentimentlist)
		btc = BlobTextClient(modeltestdouble)
		text_subjectivity = btc.get_subjectivity("....")
		# expected = in range[0,1]
		self.assertTrue(0<=text_subjectivity<=1)
	
	def test_get_polarity_float_for_empty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		modeltestdouble.return_textblob_doc('')
		btc = BlobTextClient(modeltestdouble) #[-1.0, 1.0] 0.35
		text_polarity = btc.get_polarity('.......')
		self.assertIsInstance(text_polarity, float)
	
	def test_get_polarity_float_for_nonempty_text(self):
		modeltestdouble = TextBlobGenericModel('eng_model')
		sentimentlist = [(['ultimate','finally'], 0.0, 1.0,None),   # example of sentiment anaylsis from textblob
		                 (['able'], 0.5, 0.625, None),
						 (['fearful'], -0.9, 1.0,None)]
		modeltestdouble.return_textblob_doc(sentimentlist)
		btc = BlobTextClient(modeltestdouble) #[-1.0, 1.0]
		text_polarity = btc.get_polarity('...') 
		# expected = in range[-1,1] # 0.037500000000000006
		self.assertTrue(-1<=text_polarity<=1)
    
