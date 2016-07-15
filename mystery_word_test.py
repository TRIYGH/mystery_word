import unittest
from mystery_word_testingversion import *

word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]


class TestMysteryWord(unittest.TestCase):

    def test_easy_words(self):
        self.assertEqual(easy_words(word_list), ["bird", "calf", "river", "stream", "brain"])


    def test_medium_words(self):
        self.assertEqual(medium_words(word_list), ["stream", "kneecap", "cookbook", "language", "sneaker"])


    def test_hard_words(self):
        self.assertEqual(hard_words(word_list), ["cookbook", "language", "algorithm", "integration"])

    def test_random_word(self):
        """This test is not very good. Testing things that are random is hard,
        in that there's not a predictable choice. The best we can do is make
        sure we have valid output."""
        word = get_myst_word(word_list)
        self.assertTrue(word in word_list)


    def test_display_word(self):
        word = "integration"
        mlw = []
        mwl = list(word)
        self.assertEqual(display_board(8,"# # # # # # # # # # #",word,mlw,1), "# # # # # # # # # # #")
        self.assertEqual(display_board(8,"# # # # # # # # # # #",word,mlw,1), "# # # # # # # # # # #")
        self.assertEqual(display_board(8,"# # # # g # # # # # #",word,mlw,1), "# # # # g # # # # # #")
        self.assertEqual(display_board(8,"i # # # # # # # i # #",word,mlw,1), "i # # # # # # # i # #")
        self.assertEqual(display_board(8,"i # # # g # # # i # #",word,mlw,1), "i # # # g # # # i # #")
        self.assertEqual(display_board(8,"i n # # # # # # i # n",word,mlw,1), "i n # # # # # # i # n")


    def test_is_word_complete(self):
        word = "river"
        self.assertFalse(did_you_win(["#", " ", "#", " ", "#", " ", "#", " ", "#"]))
        self.assertFalse(did_you_win(["r", " ", "#", " ", "#", " ", "#", " ", "r"]))
        self.assertFalse(did_you_win(["r", " ", "#", " ", "#", " ", "e", " ", "r"]))
        self.assertFalse(did_you_win(["r", " ", "#", " ", "#", " ", "e", " ", "r"]))
        self.assertTrue(did_you_win(["r", " ", "i", " ", "v", " ", "e", " ", "r"]))


if __name__ == '__main__':
    unittest.main()
