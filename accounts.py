class AD:
    def __init__(self,nm,bal,id,pwd):
      self.name=nm
      self.balance=bal
      self.aid=id
      self.password=pwd

    def __str__(self):
        return str(self.aid)+","+str(self.password)+","+str(self.balance)+","+str(self.name)
       

    
         