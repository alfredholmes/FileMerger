# FileMerger
Merge all files with a given list of to one text file.

## Usage

1. Clone the repository
2. Copy a folder into your local copy of the repo
3. Run merge.py to merge the files into one output.

## merge.py usage 
```
python merge.py input_directory output_file ext1 ext2 ext3 ...
```
The above will create a list of all the files (recursivley) in the directory `input_directory` with file extensions ext1, ext2, ext3 and so on and create a text file `output_file` that is all of the files in the list merged into one file.

Example
```
python merge.py obsidian_vault obsidian.md md
```

