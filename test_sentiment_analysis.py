from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer('I love playing basketball')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate running during preseason')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on defense in basketball.')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')


unittest.main()