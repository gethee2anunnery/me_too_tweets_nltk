import nltk
import csv
from constants import WORDS_TO_IGNORE, ATTRS_TO_CAPTURE
from request import get_search_response
from pprint import pprint


def write_data_from_csv_to_dict():
	data = list()
	with open("metootweets.csv", 'rU') as file_data:
		csv_reader = csv.DictReader(file_data)
		for row in csv_reader:
			row_attrs = dict()
			# counts = get_word_counts_from_text(row['text'])
			# row_attrs['word_counts'] = counts
			for k, v in row.items():
				if k in ATTRS_TO_CAPTURE:
					row_attrs[k] = row[k]
			data.append(row_attrs)
	return data


def get_word_counts_from_text(row_text):
	word_counts = dict()
	if row_text:
		clean_text = row_text.replace('?', '').replace('.', '').replace('\n', "").replace(',', "").replace('"', "").replace('!', "").replace('#', "").lower()
		words = clean_text.split(' ')
		freq = nltk.FreqDist(words)
		for k, v in freq.items():
			if k and k not in WORDS_TO_IGNORE:
				word_counts[k] = v
		print word_counts
		return word_counts


def get_data():
	return write_data_from_csv_to_dict()


if __name__ == "__main__":
    get_data()
