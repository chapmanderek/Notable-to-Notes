# Notable to Notes (or Typora in my case)
## Purpose
Attempts to migrate the Notable metadata and attachment style into a more standard nested folder structure and image linking.

Also attempts basic clean up by making the heading and title of the file matchup and removing leading whitespace from the top of the file.

## Usage
This script should be run from the base of your Notable information location.

--Notable_Notes (#or whatever you called it#)
    |
    | this script.py
    |
    |- notes/
    |
    |- attachments/

## Side Notes
Leaves the old files in place and creates new files.

If the deleted tag is present the file is skiped.

For docs with multiple tags the first tag is taken as the folder path.