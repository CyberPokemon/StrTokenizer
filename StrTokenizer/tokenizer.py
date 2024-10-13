class StrTokenizer:
    def __init__(self,inputstring,delimeter=" ",return_delims=False):
        self.inputstr=inputstring
        self.delim=delimeter
        self.returndelims=return_delims
        self.tokens=[]
        self.index=0
    