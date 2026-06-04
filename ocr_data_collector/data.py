ocr_data = []


def add_text(text):
    if text.strip():
        return ocr_data.append(text)
    

def enough_data():
    if len(ocr_data) >= 5:
        return True
    

def get_all_text():
    return ocr_data