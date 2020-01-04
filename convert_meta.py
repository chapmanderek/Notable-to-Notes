# convert meta data from Notable into a folder structure for typora
# move images and relink

import os
import sys

path_to_test_file = "./test_folder/Kegging.md"
notes_path = '.'
destination_path = './converted_notes/'
overwrite_files = True

def Read_File(file_path):
	document = []
	with open(file_path) as fhandle:
		for line in fhandle : document.append(line)
	return document

def Parse_Metadata(document):
	metadata = {}
	metadata['deleted'] = False

	# check if there is even a header from notable, assumes the first char of the first line will be a dash
	if document[0][0] != '-' : return metadata

	# if there is metadata then get and organize it
	for idx, line in enumerate(document):
		split_line = line.split()
		if len(split_line) < 1 : pass
		elif split_line[0] == 'tags:': 
			metadata['tag'] = (
				split_line[1].replace('[', '')
							 .replace(']', '')
							 .replace(',', '') 
							 )
		elif split_line[0] == 'title:' : metadata['title'] = split_line[1]
		elif split_line[0] == 'deleted:' : metadata['deleted'] = True
		elif split_line[0] == 'attachments:' : pass
		elif idx > 1 and split_line[0] == '---' : return metadata

	return metadata

def Set_Doc_Title(document, metadata):
	doc_title = '# ' + metadata['title'] + '\n'

	if document[0] == doc_title:
		return document
	else:
		document.insert(0, doc_title)
		return document

def Tag_to_Path(metadata, dest_path):
	doc_tag = metadata['tag']

	# remove the Notebook part of the tag if present as being superfulous
	doc_tag = doc_tag.replace('Notebooks/', '')

	# make sure the destination path ends with a forward slash
	if dest_path[-1] != '/':
		dest_path = dest_path + '/'

	# combine the destination path and the tag into a complete path
	folder_path = dest_path + doc_tag + '/'

	return folder_path

def Create_Folder(metadata):
	folder_path = metadata['folder path']
	
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

def Write_Document(document, metadata):
	if destination_path[-1] == '/':
		doc_path = destination_path + metadata['title'] + '.md'
	else:
		doc_path = destination_path +'/' + metadata['title'] + '.md'

	with open(doc_path, 'w') as doc_path_handle:
		for line in document:
			doc_path_handle.write(line)

def Remove_Metadata(document):
	if document[0][0] != '-' : return document
	
	document.pop(0) # get rid of the first line which should be the metadata beginner
	for idx, line in enumerate(document):
		if line == '---\n' : return document[(idx+1):]

	print('something went wrong')
	sys.exit(1)

def Remove_Empty_Beginning(document):
	for idx, line in enumerate(document):
		if line == '\n' or line == '' : pass
		else : return document[idx:]

document = Read_File(path_to_test_file)
doc_metadata = Parse_Metadata(document)

if not doc_metadata['deleted']:
	document = Remove_Metadata(document)
	document = Remove_Empty_Beginning(document)
	document = Set_Doc_Title(document, doc_metadata)
	doc_metadata['folder path'] = Tag_to_Path(doc_metadata, destination_path)
	Create_Folder(doc_metadata)
	# Write_Document(document, doc_metadata)

# print(document)
for key in doc_metadata:
	print('{k} : {v}'.format(k=key,v=doc_metadata[key]) )

# print(doc_metadata)