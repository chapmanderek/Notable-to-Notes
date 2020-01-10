# convert meta data from Notable into a folder structure for typora (similar other markdown program)
# move images and relink

import os
import sys

path_to_test_file = "./test_folder/Kegging.md"
notes_path = '.'
destination_path = './converted_notes/'
# overwrite_files = True   does nothing yet


def Read_File(file_path):
    document = []
    with open(file_path) as fhandle:
        for line in fhandle:
            document.append(line)
    return document


def Tag_meta_line(line):
    # tags: [stuff to keep, otherthings]
    # if there are multiple tags (hence the comma) attempt to grab the first tag and correctly handle tags with spaces in the name
    if ',' in line:
        line = line.split(',')
        line = line[0].split()
        main_tag = '_'.join(line[1:len(line)]) #drop the tags: part and join the rest of the main tag into a valid folder name (no spaces)
    elif ',' not in line:
        line = line.split()
        main_tag = line[1]

    main_tag = main_tag.replace('[', '') \
                    .replace(']', '') \
                    .replace(',', '')
    return main_tag


def Title_meta_line(line):
    line = line.split()
    # correctly handle titles with spaces in the name
    if len(line) > 2:
        title = ' '.join(line[1:len(line)])
        return title
    elif len(line) == 2:
        return line[1]


def Parse_Metadata(document):
    metadata = {}
    metadata['deleted'] = False

    # check if there is a header from notable,
    # assumes the first char of the first line will be a dash
    if document[0][0] != '-':
        return False

    # if there is metadata then get and organize it
    for idx, line in enumerate(document):
        # split_line = Split_meta_line(line)
        split_line = line.split()

        if len(split_line) < 1:
            pass
        elif split_line[0] == 'tags:':
            metadata['tag'] = Tag_meta_line(line)
        elif split_line[0] == 'title:':
            metadata['title'] = Title_meta_line(line)
        elif split_line[0] == 'deleted:':
            metadata['deleted'] = True
        elif split_line[0] == 'attachments:':
            metadata['attachments'] = True
        elif idx > 1 and split_line[0] == '---':
            return metadata

    return metadata


def Set_Doc_Title(document, metadata):
    doc_title = '# ' + metadata['title'] + '\n'

    if document[0] == doc_title:
        return document
    else:
        document.insert(0, doc_title)
        return document


def Tag_to_Folder_Path(metadata, destination_path):
    doc_tag = metadata['tag']

    # remove the Notebook part of the tag if present as being superfulous
    doc_tag = doc_tag.replace('Notebooks/', '')

    # make sure the destination path ends with a forward slash
    if destination_path[-1] != '/':
        destination_path = destination_path + '/'

    # combine the destination path and the tag into a complete folder path
    metadata['folder path'] = os.path.join(destination_path, doc_tag)

    return metadata


def Create_Folder(metadata):
    if not os.path.exists(metadata['folder path']):
        os.makedirs(metadata['folder path'])


def Write_Document(document, metadata):
    title = metadata['title']

    if ' ' in title:
        title = title.split()
        title = '_'.join(title)

    doc_path = metadata['folder path'] + '/' + title + '.md'
    with open(doc_path, 'w') as doc_path_handle:
        for line in document:
            doc_path_handle.write(line)


def Remove_Metadata(document):
    if document[0][0] != '-':
        return document

    # get rid of the first line which should be the metadata beginning
    document.pop(0)
    for idx, line in enumerate(document):
        if line == '---\n':
            return document[(idx + 1):]

    print('something went wrong')
    sys.exit(1)


def Remove_Empty_Beginning(document):
    for idx, line in enumerate(document):
        if line == '\n' or line == '':
            pass
        else:
            return document[idx:]


def Remove_Empty_Ending(document):
    document.reverse()
    for idx, line in enumerate(document):
        if line == '\n' or line == '':
            pass
        else:
            document = document[idx:]
            document.reverse()
            return document


document = Read_File(path_to_test_file)
metadata = Parse_Metadata(document)

if not metadata['deleted']:
    document = Remove_Metadata(document)
    document = Remove_Empty_Beginning(document)
    document = Remove_Empty_Ending(document)
    document = Set_Doc_Title(document, metadata)
    metadata = Tag_to_Folder_Path(metadata, destination_path)
    Create_Folder(metadata)
    Write_Document(document, metadata)

# print(document)
# for key in metadata:
#     print('{k} : {v}'.format(k=key, v=metadata[key]))
