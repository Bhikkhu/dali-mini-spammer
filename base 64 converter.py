import base64
img_data = ''
with open("base64.txt", "r") as f:
    img_data = f.read()
    img_data = str.encode(img_data)
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))
