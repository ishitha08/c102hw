import cv2 
import dropbox
import time
import random


def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    return image_name
    print("snapshot taken")

    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "BcVeMSFv9KAAAAAAAAAADyMXZDGx8wxuDd9pThdhR70lAuz3BFGOvWf7-UdBqpMl"
    file = img_counter
    file_from = file
    file_to = "/newfolder/"+(image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')


def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)

    main()
