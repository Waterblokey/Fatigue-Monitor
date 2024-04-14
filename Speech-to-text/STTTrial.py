#Trial program using whisper to convert mp4 file to text

import whisper

def STT():
    model = whisper.load_model("base")
    result = model.transcribe("Speech-to-text/outro.mp4", language="en")
    print(result["text"])
    return(result["text"])

