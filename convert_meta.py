# convert meta data from Notable into a folder structure for typora
# move images and relink



path_to_test_file = "./test_folder/Kegging.md"
base_notes_path = '.'

def open_file(file_path):
	document = []
	with open(file_path) as fhandle:
		for line in fhandle : document.append(line)
	return document

def parse_metadata(document):
	metadata = {}
	for line in document:
		split_line = line.split()
		# print(split_line)
		if len(split_line) < 1 : pass
		elif split_line[0] == 'tags:' : metadata['tags'] = split_line[1].replace('[', '').replace(']', '')
		elif split_line[0] == 'title:' : metadata['title'] = split_line[1]
		elif split_line[0] == 'attachments:' : pass

	return metadata

def create_folder():
	# check if folder already exists
	pass

def move_file():
	pass

def remove_metadata():
	pass

document = open_file(path_to_test_file)
# print(document)
doc_metadata = parse_metadata(document)
print(doc_metadata)