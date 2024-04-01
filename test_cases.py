import unittest
from Artwork import Artwork
from Exhibition import Exhibition
from Visitor import Visitor
from Ticket import Ticket
from PriceCalculator import PriceCalculator
from SpecialEvent import SpecialEvent

class TestArtwork(unittest.TestCase):
    def test_artwork_info(self):
        artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent Gallery")
        expected_output = "Title: Mona Lisa, Artist: Leonardo da Vinci, Location: Permanent Gallery"
        actual_output = artwork.get_info()
        self.assertEqual(actual_output, expected_output)

# Add more test cases for other classes as required

if __name__ == '__main__':
    unittest.main()
