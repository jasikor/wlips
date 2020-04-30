import argparse
import sys
import shutil

from scripts.src.CharacterSetsReader import CharacterSetsReader
from scripts.src.WordListCreator import WordListCreator
from scripts.src.FileHash import FileHash

parser = argparse.ArgumentParser(
    description="Create word list based on the preliminary word list",
    epilog="Example: python3 scripts/create_word_list.py -l language")
parser.add_argument('-l', '--language', required=True)

args = parser.parse_args()
preliminary_word_list_path = "../wlip-0003/preliminary-word-lists/" + args.language

character_sets = CharacterSetsReader().parse("../wlip-0001/character-sets/")
word_list_creator = WordListCreator()
try:
    word_list = word_list_creator.create_word_list(preliminary_word_list_path, character_sets)
except:
    print("error: unable to parse word list file: '{}'".format(preliminary_word_list_path))
    sys.exit(1)

print("Created word list:\n")
print(word_list)

with open("temp_word_list", "w") as f:
    for word in word_list:
        f.write(word + '\n')

file_hash = FileHash().compute_file_hash("temp_word_list")
word_list_path = "../wlip-0003/word-lists/" + args.language + "-" + file_hash
shutil.move("temp_word_list", word_list_path)

sys.exit(0)
