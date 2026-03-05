import ffmpeg
import os

def convert(input, output_directory, fname, dumpName, root):
    try:
        #ffmpeg code to convert all files to 16 bit 44100Hz wav files
        output = output_directory + fname + ".wav"
        if not os.path.exists(output):
            (
                ffmpeg.input(input)
                .output(output, ar = 44100, sample_fmt = 's16', loglevel='quiet')
                .run()
            )

        #choose to say files succeeded in dump
        if(0):
            with open(dumpName, "a") as txt:
                txt.write('SUCCESS WITH FILE:  ' + input + "\n")

    #write errors to dump files
    except:
        with open(dumpName, "a") as txt:

            try:
                txt.write('ERROR WITH CONVERTING:  ' + input + "\n")
                pass
            except:
                txt.write('ERROR WITH CONVERTING FILE IN ' + root + ", NAME HAS UNSUPPORTED CHARACTER\n")
                pass