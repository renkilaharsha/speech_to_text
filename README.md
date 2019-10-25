
# Speech to Text conversion #

--------
Prerequisites 
--------
    PYTHON : >= 3.5
    Os : linux(Ubuntu,debian, etc)
Required installations:

        sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
        sudo apt-get install python3-pyaudio
        
        " Pyaudio related dependencies to be installed in the System"

 ----------
 Installation
 ------------
 
 1. Clone the repository
    
        git clone https://github.com/renkilaharsha/speech_to_text.git

2. Change directory

        cd speech_to_text-master/speech_2_text
        
 3. Install the setup.py file
 
        python3 setup.py install 
                      or
        sudo python3 setup.py install 
        
 ---------
 Usage of package speech to text
 ------------
 
     >>> from speech_2_text.s_2_t import speech_to_text 
     >>> var = speech_to_text(48000,2048) 
     >>> var.convert()
     ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
     ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
     ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
     ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
     ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
     ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
     ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map  
     Cannot connect to server socket err = No such file or directory
     Cannot connect to server request channel
     jack server is not running or cannot be started
     JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
     JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
     
      Say something :         ------input from the internal microphone
      You said:               ------Output to  STDOUT(Converted text)

------
NOTE
------

      
  #### *Use Earphone or Headphone for input to program (Recommended).* ####
  #### *Please Connect your system to working internet otherwise the conversion will not be done.* ####

--------
Example:
--------

    (Input - Audio from internal microphone) Say Something  : " Double B is better than Triple C" (audio)
    (Output - to display ) you said: BB is better than ccc
    
    The program will run untill the Exit is spoken:
    
    Say Something : "Exit" (audio)
    you said: exit
    Good Bye


     

------
Design
------

speech_to_text.ipynb uses Google Speech Recognition API to convert the given English speech to text. Sample rate and chunk size are two arguments in the speech API used. The default sample rate(48000 samples per second) and chunk size of 10240 Bytes has been considered as the storage space which handles around 1-2 lines of speech. Chunk size has the flexibilty to be increased so that it can handle sufficiently large amounts of data. 

The speech converted using Google Speech API is sent as a parameter to the Abbreviation class invoked from package called Abbreviations in main program. The Abbreviation class invokes convert function which takes the input as text and generates the processed text as output. For instance, 

    Input : Triple A ,Output : AAA;
    Input : Dollars 2 ,Output : $2;
    Input : 25 degrees, Output : 25 °C;

As we can see above, quantification(double,triple,etc.), units of temperature(Fahrenheit, Celsius,etc.) and monetary units(Rupees, Dollars,etc.) have been implemented as a part of this code.

------------
Future Scope
------------
More features like converting mathematical operators into symbols in a spoken equation/expression can be converted into written  mathematical format. For example,

    Input : square root of 4 plus 1, Ouput : √4+1

