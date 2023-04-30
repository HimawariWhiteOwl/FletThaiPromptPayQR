from pydantic import BaseModel
class DataQRModel(BaseModel):
    BillerId: str
    Ref1: str
    Ref2: str
    Amount: str