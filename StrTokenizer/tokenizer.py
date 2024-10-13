class StrTokenizer:
    def __init__(self,inputstring,delimeter=" ",return_delims=False):
        self.inputstr=inputstring
        self.delim=delimeter
        self.returndelims=return_delims
        self.tokens=[]
        self.index=0

        self.create_token()#string is being divided into tokens
    
    def create_token(self):
        w=""

        for i in self.inputstr:
            if i in self.delim:
                if w!="":
                    self.tokens.append(w)
                if self.returndelims:
                    self.tokens.append(i)
            else:
                w=w+i