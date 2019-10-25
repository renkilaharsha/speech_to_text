# Designing a spoken english to written english conversion system #

Designing the speech to text project will require continous update/addition  of rules according to the requirement. The continuous update/addtion of rules will not affect the previously defined rules. To achieve the above mentioned type of project, the project has to define in **modular progamming**.

    Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.
    
------------------
Design
------------------

 **Functionalities(Say)** :-
 
      1. Converting Speech to text.
      2. Taking care of Abbreviation.
          a) Monetory Units.
          b) Units of Measurements.
          c) Quantification.
          d) Mathematical Expressions.
          
       
1. Define rules for each functionalities mentioned above in Classes or functions.

    For example:-

        def monetory_units(input):
 
                ------
             # define rules 
               
                ------
     
            return(output)

2. Define each functionality in seperate file.

  Example:

     monetory.py
     measurements.py
     quantification.py
     speech_2_text.py
     mathematical_expressions.py
  
3. Define a new program which imports the defined functionalities and  invokes the functionalities required.

Which ever functionalities defined are required can be used in the main.py program.

  Example:
      
       program name :- main.py

       ### code starts 
       
       from speech_to_text.s_2_t import speech_2_text
       from  Abbreviations.monetory import monetory_units
       
       text =  speech_2_text(__parameters__)
       converted_text = monetory_units(text)
       
       ------------
       
       
Like above example we can invoke any functionality into main function.

### Directory design ###

    project (Module)
    |
    |
    ------> main.py 
      |
      |  Speech_to_text  (Sub Modules)
            |
            -----> s_2_t.py
            -----> __init__.py
      | Abbreviations     (Sub Modules)
            |
            -----> monetory.py
            -----> measurements.py
            -----> quantification.py
            -----> mathematical_expressions.py
            -----> __init__.py
            
            
           __init__.py file existing tells python complier that the folder is an module.
  
      
 
 ## To include the new functionality into the existing project ##
 
 New functionality :- Sentimentment analysis of speaker(wheather the speech is positive or negative or neutral)  
 
 1. Define the rules of functionalities in the ina file.
 
 2. Save the functionality defines in a seperate file.
 
 3. Add the the Sub Module(sentiment) in the module(Project).
 
 Example:
 
 a) Create a directory called Sentiment  in the project directory.
 
 b) Create a python file called  sentiment.py and __init__.py
 
 C) Define the rules in a function called senti_analysis() in sentiment.py
 
 
 ### Directory design  changes  to :###

    project (Module)
    |
    |
    ------> main.py 
      |
      |  Speech_to_text  (Sub Module)
            |
            -----> s_2_t.py
            -----> __init__.py
      | Abbreviations     (Sub Module)
            |
            -----> monetory.py
            -----> measurements.py
            -----> quantification.py
            -----> mathematical_expressions.py
            -----> __init__.py
            
      |Sentiment   (Sub Module)
            |
            -----> sentiment.py
            -----> __init__.py
            
 
 ## Using the new defined functionality in the existing project ##
 
 To use the new functionality we need not to change the existing sub modules and only change the main.py function.
 
  Example:
      
       program name :- main.py

       ### code starts 
       
       from speech_to_text.s_2_t import speech_2_text
       from  Abbreviations.monetory import monetory_units
       from Sentiment.sentiment import senti_analysis 
       
       text =  speech_2_text(__parameters__)
       converted_text = monetory_units(text)
       senti = senti_analysis(converted_text)
       
       
       ------------
 
 In the above example we just invoked the senti_analysis function and used in the main.py with out affecting the previously defined functionalities like monetory_units  etc..
 
 
 So by defining the rules which are independent will allow us to add new funcionalities with out affecting the previously defined functionalities.
 
 
