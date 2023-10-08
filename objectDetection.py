import GPTRecommendation as gpt
import webscraper as ws
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
import csv

video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("Object Detection", output_image)
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

def main():
    for i in labels:
        if(i != "person"):
            recommends = gpt.get_Recommendation(i)
            recommendations = recommends.split(",")
            print("3 items ChatGPT would recommend similar to " + i + " is " + recommendations[0] + ", " + recommendations[1] + ", " + recommendations[2])
            
            returnInfo = ws.get_page_content(i)
            print("\nThe top results on Amazon.com are: ")

            for i in range(len(returnInfo[0])):
                x = i + 1
                print(f"{x}. ")
                print("The name of this item is", returnInfo[0][i])
                print("The price of this item is", returnInfo[1][i])
                print("The star rating of this item is", returnInfo[2][i] + "\n")
            time.sleep(3)

if __name__ == "__main__":
    main()
