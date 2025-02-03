import os, sys
from pathlib import Path





def merge_files(input_dir, output, extensions):
    files = []
    for extension in extensions:
        files += list(Path(input_dir).rglob(f"*.{extension}"))

    #check if output exists 
    if os.path.isfile(output):
        raise Exception(f'File {exists}, aborting! Please delete or rename existing file and run again, or change the output file')

    with open(output, 'w') as output_file:
        for file in files:
            with open(str(file), 'r') as f:
                output_file.write(f'------- start of {file} -------\n')
                output_file.write(f.read())
                output_file.write(f'----- end of {file} -----\n')



if __name__=='__main__':
    input_dir, output = sys.argv[1:3]
    extensions = sys.argv[3:]
    merge_files(input_dir, output, extensions)


    
