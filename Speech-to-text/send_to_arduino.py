import time
import os
import serial
from STTTrial import *
from Sentiment_Analysis import *

ser = serial.Serial('COM3', 9600, timeout=1)
def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)

    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated

        if not line:
            analyze(STT())
            time.sleep(0.1)
            continue

        yield line

if __name__ == '__main__':


    logfile = open(r"Speech-to-text/outro.txt","r")
    loglines = follow(logfile)
    # iterate over the generator
    for line in loglines:
        print(line)
        ser.write((line.strip() + '\n').encode())
        # Wait a bit to let Arduino process and display the line
        time.sleep(2)  # Adjust delay as needed