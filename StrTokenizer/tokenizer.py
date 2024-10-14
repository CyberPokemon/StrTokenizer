class StrTokenizer:
    def __init__(self,inputstring:str,delimeter: str=" ",return_delims: bool=False):
        self.inputstr=inputstring
        self.delim=delimeter
        self.returndelims=return_delims
        self.tokens=[]
        self.index=0
        self.nooftokens=0

        self.create_token()#string is being divided into tokens
    
    def create_token(self) -> None:
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
    
    def countTokens(self) -> int:
        return len(self.tokens)
    
    def countTokensLeft(self) ->int:
        return len(self.tokens)-self.index
    
    def hasMoreTokens(self) -> bool:
        return self.index < len(self.tokens)
        
    def nextToken(self) ->str:
        if self.index==self.nooftokens:
            raise IndexError("No more tokens available.")
        else:
            self.index+=1
            return self.tokens[self.index-1]
        
    def rewind(self, steps=None) -> None:
        if steps is None:
            self.index = 0
        else:
            if self.index - steps < 0:
                raise IndexError("INVALID INDEX")
            else:
                self.index -= steps