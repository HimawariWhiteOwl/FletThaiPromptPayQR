from Model.DataQRCodeModel import DataQRModel


def TextNpmsFormat(model: DataQRModel):
    NPMSData: str = None
    try:
        if not ValidateData(model):
            return None

        NPMSData = f"|{model.BillerId}\r{model.Ref1}\r{model.Ref2}\r{model.Amount}"

    except Exception as e:
        print(type(e), str(e))
    return NPMSData


def ValidateData(model: DataQRModel):
    if len(model.Ref1) > 18:
        print(f"Error Length Reference1 Over limit, Maximum is 18 characters")
        return False
    if len(model.Ref2) > 18:
        print(f"Length Reference2 Over limit, Maximum is 18 characters")
        model.Ref2 = model.Ref2.replace(" ", "").replace("-", "").replace("_", "").upper()[0:18]
    if model.Ref2 == "nan":
        model.Ref2.replace("nan","")
    if len(model.Amount) > 10:
        print(f"Error Length Amount Over limit, Maximum is 10 characters")
        return False
    Amount = model.Amount
    AmountInt = Amount.split(".")[0]
    AmountDec = Amount.split(".")[1]
    AmountNPMSQR = f"{AmountInt}{AmountDec}"
    model.Amount = AmountNPMSQR
    return True
