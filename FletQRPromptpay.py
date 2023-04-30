import flet as ft
from Model.DataQRCodeModel import DataQRModel
from Function.GenerateQR import CreateQRPicture
from Function.NationalPaymentMessageStandart import TextNpmsFormat
from Function.ThaiQRFormat import TextThaiQRTag30Format, TextThaiQRTag29Format
def main(page: ft.Page):
    page.title = "Flet QR PromptPay"
    page.window_height = 1050
    page.window_width = 500
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 50
    def SelectPromptPayType(e):
        text.value = f"PromptPay Type is:  {qr_dropdown.value}"
        if qr_dropdown.value == "tag29":
            Id.label = "Enter Your TAX ID"
            Ref1.visible = False
            Ref2.visible = False
            MerchantName.value = False
            qr_modeForTag29.visible = True
        elif qr_dropdown.value == "tag30":
            Id.label = "Enter Your Biller ID"
            Ref1.visible = True
            Ref2.visible = True
            MerchantName.visible = True
            qr_modeForTag29.visible = False
        elif qr_dropdown.value == "npms":
            Id.label = "Enter Your Biller ID BOT Formate"
            Ref1.visible = True
            Ref2.visible = True
            MerchantName.visible = False
            qr_modeForTag29.visible = False
        page.update()

    def GenerateQRImage(e):
        print(qr_dropdown.value)
        print(qr_modeForTag29.value)
        print(f"{Id.value}, {Ref1.value}, {Ref2.value}, {promptpayAmount.value}, {MerchantName.value}")
        if promptpayAmount.value == "" or Id.value == "":
            if Id.value == "":
                Id.error_text = "Missing Promptpay Id"
            if promptpayAmount.value == "":
                promptpayAmount.error_text = "Missing amount"

            page.update()
            return
        model = DataQRModel
        model.BillerId = Id.value
        model.Ref1 = Ref1.value
        model.Ref2 = Ref2.value
        Amount = float(promptpayAmount.value)
        strAmount = "{:.2f}".format(Amount)
        model.Amount = strAmount
        data = ""
        if qr_dropdown.value == "tag29":

            data = TextThaiQRTag29Format(model, qr_modeForTag29.value)
        elif qr_dropdown.value == "tag30":
            if Ref1.value == "" or Ref2.value == "":
                if Ref1.value == "":
                    Ref1.error_text = "Missing Reference 1"
                if Ref2.value == "":
                    Ref2.error_text = "Missing Reference 2"
                page.update()
                return
            data = TextThaiQRTag30Format(model, MerchantName.value)
        elif qr_dropdown.value == "npms":
            data = TextNpmsFormat(model)

        path = CreateQRPicture(data, model, 'xxxx', "My")
        promptpayimg.src = path



        page.update()

    qr_dropdown = ft.Dropdown(
        width=400,
        options=[
            ft.dropdown.Option(text="Tag29", key="tag29"),
            ft.dropdown.Option(text="Tag30", key="tag30"),
            ft.dropdown.Option(text="BOT Formate", key="npms"),
        ],
        value="tag29",

        on_change=SelectPromptPayType,
    )
    qr_modeForTag29 = ft.Dropdown(
        width=400,
        options=[
            ft.dropdown.Option(text="MobileNo", key="mobile"),
            ft.dropdown.Option(text="NID_TaxID", key="taxid"),
            ft.dropdown.Option(text="E-wallet", key="Ewall"),
            ft.dropdown.Option(text="Bank Account", key="BankAccount")
        ],
        value="mobile"
    )

    text = ft.Text()
    Id = ft.TextField(label="Enter Your PromptPay ID",width=400)
    Ref1 = ft.TextField(label="Enter Your Reference1", visible=False, width=400)
    Ref2 = ft.TextField(label="Enter Your Reference2", visible=False, width=400)
    MerchantName = ft.TextField(label="Enter Merchant Name", visible=False, width=400)
    promptpayAmount = ft.TextField(label="Enter Your Amount", width=400)
    promptpayimg = ft.Image(src="thai-qr-payment.png",width=400,height=400)
    btnGenerateQR = ft.ElevatedButton(text="Generate QR", width=400,on_click=GenerateQRImage)

    col = ft.Column(controls=[qr_dropdown, text, qr_modeForTag29, Id, Ref1, Ref2, MerchantName, promptpayAmount, promptpayimg, btnGenerateQR])
    row = ft.Row(controls=[col], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row)

ft.app(target=main)