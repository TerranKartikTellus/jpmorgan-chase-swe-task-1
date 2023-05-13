import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
       actual_data = getDataPoint(q)
       expected_output = ( q['stock'],q['top_bid']['price'], q['top_ask']['price'] , (q['top_bid']['price'] + q['top_ask']['price'])/2  )
       print(expected_output)
       self.assertEqual(actual_data, expected_output)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
       actual_data = getDataPoint(q)
       expected_data = ( q['stock'],q['top_bid']['price'], q['top_ask']['price'] , (q['top_bid']['price'] + q['top_ask']['price'])/2 ) 
       self.assertEqual(actual_data, expected_data)

  def test_getRatio(self):
    quotes = [
      {'inputA': 0,'inputB':1, 'output':0},
      {'inputA': 1,'inputB':0, 'output':None},
      {'inputA': 1,'inputB':2, 'output':0.5},
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
       actual_data = getRatio(q['inputA'],q['inputB'])
       expected_data = ( q['output'] ) 
       self.assertEqual(actual_data, expected_data)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
