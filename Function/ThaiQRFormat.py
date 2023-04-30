from Model.DataQRCodeModel import DataQRModel
from ClassQRConfig import ThaiQRCodeConfig


def TextThaiQRTag30Format(model: DataQRModel, merchantName: str):
    if not ValidateData(model):
        return None
    config = ThaiQRCodeConfig
    datalist = []
    tag30datalist = []

    datalist.append(TagFormat(config.Tag00_PayloadFormat, config.Tag00_PayloadEMVCo_QRCode))
    datalist.append(TagFormat(config.Tag01_PointOfInitiation,
                              config.Tag01_POIDynamicMode if model.Amount != '' else config.Tag01_POIStaticMode))

    tag30datalist.append(TagFormat(config.TagAID, config.TagAID_DomesticMerchant)) #Mode
    tag30datalist.append(TagFormat(config.Tag30_BillerId, model.BillerId))
    tag30datalist.append(TagFormat(config.Tag30_Ref1, model.Ref1))
    tag30datalist.append(TagFormat(config.Tag30_Ref2, model.Ref2))
    tag30data = ''.join(tag30datalist)

    datalist.append(TagFormat(config.Tag30_BillPayment, tag30data))

    datalist.append(TagFormat(config.Tag53_TransactionCurrency, config.Tag53_TransactionCurrency_THB))
    datalist.append(TagFormat(config.Tag54_TransactionAmount, model.Amount if model.Amount != '' else ''))
    datalist.append(TagFormat(config.Tag58_CountryCode, config.Tag58_CountryCode_TH))
    datalist.append(TagFormat(config.Tag59_MerchantName, merchantName))

    data = ''.join(datalist)

    check_sum = f"{data}{config.Tag63_CRC}04"
    finalData = f"{data}{TagFormat(config.Tag63_CRC, CRC16CCITT(check_sum)).upper()}"
    # check_sum = hex(libscrc.ccitt(data.encode("ascii"), 0xffff)).replace('0x', '')
    # if len(check_sum) < 4:
    #     check_sum = ("0" * (4 - len(check_sum))) + check_sum
    # finalData = f"{data}{TagFormat(config.Tag63_CRC, check_sum).upper()}"
    return finalData


def TextThaiQRTag29Format(model: DataQRModel, mode: str):
    if len(model.Amount) > 13:
        print(f"Error Length Amount Over limit, Maximum is 13 characters")
        return None
    config = ThaiQRCodeConfig
    datalist = []
    tag29datalist = []

    datalist.append(TagFormat(config.Tag00_PayloadFormat, config.Tag00_PayloadEMVCo_QRCode))
    datalist.append(TagFormat(config.Tag01_PointOfInitiation,
                              config.Tag01_POIDynamicMode if model.Amount != '' else config.Tag01_POIStaticMode))
    tag29datalist.append(TagFormat(config.TagAID, config.TagAID_MerchantPresentedQR))  # Mode

    if mode == "mobile":
        tag29datalist.append(TagFormat(config.Tag29_MobileNo, model.BillerId))
    elif mode == "taxid":
        tag29datalist.append(TagFormat(config.Tag29_NID_TaxID, model.BillerId))
    elif mode == "Ewall":
        tag29datalist.append(TagFormat(config.Tag29_EWallletId, model.BillerId))
    elif mode == "BankAccount":
        tag29datalist.append(TagFormat(config.Tag29_BankAccount, model.BillerId))
    tag29data = ''.join(tag29datalist)

    datalist.append(TagFormat(config.Tag29_CreditTransferWithPromptPayId, tag29data))
    datalist.append(TagFormat(config.Tag53_TransactionCurrency, config.Tag53_TransactionCurrency_THB))
    datalist.append(TagFormat(config.Tag54_TransactionAmount, model.Amount if model.Amount != '' else ''))
    datalist.append(TagFormat(config.Tag58_CountryCode, config.Tag58_CountryCode_TH))
    data = ''.join(datalist)

    check_sum = f"{data}{config.Tag63_CRC}04"
    finalData = f"{data}{TagFormat(config.Tag63_CRC, CRC16CCITT(check_sum)).upper()}"
    return finalData

def TagFormat(TagId: str, Data: str):
    dataLen = f"00{len(Data)}"
    return f"{TagId}{dataLen[len(dataLen) - 2:]}{Data}"


def ValidateData(model: DataQRModel):
    if len(model.Ref1) > 20:
        print(f"Error Length Reference1 Over limit, Maximum is 20 characters")
        return False
    if len(model.Ref2) > 20:
        print(f"Length Reference2 Over limit, Maximum is 20 characters")
        model.Ref2 = model.Ref2.replace(" ", "").replace("-", "").replace("_", "").upper()[0:20]
    if model.Ref2 == "nan":
        model.Ref2.replace("nan","")
    if len(model.Amount) > 13:
        print(f"Error Length Amount Over limit, Maximum is 13 characters")
        return False

    return True


def CRC16CCITT(data: str, polynomial: int = 0x1021, crc: int = 0xFFFF):
    byteArray = bytes(data, 'ascii')
    for b in byteArray:
        for i in range(8):
            bit = (b >> 7 - i & 1) == 1
            c15 = (crc >> 15 & 1) == 1
            crc <<= 1
            if (c15 ^ bit): crc ^= polynomial
    crc &= 0xFFFF
    print(('{:04x}'.format(crc).upper()), crc)
    return '{:04x}'.format(crc).upper()
