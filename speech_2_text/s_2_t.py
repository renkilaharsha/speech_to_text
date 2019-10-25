import speech_recognition as sr
import sys
from speech_2_text.submodule.abbreviations import Abbreviation

class speech_to_text:

    def __init__(self,sample_rate,chunck_size):
        self.sample_rate = sample_rate
        self.chunck_size = chunck_size
        self.r = sr.Recognizer()


    def convert(self):
        while(True):
            with sr.Microphone( sample_rate = self.sample_rate,chunk_size = self.chunck_size) as source:
                self.r.adjust_for_ambient_noise(source)
                print("Say Something")
                audio = self.r.listen(source)

                try:
                    text = self.r.recognize_google(audio)


                    if(text == "exit"):
                        print("you said: " + text)
                        print("Good Bye" )
                        break

                    else:
                        con  = Abbreviation(text)
                        words = con.convert()
                        text = " ".join(words)
                        print("you said: " + text)

    #error occurs when google could not understand what was said

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")

                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                except SystemExit as c:
                    print("Good Bye")


