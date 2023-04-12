class MedPlus:
    def __init__(self,Name:str,Batch_Number:int,Price:float):
        self.Name = Name
        self.Batch_Number= Batch_Number
        self.Price= Price
    def set_Name(self, Name:str):
        self.Name = Name
    def set_Batch_Number(self, Batch_Number:int):
        self.Batch_Number= Batch_Number
    def set_Price(self, Price:float):
        self.Price= Price
    
    def get_Name(self) -> str:
        return self.Name
    
    def get_Batch_Number(self) -> int:
        return self.Batch_Number
    
    def get_Price(self) -> float:
        return self.Price
Medicine= MedPlus("paracitamol",25,12.21)
print(Medicine.get_Name())
Medicine.set_Price(50.100)
print(Medicine.get_Price())
