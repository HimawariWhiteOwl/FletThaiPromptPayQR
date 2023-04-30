from Model.DataQRCodeModel import DataQRModel
import qrcode as qrc
from PIL import Image
import os


def CreateQRPicture(data: str, model: DataQRModel, Comment: str = "",Bank: str = ""):
    baseheight = 100
    face = Image.open('thai-qr-payment.png')
    hpercent = (baseheight / float(face.size[1]))
    wsize = int((float(face.size[0]) * float(hpercent)))
    face = face.resize((wsize, baseheight))  # Image.ANTIALIAS
    qr_big = qrc.QRCode(version=1, box_size=10, border=2, error_correction=qrc.constants.ERROR_CORRECT_H)
    qr_big.add_data(data)
    qr_big.make(fit=True)
    img_qr_big = qr_big.make_image(fill_color='#000000', back_color='#FFFFFF').convert('RGB')
    pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
    img_qr_big.paste(face, pos)

    path = "QRPicture"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    BankisExist = os.path.exists(f"{path}/{Bank}")
    if not BankisExist:
        os.makedirs(f"{path}/{Bank}")
    filePath = f"{path}/{Bank}/{Bank}-QR Tnx {model.Ref1} Amount {model.Amount} {Comment}.png"
    if os.path.exists(filePath):
        os.remove(filePath)
    img_qr_big.save(filePath)
    return filePath