import flet as ft
from Model.DataQRCodeModel import DataQRModel
from Function.GenerateQR import CreateQRPicture
from Function.NationalPaymentMessageStandart import TextNpmsFormat
from Function.ThaiQRFormat import TextThaiQRTag30Format, TextThaiQRTag29Format

def main(page: ft.Page):

    def button_clicked(e):
        dataType = type.value
        model = DataQRModel
        model.BillerId = taxId.value
        model.Ref1 = ref1.value
        model.Ref2 = ref2.value
        model.Amount = amount.value
        path = None
        if dataType == "Tag30":
            MerchantName = "PRAINFINTECH COMPANY"
            data = TextThaiQRTag30Format(model, MerchantName)
            path = CreateQRPicture(data, model, "QR30 Flet", "KTB")
            img.src = path
        elif dataType == "Tag29":
            data = TextThaiQRTag29Format(model)
            path = CreateQRPicture(data, model, 'QR29 Flet', "My")
            img.src = path
        elif dataType == "BOT FORMAT":
            data = TextNpmsFormat(model)
            print(data)
            path = CreateQRPicture(data, model, 'QR BOT Flet', "CIMB")
            img.src = path
        page.update()
    taxId = ft.TextField(label="Your TAX ID")
    type = ft.Dropdown(
        # width=200,
        options=[
            ft.dropdown.Option("Tag30"),
            ft.dropdown.Option("Tag29"),
            ft.dropdown.Option("BOT FORMAT"),
        ],
    )
    ref1 = ft.TextField(label="Your Ref1")
    ref2 = ft.TextField(label="Your Ref2")
    amount = ft.TextField(label="Amount")
    img = ft.Image(src=f"C:/Users/WhiteOwl/Downloads/HimaFixBugDis.png", width=500, height=500)
    b = ft.TextButton("Gen QR", on_click=button_clicked)





    page.add(type, taxId, ref1, ref2, amount, img, b)


ft.app(
    target=main,
    assets_dir="assets"
)
