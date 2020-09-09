class towords:
    def __init__(self,p):
        self.sen=p.split('.')
        self.words=[]
        for i in self.sen:
            self.words.append(i.split(' '))
    def getsen(self):
        return self.sen
    def getword(self):
        return  self.words
    def getwords(self,sen):
        return  sen.split(' ')
