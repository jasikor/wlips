# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.WordListCreator import WordListCreator

class TestWordListCreator(unittest.TestCase):

    scenarios_get_words = [
        ([], []),
        (["\n"], []),
        (["# any line starting with hash"], []),
        (["aaaa\n"], ["aaaa"]),
        (["aaaa\n", "bbbb\n"], ["aaaa", "bbbb"]),
        (["aaaa,bbbb\n"], ["aaaa", "bbbb"]),
        (["aaaa,bbbb,cccc\n"], ["aaaa", "bbbb", "cccc"])
    ]
    def test_get_words(self):
        for lines, expected_list_of_words in self.scenarios_get_words:
            with self.subTest():
                self.assertEqual(expected_list_of_words, WordListCreator().get_words(lines))

    scenarios_create_map_of_neighbours = [
        (["aaaa"], {"aaaa": set()}),
        (["aaaa", "bbbb"], {"aaaa":set(), "bbbb":set()}),
        (["aaaa", "aaab"], {"aaaa":set(["aaab"]), "aaab":set(["aaaa"])}),
        (["aaaa", "baaa", "abaa", "aaba", "aaab", "ffff"], {"aaaa":set(["baaa", "abaa", "aaba", "aaab"]), "baaa":set(["aaaa"]), "abaa":set(["aaaa"]), "aaba":set(["aaaa"]), "aaab":set(["aaaa"]), "ffff":set()})
    ]
    def test_create_map_of_neighbours(self):
        for words, expected_map_of_neighbours in self.scenarios_create_map_of_neighbours:
            with self.subTest():
                self.assertEqual(expected_map_of_neighbours, WordListCreator().create_map_of_neighbours(words))

    scenarios_create_sets_of_neighbours = [
        ({"aaaa":set()}, {frozenset(["aaaa"])}),

        ({"aaaa":set(), "bbbb":set()}, {frozenset(["aaaa"]), frozenset(["bbbb"])}),

        ({"aaaa":set(["aaab"]), "aaab":set(["aaaa"])}, {frozenset(["aaaa", "aaab"])}),

        ({"aaaa":set(["baaa", "abaa", "aaba", "aaab"]), "baaa":set(["aaaa"]), "abaa":set(["aaaa"]), "aaba":set(["aaaa"]), "aaab":set(["aaaa"]), "ffff":set()},
         {frozenset(["aaaa", "baaa", "abaa", "aaba", "aaab"]), frozenset(["ffff"])}),

        ({"aaaa":set(["aaab"]), "aaab":set(["aaaa"]), "babb":set(["baab"]), "baab":set(["babb", "aaab"])}, {frozenset(["aaaa", "aaab", "baab", "babb"])}),
    ]
    def test_create_sets_of_neighbours(self):
        for map_of_neighbours, expected_sets_of_neighbours in self.scenarios_create_sets_of_neighbours:
            with self.subTest():
                self.assertEqual(expected_sets_of_neighbours, WordListCreator().create_sets_of_neighbours(map_of_neighbours))

if __name__ == '__main__':
    unittest.main()
