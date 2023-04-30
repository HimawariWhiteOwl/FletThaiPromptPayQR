class ThaiQRCodeConfig:
    #TagId
    Tag00_PayloadFormat: str = "00"
    Tag01_PointOfInitiation: str = "01"
    Tag29_CreditTransferWithPromptPayId: str = "29"
    Tag30_BillPayment: str = "30"
    Tag53_TransactionCurrency: str = "53"
    Tag54_TransactionAmount: str = "54"
    Tag58_CountryCode: str = "58"
    Tag59_MerchantName: str = "59"
    Tag63_CRC: str = "63"
    #TagData
    Tag00_PayloadEMVCo_QRCode: str = "01"
    Tag01_POIStaticMode: str = "11"
    Tag01_POIDynamicMode: str = "12"
    TagAID: str = "00"

    Tag29_MobileNo: str = "00"
    Tag29_NID_TaxID: str = "02"
    Tag29_EWallletId: str = "03"
    Tag29_BankAccount: str = "04"

    Tag30_BillerId: str = "01"
    Tag30_Ref1: str = "02"
    Tag30_Ref2: str = "03"

    TagAID_MerchantPresentedQR: str = "A000000677010111"
    TagAID_CustomerPresentedQR: str = "A000000677010114"
    TagAID_DomesticMerchant: str = "A000000677010112"
    TagAID_CrossBorderMerchant: str = "A000000677012006"

    Tag53_TransactionCurrency_THB: str = "764"
    Tag58_CountryCode_TH: str = "TH"

