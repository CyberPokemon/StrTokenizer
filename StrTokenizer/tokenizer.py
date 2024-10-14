class StrTokenizer:
    def __init__(self,inputstring,delimeter=" ",return_delims=False):
        self.inputstr=inputstring
        self.delim=delimeter
        self.returndelims=return_delims
        self.tokens=[]
        self.index=0
        self.nooftokens=0

        self.create_token()#string is being divided into tokens
    
    def create_token(self):
        w=""

        for i in self.inputstr:
            if i in self.delim:
                if w!="":
                    self.tokens.append(w)
                if self.returndelims:
                    self.tokens.append(i)
                w=""
            else:
                w=w+i
        if w:
            self.tokens.append(w)
        self.nooftokens=len(self.tokens)
    
    def countTokens(self):
        return len(self.tokens)
    
    def countTokensLeft(self):
        return len(self.tokens)-self.index
    
    def hasMoreTokens(self):
        return self.index < len(self.tokens)
        
    def nextToken(self):
        if self.index==self.nooftokens:
            raise IndexError("No more tokens available.")
        else:
            self.index+=1
            return self.tokens[self.index-1]