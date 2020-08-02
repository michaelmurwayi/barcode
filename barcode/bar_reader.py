from pyzbar import pyzbar
import argparse
import cv2


def arg():

    # construct parser and arg to pass
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True)
    args = vars(ap.parse_args())

    return args

def get_barcode_data(image_path):

    # load image to cv2 from args and decode
    
    image = cv2.imread(image_path)
    # finds barcode in image and decodes each barcode
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        # get the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  
        
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)

        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        print(barcodeData)
        return barcodeData

        
if __name__ == '__main__':
    get_barcode_data("test2.jpeg")
