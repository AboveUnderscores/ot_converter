import os
import time
import pathlib
import wav_convert as wc


#put directories of input and output folders here! the output folder will contain the input folder as well as all subfolders
input_directory = "D:\Music Making\CIKARA\Sample Packs\CIKARA - Transistor"
output_directory = "D:\Music Making\CIKARA\Misc"


#gets folder that we want to convert from path
path1 = pathlib.Path(input_directory)
folder = path1.parent.name if not path1.is_dir() else path1.name

#creates timestamped dump file that shows any errors
timeStr = time.strftime('%m-%d-%Y_%H%M%S')
dumpName = 'convert_dump\convert_' + folder + '_' + timeStr + '.txt'
with open(dumpName, 'w') as txt:
    txt.write('Converting Files From ' + input_directory + '\n \n')

#walks thru input directory and converts all audio files
for root, dirs, files in os.walk(input_directory):
    for file in files:

        #gets file from root [ ex. C:\\Production\\Samples\\One_Shot\\Drums\\Snare\\young_chop_snare.mp3 ]
        input_file = root + '\\' + file 
        #grabs just file name
        fname = os.path.splitext(file)[0] 
        #grabs just file ext
        ext = os.path.splitext(file)[1] 

        if(ext == '.mp3') or (ext == '.wav') or (ext == '.WAV') or (ext == '.aif') or (ext == '.flac'):

            #gets structure of folder that you are trying to convert files in [ for example, Samples\\One_Shot\\Drums\\Snare ]
            rt = root
            folder_structure = rt[rt.rindex(folder):] 
            #creates structure of output file from root [ for example, C:\\Production\\Samples\\ ]
            output = output_directory + '\\' + folder_structure + '\\' 
            #print(input_file)
            #print(output + '\n')

            #duplicates folder structure of input folder and tries to convert audio
            os.makedirs(output, mode=0o777, exist_ok=True)
            wc.convert(input_file, output, fname, dumpName, root)


        #catches files that can't be converted and passes some common non-audio files
        else:
            with open(dumpName, "a") as txt:
                if not ((ext == '.asd') or (ext == '.ini') or (ext == '.xmp') or (ext == '.lnk') or (ext == '.mid') or (ext == '.txt')):
                    txt.write('FILE INCORRECT TYPE:  ' + input_file + "\n")
with open(dumpName, "a") as txt:
    txt.write('\nDONE WITH CONVERSION')
print('DONE WITH CONVERSION')