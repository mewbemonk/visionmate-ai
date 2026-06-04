import cv2
import time
from img_to_text.ocr import frame_text
from text_to_speech.pyttsx import voice
from ocr_data_collector.data import add_text,enough_data,get_all_text
from agents.fix_ocr_text_agent import fix_ocr_text
from agents.response_agent import response
from memory.context import save_context






def webcam():
    
    cap = cv2.VideoCapture(0)


    last_time = 0
    

    while cap.isOpened():

        ret , frame = cap.read()

        if not ret:

            print("frame is not captured properly ...")

            break

        cv2.imshow("webcam-frame",frame)

        if time.time() - last_time >= 2:

            current_text = frame_text(frame)

            if current_text:

                print("Collected:", get_all_text())

                add_text(current_text)

                print(current_text)

                last_time = time.time()

        
        if enough_data():

            history = get_all_text()

            print(history)

            final_text = fix_ocr_text(history)

            save_context(final_text)

            final_response = response(final_text)

            print(final_response)

            voice(final_response)

            break

        
        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):

            print('quitting...')
            break





    cap.release()

    cv2.destroyAllWindows()


webcam()