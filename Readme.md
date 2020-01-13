# Migrate Notable Metadata to 'Standard' MD Notes Structure
## Purpose
Attempt to migrate the Notable metadata and attachment style into a more standard nested folder structure and image linking.

Also attempts basic clean up by making the heading and title of the file matchup and removing  whitespace from the top/bottom of the file.

## Usage
This script should be run from the base of your Notable information location.

--Notable_Notes (*or whatever you called it*)
    |
    | this script.py
    |
    |- notes/
    |
    |- attachments/
    |
    |- converted_notes/

When finished all notes will be moved into a folder structure based on their main tag in converted_notes and all attached images into an images folder inside of each folder containing that note.

## Side Notes
Leaves the old files in place and creates new files.

If the deleted tag is present the file is skiped.

For docs with multiple tags the first tag is taken as the folder path.

Uses the title tag for the first line of the document as well as the name of the file.