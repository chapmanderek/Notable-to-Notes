# convert meta data from Notable into a folder structure for typora
# move images and relink

import os

path_to_test_file = "./test_folder/Kegging.md"
notes_path = '.'
destination_path = './converted_notes/'

def open_file(file_path):
	document = []
	with open(file_path) as fhandle:
		for line in fhandle : document.append(line)
	return document

def parse_metadata(document):
	metadata = {}

	# check if there is even a header from notable, assumes the first char of the first line will be a dash
	if document[0][0] != '-' : return metadata

	# if there is metadata then get and organize it
	for idx, line in enumerate(document):
		split_line = line.split()
		if len(split_line) < 1 : pass
		elif split_line[0] == 'tags:' : metadata['tags'] = split_line[1].replace('[', '').replace(']', '')
		elif split_line[0] == 'title:' : metadata['title'] = split_line[1]
		elif split_line[0] == 'attachments:' : pass
		elif idx > 1 and split_line[0] == '---' : return metadata

	return metadata

def set_title(document, metadata):
	pass

def create_folder():
	# check if folder already exists
	pass

def move_file():
	pass

def remove_metadata():
	pass

document = open_file(path_to_test_file)
doc_metadata = parse_metadata(document)

print(doc_metadata)