
class Abbreviation:
    def __init__(self,text):
        self.text = text 
        self.words = self.text.split()
        self.degree = {"Celsius":"°C","Centigrade":"°C","centrigrade":"°C","celsius":"°C","Fahrenheit":"°F","fahrenheit":"°F"}
        self.num_tuple = { "single" : 1 ,"double":2,"triple":3,"quadruple":4,"quintuple":5,"sextuple":6,"septuple":7, "octuple":8 ,"nonuple":9,  "decuple":10,"undecuple":11 ,  "duodecuple":12,   "tredecuple":13
, "centuple": 100 , "Single" : 1 ,"Double":2,"Triple":3,"Quadruple":4,"Quintuple":5,"Sextuple":6,"Septuple":7, "Octuple":8 ,"Nonuple":9,  "Decuple":10,"Undecuple":11 ,  "Duodecuple":12,   "Tredecuple":13
, "Centuple": 100}
        self.money = {"rupees":"₹","Rupees":'₹'}
        self.lst = []

    def quantification(self,i):

        """ This function converts the words like "Triple A" to "AAA" """
        if(self.words[i] in self.num_tuple):
            count = self.num_tuple[self.words[i]]
            if(i != (len(self.words)-1)):
                self.words[i+1] = self.words[i+1]*count
                self.lst.append(i)

    def degreeconversion(self,i): 
        """This fuctionconverts the text like "25 degrees centigrade" to "25 °C " """
        if(self.words[i] in self.degree):
            if(i != 0):
                if(i-1 >= 0):
                    if(self.words[i-2].isnumeric() ==True and (self.words[i-1]=='degree' or self.words[i-1]=='Degree' or self.words[i-1]=='degrees' or self.words[i-1]=='Degrees'  )):
                        self.words[i] = self.degree[self.words[i]]
                        self.lst.append(i-1)
    def monetory(self,i):
        """ This function converts the text like 25 rupees to "₹" """
        if(self.words[i] in self.money):
            if( i !=0):
                if(i-1 >0):
                    if(self.words[i-1].isnumeric() == True):
                        self.words[i-1] = self.money[self.words[i]]+self.words[i-1]
                        self.lst.append(i-1)


    def convert(self):

        for  i in range(len(self.words)):
            self.quantification(i)
            self.degreeconversion(i)

        for j in range(len(self.lst)):
            self.words.pop(self.lst[j]-j)
        return(self.words)

