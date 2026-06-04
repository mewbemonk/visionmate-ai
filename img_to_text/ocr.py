import easyocr

reader = easyocr.Reader(['en'],gpu=False)

def frame_text(frame:str)->str:

    res = ""

    img_text = reader.readtext(frame)

    for text in img_text:

        res += text[1] + " "

    return res



